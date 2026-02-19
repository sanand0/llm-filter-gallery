#!/usr/bin/env bash
# Filter v4: Risograph Reverie
# Apply with: bash filter.sh [input.avif]
set -e

INPUT="${1:-inputs/comic.avif}"
OUTPUT="$(dirname "$0")/output.webp"
TMP=$(mktemp /tmp/filter_v4_XXXXXX.png)

ffmpeg -y -i "$INPUT" "$TMP" 2>/dev/null

python3 - "$TMP" "$OUTPUT" <<'PYEOF'
import sys, os, math
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageDraw
from scipy.ndimage import gaussian_filter, uniform_filter

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert('RGB')

# ---- Filter v4: Risograph Reverie ----
# Run: python3 generate_v4_v30.py  to regenerate all outputs.
# This script is auto-generated. For the full implementation see generate_v4_v30.py

import subprocess, importlib.util, tempfile, pathlib
gen = pathlib.Path(__file__).parent.parent.parent / 'generate_v4_v30.py'
spec = importlib.util.spec_from_file_location('gen', gen)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.APPLY_FNS[4](img)
result.save(dst, 'WEBP', quality=75, method=6)
print(f'Saved: {dst}')
PYEOF

rm -f "$TMP"
echo "Done: $OUTPUT"
