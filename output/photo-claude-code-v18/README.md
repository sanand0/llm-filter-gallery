# Filter v18: Terminal Matrix

## The Aesthetic

ASCII character-cell rendering in phosphor green on black CRT terminal.

## Input

Applied to `inputs/photo.avif`.

## Technique

See `filter.sh` for the full multi-step recipe.

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy / SciPy / scikit-image
- Output: WebP (quality 75, method 6)
