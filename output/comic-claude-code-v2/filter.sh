#!/usr/bin/env bash
# Filter: Thermal Scan
# Maps image luminance to a thermal colormap (black→purple→red→orange→yellow→white)
# then adds CRT scanlines and a vignette for a sci-fi sensor aesthetic.
set -e

INPUT="${1:-inputs/chart.avif}"
OUTPUT="$(dirname "$0")/output.webp"
TMP=$(mktemp /tmp/thermal_scan_XXXXXX.png)

ffmpeg -y -i "$INPUT" "$TMP" 2>/dev/null

python3 - "$TMP" "$OUTPUT" <<'PYEOF'
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert("RGB")
w, h = img.size

# --- Boost contrast before mapping so the chart details pop ---
img = ImageEnhance.Contrast(img).enhance(1.4)
img = ImageEnhance.Sharpness(img).enhance(1.6)

# Luminance
gray = np.array(img.convert("L"), dtype=np.float32) / 255.0

# --- Thermal colormap: 8-stop gradient ---
stops = np.array([0.00, 0.12, 0.28, 0.45, 0.60, 0.75, 0.88, 1.00])
colors = np.array([
    [  0,   0,   0],   # black      (cold)
    [ 60,   0, 120],   # deep purple
    [180,   0,  80],   # magenta-red
    [230,  30,   0],   # red
    [255, 120,   0],   # orange
    [255, 230,   0],   # yellow
    [255, 255, 160],   # pale yellow
    [255, 255, 255],   # white       (hot)
], dtype=np.float32)

t = gray.ravel()
R = np.interp(t, stops, colors[:, 0])
G = np.interp(t, stops, colors[:, 1])
B = np.interp(t, stops, colors[:, 2])
thermal = np.stack([R, G, B], axis=1).reshape(h, w, 3).astype(np.uint8)
result = Image.fromarray(thermal)

# --- CRT scanlines: darken every 3rd row slightly ---
arr = np.array(result, dtype=np.float32)
arr[0::3, :, :] *= 0.65
arr[1::3, :, :] *= 0.90

# --- Horizontal phosphor smear: slight blur ---
result = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))
result = result.filter(ImageFilter.GaussianBlur(radius=0.6))

# --- Vignette ---
vx = np.linspace(-1, 1, w)
vy = np.linspace(-1, 1, h)
vX, vY = np.meshgrid(vx, vy)
vignette = np.clip(1.0 - (vX**2 + vY**2) * 0.55, 0.15, 1.0)
arr = np.array(result, dtype=np.float32)
arr *= vignette[:, :, np.newaxis]

# --- Slight noise for CRT grain ---
noise = np.random.normal(0, 4, arr.shape)
arr = np.clip(arr + noise, 0, 255)

Image.fromarray(arr.astype(np.uint8)).save(dst, "WEBP", quality=75, method=6)
print(f"Saved: {dst}")
PYEOF

rm -f "$TMP"
echo "Done: $OUTPUT"
