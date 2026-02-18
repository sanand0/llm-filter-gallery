#!/usr/bin/env bash
# Filter: Gilded Woodblock
# Transforms the chart into a Japanese ukiyo-e woodblock print:
# posterized tones, ink-carved edges, aged parchment palette, woodgrain texture.
set -e

INPUT="${1:-inputs/chart.avif}"
OUTPUT="$(dirname "$0")/output.webp"
TMP=$(mktemp /tmp/woodblock_XXXXXX.png)

ffmpeg -y -i "$INPUT" "$TMP" 2>/dev/null

python3 - "$TMP" "$OUTPUT" <<'PYEOF'
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert("RGB")
w, h = img.size

# --- Step 1: Posterize to a limited tonal range (woodblock has few ink layers) ---
posterized = img.convert("L")
posterized = ImageEnhance.Contrast(Image.fromarray(
    (np.floor(np.array(posterized, dtype=np.float32) / 42) * 42).clip(0, 255).astype(np.uint8)
)).enhance(1.2)

# --- Step 2: Extract ink edges (sharp carved lines) ---
edges = posterized.filter(ImageFilter.FIND_EDGES)
edges = ImageOps.autocontrast(edges, cutoff=3)
edges_arr = np.array(edges, dtype=np.float32) / 255.0

# --- Step 3: Build the ukiyo-e color palette ---
# Paper: aged parchment gold
# Dark plate: deep sumi ink (near-black with blue-black tint)
# Mid plate: burnt sienna / ochre
# Light plate: pale celadon green
gray_arr = np.array(posterized, dtype=np.float32) / 255.0

# Tone-map gray levels to palette colors via 5-stop interpolation
stops  = np.array([0.00, 0.25, 0.50, 0.75, 1.00])
c_R = np.array([ 15,  80, 185, 220, 240], dtype=np.float32)  # R channel
c_G = np.array([ 12,  55, 140, 195, 225], dtype=np.float32)  # G channel
c_B = np.array([ 25,  40,  80, 155, 195], dtype=np.float32)  # B channel

t = gray_arr.ravel()
R = np.interp(t, stops, c_R)
G = np.interp(t, stops, c_G)
B = np.interp(t, stops, c_B)
palette = np.stack([R, G, B], axis=1).reshape(h, w, 3)

# --- Step 4: Stamp ink edges as near-black sumi ---
ink_mask = edges_arr[:, :, np.newaxis]
ink_color = np.array([14, 12, 22], dtype=np.float32)  # sumi ink
palette = palette * (1 - ink_mask * 0.92) + ink_color * ink_mask * 0.92

# --- Step 5: Paper texture - horizontal woodgrain lines ---
rng = np.random.default_rng(42)
grain_h = rng.normal(0, 1.8, (h, 1)) * np.ones((1, w))   # horizontal bands
grain_n = rng.normal(0, 3.5, (h, w))                       # fine noise
palette += grain_h[:, :, np.newaxis] * 0.6 + grain_n[:, :, np.newaxis] * 0.5

# --- Step 6: Warm the highlights with a golden tint ---
lum = (palette[:, :, 0] * 0.299 + palette[:, :, 1] * 0.587 + palette[:, :, 2] * 0.114)
gold_mask = (lum / 255.0) ** 2  # more effect in bright areas
palette[:, :, 0] += gold_mask * 14
palette[:, :, 1] += gold_mask * 6
palette[:, :, 2] -= gold_mask * 8

# --- Step 7: Slight vignette (tea-stained edges) ---
vx = np.linspace(-1, 1, w)
vy = np.linspace(-1, 1, h)
vX, vY = np.meshgrid(vx, vy)
vignette = np.clip(1.0 - (vX**2 + vY**2) * 0.30, 0.70, 1.0)
palette *= vignette[:, :, np.newaxis]

result = Image.fromarray(np.clip(palette, 0, 255).astype(np.uint8))

# Final subtle emboss to reinforce carved texture
result = result.filter(ImageFilter.SMOOTH)

result.save(dst, "WEBP", quality=75, method=6)
print(f"Saved: {dst}")
PYEOF

rm -f "$TMP"
echo "Done: $OUTPUT"
