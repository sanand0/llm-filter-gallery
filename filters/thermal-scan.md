# Filter 2: Thermal Scan

## The Aesthetic

A false-color thermal imaging sensor readout. The chart becomes a heat-map
as if captured by an infrared camera — cold regions in deep purple, mid-values
burning red-orange, peaks blazing yellow-white. Overlaid CRT scanlines give it
the feel of vintage scientific instrumentation.

## Why It's Interesting

Thermal colormapping is a classic perceptual trick: it reassigns luminance to a
perceptually non-linear hue progression that our eyes parse faster than greyscale.
Applied to a data chart, it:

- Immediately highlights _hot_ (high-value) regions versus _cold_ (low-value) ones
- Turns a dry visualization into something viscerally dramatic
- The scanline + noise layer adds temporal texture — it looks _live_, as if the
  sensor is actively reading out

This filter demonstrates how re-encoding the same data through a different visual
channel (hue rather than shape) can radically change how the information is felt.

## Technique

Multi-step recipe using Python + PIL + NumPy:

1. **Pre-enhance** — Contrast ×1.4, Sharpness ×1.6 to exaggerate chart details
   before the colormap flattens them into luminance
2. **8-stop thermal LUT** — manual gradient interpolation across
   `black → deep-purple → magenta-red → red → orange → yellow → pale-yellow → white`
   applied per-pixel via `np.interp` on flattened luminance
3. **CRT scanlines** — rows 0::3 dimmed to 65%, rows 1::3 to 90%, leaving
   rows 2::3 at full brightness (3-row cadence = ~144 "lines" on a 1024px image)
4. **Phosphor smear** — subtle Gaussian blur (σ=0.6) softens the scanline
   banding to mimic phosphor persistence
5. **Vignette + noise** — radial vignette floored at 15%, plus Gaussian noise
   σ=4 for CRT grain

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy
- Output: WebP (quality 75, method 6)
