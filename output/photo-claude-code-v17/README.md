# Filter v17: CMYK Separation

## The Aesthetic

Four-colour halftone dot screens (C/M/Y/K) at different angles with slight misregistration.

## Input

Applied to `inputs/photo.avif`.

## Technique

See `filter.sh` for the full multi-step recipe.

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy / SciPy / scikit-image
- Output: WebP (quality 75, method 6)
