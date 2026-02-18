# Filter 1: Neon Blueprint

## The Aesthetic

A dark technical schematic — as if the chart was redrawn on a circuit-board plotter
and backlit with cyan phosphor. Think: hacker terminal meets engineering blueprint.

## Why It's Interesting

Charts are inherently technical objects. This filter leans into that identity by:
- Stripping all fill/color information and rebuilding only the *structure* (edges)
- Placing that structure on a deep navy field to maximize contrast
- Layering three glow halos (sharp core → medium diffuse → wide bloom) to simulate
  the soft luminance of an actual phosphor display
- Overlaying a faint grid that echoes engineering graph paper without overwhelming

The result makes data-ink relationships *spatial* — you see the skeleton of the chart,
not its surface. Dense regions glow brighter; sparse regions recede into darkness.
It's a filter that reveals topology.

## Technique

Multi-step recipe using Python + PIL + numpy:

1. **Edge extraction** — UnsharpMask pre-sharpening → `FIND_EDGES` → `autocontrast`
2. **Triple-layer glow** — Gaussian blur at σ=3 (medium) and σ=8 (wide) blended at
   different intensities to build a halo effect around each edge
3. **Dark canvas construction** — numpy array seeded at near-black navy, with a
   sub-pixel grid baked in at 8 px/channel for the blueprint grid
4. **Additive color compositing** — edges and glows added with cyan-weighted
   (R=60, G=255, B=255 for core; G-dominant for halos)
5. **Radial vignette** — parabolic darkening toward corners, floored at 30%
   to preserve the dark aesthetic without pure black edges

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy
- Output: WebP (quality 75, method 6)
