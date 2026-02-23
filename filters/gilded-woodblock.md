# Filter 3: Gilded Woodblock

## The Aesthetic

A Japanese ukiyo-e woodblock print. The chart is reborn as a hand-carved print
on aged parchment: tones reduced to a few discrete ink layers, edges rendered as
bold carved lines in sumi ink, the palette drawn from celadon, indigo, ochre and
gold. Woodgrain noise and a tea-stained vignette complete the illusion.

## Why It's Interesting

Woodblock printing is inherently a _quantization_ technique — an artisan carves
discrete tonal layers, prints each in a separate pass, and accepts that the
medium imposes simplification. This filter maps that process onto a data chart:

- **Posterization** reduces continuous values to 6 tonal bands, which is honest
  about the resolution limits of the original printing craft
- **Ink edges** are extracted and stamped as near-black lines, mimicking the
  key-block (墨摺) that defines contours in traditional ukiyo-e
- **Palette mapping** routes the posterized grey levels through a 5-stop
  gradient from deep sumi through indigo, celadon mid-tones, to warm gold
  highlights — the characteristic cool-to-warm shift of Edo-period printmaking
- Horizontal **woodgrain noise** (seeded RNG for reproducibility) simulates
  the fibrous texture of the printing block bleeding through the washi paper
- A golden highlight tint warms luminous regions, evoking the gold-leaf
  accents that appear in premium _nishiki-e_ prints

The result is meditative and tactile: a data visualization that looks like it
could hang in a museum alongside Hokusai.

## Technique

Multi-step recipe using Python + PIL + NumPy:

1. **Posterize** — quantize luminance to 6 bands (floor to nearest 42/255 step)
2. **Edge carving** — `FIND_EDGES` + `autocontrast` on posterized grey layer
3. **5-stop palette LUT** — `np.interp` maps grey → (R,G,B) through a
   curated indigo-celadon-gold gradient
4. **Sumi ink stamp** — edges blended at 92% opacity toward `[14, 12, 22]`
   (near-black with a blue undertone, matching real sumi ink)
5. **Woodgrain texture** — horizontal `rng.normal(σ=1.8)` bands + fine
   isotropic `rng.normal(σ=3.5)` noise added to palette
6. **Golden highlight** — quadratic luminance mask brightens R, adds G,
   subtracts B in bright areas for a warm golden tint
7. **Vignette + smooth** — radial vignette floored at 70%, final `SMOOTH`
   pass to unify ink transitions

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy
- Output: WebP (quality 75, method 6)
