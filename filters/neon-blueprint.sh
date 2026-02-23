#!/usr/bin/env bash
# Filter: Neon Blueprint
# Converts the chart into a dark technical schematic with glowing cyan edges.
set -e

INPUT="${1:-inputs/chart.avif}"
OUTPUT="$(dirname "$0")/output.webp"
TMP=$(mktemp /tmp/neon_blueprint_XXXXXX.png)

# Step 1: Convert AVIF to PNG using ffmpeg
ffmpeg -y -i "$INPUT" "$TMP" 2>/dev/null

# Step 2: Apply the Python filter
python3 - "$TMP" "$OUTPUT" <<'PYEOF'
import sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageDraw

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert("RGB")
w, h = img.size

# --- Edge extraction ---
gray = img.convert("L")
# Enhance edges with a sharpened source before detecting
sharp = gray.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
edges = sharp.filter(ImageFilter.FIND_EDGES)
edges = ImageOps.autocontrast(edges, cutoff=1)

# Glow = blurred version of edges
glow_sm = edges.filter(ImageFilter.GaussianBlur(3))
glow_lg = edges.filter(ImageFilter.GaussianBlur(8))

# --- Build dark navy canvas ---
bg = np.zeros((h, w, 3), dtype=np.float32)
bg[:, :, 2] = 18   # faint blue base

# Draw a subtle grid
grid_step = 48
bg[::grid_step, :, 1] += 8
bg[::grid_step, :, 2] += 22
bg[:, ::grid_step, 1] += 8
bg[:, ::grid_step, 2] += 22

# --- Layer edges + glow in cyan-white ---
e  = np.array(edges,   dtype=np.float32) / 255.0
gs = np.array(glow_sm, dtype=np.float32) / 255.0
gl = np.array(glow_lg, dtype=np.float32) / 255.0

# Large glow: blue tint
bg[:, :, 0] += gl * 40
bg[:, :, 1] += gl * 100
bg[:, :, 2] += gl * 160

# Medium glow: cyan
bg[:, :, 0] += gs * 10
bg[:, :, 1] += gs * 200
bg[:, :, 2] += gs * 230

# Sharp edges: near-white cyan core
bg[:, :, 0] += e * 60
bg[:, :, 1] += e * 255
bg[:, :, 2] += e * 255

# Clamp and build result
result = Image.fromarray(np.clip(bg, 0, 255).astype(np.uint8))

# --- Vignette (soft dark corners) ---
vx = np.linspace(-1, 1, w)
vy = np.linspace(-1, 1, h)
vX, vY = np.meshgrid(vx, vy)
vignette = np.clip(1.0 - (vX**2 + vY**2) * 0.45, 0.3, 1.0)
arr = np.array(result, dtype=np.float32)
arr *= vignette[:, :, np.newaxis]
result = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

result.save(dst, "WEBP", quality=75, method=6)
print(f"Saved: {dst}")
PYEOF

rm -f "$TMP"
echo "Done: $OUTPUT"
