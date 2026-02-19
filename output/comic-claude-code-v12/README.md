# Filter v12: Signal Corrupted

## The Aesthetic

Digital glitch with scan-line displacement, RGB bleed, block corruption, and neon noise.

## Input

Applied to `inputs/comic.avif`.

## Technique

See `filter.sh` for the full multi-step recipe.

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy / SciPy / scikit-image
- Output: WebP (quality 75, method 6)
