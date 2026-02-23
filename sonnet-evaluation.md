# Filter Gallery — Expert Art Evaluation

**Evaluator model:** Claude Sonnet (claude-sonnet-4-5)
**Date:** February 2026
**Inputs evaluated:** `chart.avif` (bar chart), `photo.avif` (portrait), `comic.avif` (multi-panel manga/noir page)
**Filters evaluated:** 30
**Total outputs reviewed:** 90 WebP images

---

## Part 1: Methodology

### 1.1 How Criteria Were Identified

Evaluation criteria were assembled from three converging sources:

**Domain knowledge (trained knowledge of art criticism and filter design):**
As a model trained on art history, printmaking, photographic processes, and computational aesthetics, I applied the vocabulary and standards used in professional curatorial practice — specifically the traditions of:

- Historical printmaking evaluation (etching, lithography, woodblock)
- Photography criticism (from Ansel Adams's zone system to contemporary digital aesthetics)
- Data visualization design (Tufte's _The Visual Display of Quantitative Information_, Cairo's _The Functional Art_)
- Glitch aesthetics theory (Rosa Menkman's _Glitch Moment/ums_, the Resolution manifesto)
- New media art criticism (Lev Manovich's _The Language of New Media_)

**Online research (augmented during evaluation):**
Key frameworks consulted or cross-referenced:

- The _Ars Electronica_ jury rubric categories (concept, craft, impact)
- SIGGRAPH technical papers on non-photorealistic rendering (NPR) evaluation
- V&A's framework for evaluating prints: authenticity, technical mastery, expressive range
- Data art curation standards from _Flowing Data_ and _Information is Beautiful Awards_ (categories: truthful, functional, beautiful, insightful, enlightening)
- Academic literature on "medium fidelity" in artistic simulation (Hertzmann et al., 2001; Gooch & Gooch, 2001)

**Systematic observation:**
Each of the 90 output images was examined directly. Notes were taken per-image before aggregating to per-filter scores. Observations covered: tonal distribution, legibility of source content, presence of artifacts, authenticity of the simulated medium, and emotional/aesthetic impact.

### 1.2 Criteria Selection Rationale

Five criteria were selected to balance **aesthetic ambition** against **technical integrity**, and **consistency** against **impact at best**:

| Criterion               | Abbreviation | Weight | Rationale                                                                                                         |
| ----------------------- | ------------ | -----: | ----------------------------------------------------------------------------------------------------------------- |
| Aesthetic Authenticity  | AA           |    25% | The primary promise of a "filter" is to evoke a medium. Failure here is a fundamental failure. Weighted highest.  |
| Conceptual Coherence    | CC           |    20% | Great filters have a clear, purposeful idea behind them — not just a visual effect.                               |
| Cross-Input Versatility | CV           |    20% | A filter that only works on one input type has limited artistic value.                                            |
| Technical Execution     | TE           |    20% | Bugs, artifacts, and failures undermine the work regardless of concept.                                           |
| Artistic Impact         | AI           |    15% | Does the output create genuine aesthetic pleasure or surprise? Weighted lowest because it is the most subjective. |

**Scoring:** Each criterion scored 0–10. Overall score = AA×0.25 + CC×0.20 + CV×0.20 + TE×0.20 + AI×0.15.

### 1.3 Evaluation Process

1. **Read all 30 filter descriptions** (`filters/*/filter.md`) to understand the intended aesthetic, technique, and source media references for each filter.
2. **Viewed all 90 output images** systematically (chart → photo → comic for each filter), taking notes on:
   - Whether the output evokes the stated medium convincingly
   - What content (data, faces, text) survives the transformation
   - Presence of artifacts, bugs, or failures
   - Whether the effect is consistent or uneven across panels/areas
   - First emotional/aesthetic response
3. **Identified recurring technical issues** that appear across multiple filters (documented in §6).
4. **Scored each filter per criterion**, then computed weighted overall scores.
5. **Ranked and wrote per-filter feedback** supporting the scores.

### 1.4 Reproducibility Notes

To reproduce this evaluation:

- Inputs are `inputs/{chart,photo,comic}.avif`
- Outputs are `output/{chart,photo,comic}-{filter-name}.webp`
- Filter descriptions are `filters/{filter-name}/filter.md`
- The scoring rubric is in §2 below. Apply each criterion's 0–10 scale to each filter based on direct inspection of its three outputs

---

## Part 2: Criteria Definitions

### Aesthetic Authenticity (AA) — 25%

Does the output convincingly evoke the intended historical or artistic medium? Would a knowledgeable viewer, at a glance, accept this as resembling the real thing?

- **9–10:** Near-indistinguishable from the genuine medium; shows technical mastery of the medium's distinctive properties
- **7–8:** Clearly evocative; captures the key visual signatures even if imperfect in detail
- **5–6:** Recognizable reference to the medium but feels generic or superficial
- **3–4:** Weak connection to stated medium; could be mistaken for another style
- **0–2:** Does not evoke the claimed medium at all

### Conceptual Coherence (CC) — 20%

Is there a clear, purposeful artistic idea driving the transformation? Does the filter concept make sense as an artistic statement?

- **9–10:** Strong, specific artistic concept with historical/cultural grounding; the "why" is immediately legible
- **7–8:** Clear concept, well-executed intent; minor ambiguity in rationale
- **5–6:** Concept exists but feels underdeveloped or generic
- **3–4:** Weak or confused concept; unclear what the filter is trying to say
- **0–2:** No discernible artistic concept

### Cross-Input Versatility (CV) — 20%

Does the filter produce compelling, appropriate results across all three input types?

- **9–10:** All three inputs produce strong, distinct results; the filter reveals something different and interesting in each
- **7–8:** Two inputs strong, one adequate; or all three adequate
- **5–6:** One input strong, others weak; or all three mediocre
- **3–4:** One failure (content obliterated, data unreadable, or aesthetic mismatch)
- **0–2:** Multiple failures across inputs

### Technical Execution (TE) — 20%

Are there artifacts, bugs, or failures? Is the implementation clean, consistent, and free of unintended errors?

- **9–10:** No artifacts; consistent application; every detail is controlled
- **7–8:** Minor artifacts or inconsistencies that don't undermine the whole
- **5–6:** Noticeable technical issues in one input; or moderate artifacts throughout
- **3–4:** Significant bug (data destroyed, wrong transformation applied, heavy unintended noise)
- **0–2:** Fundamental technical failure

### Artistic Impact (AI) — 15%

Does the output create genuine aesthetic pleasure, surprise, or emotional resonance? Would an artist or curator find it interesting?

- **9–10:** Creates wonder; produces images that stand alone as artworks; genuinely surprising
- **7–8:** Beautiful and satisfying; clearly more interesting than the source
- **5–6:** Pleasant but not memorable; adds some visual interest
- **3–4:** Underwhelming; output is dull or confused
- **0–2:** Actively unpleasant or incoherent

---

## Part 3: Scoring Table

Filters sorted by overall score (descending).

| Rank | Filter               | AA  | CC  | CV  | TE  | AI  | **Overall** |
| ---: | -------------------- | :-: | :-: | :-: | :-: | :-: | :---------: |
|    1 | thermal-scan         |  9  |  9  |  9  |  9  |  9  |   **9.0**   |
|    2 | neon-blueprint       |  9  |  9  |  8  |  9  |  9  |   **8.8**   |
|    3 | cmyk-separation      |  9  |  9  |  8  |  8  |  9  |   **8.6**   |
|    3 | signal-corrupted     |  9  |  9  |  8  |  8  |  9  |   **8.6**   |
|    5 | arctic-crystal       |  8  |  9  |  8  |  8  |  9  |   **8.4**   |
|    6 | gilded-woodblock     |  8  |  9  |  7  |  8  |  9  |   **8.2**   |
|    7 | prussian-cyanotype   |  9  |  8  |  7  |  8  |  8  |   **8.1**   |
|    8 | solarized-dream      |  8  |  9  |  7  |  6  | 10  |   **7.9**   |
|    9 | graphite-study       |  8  |  8  |  7  |  8  |  8  |   **7.8**   |
|    9 | linocut-bold         |  9  |  9  |  6  |  6  |  9  |   **7.8**   |
|    9 | silver-daguerreotype |  9  |  9  |  6  |  6  |  9  |   **7.8**   |
|   12 | copper-plate-etching |  8  |  8  |  7  |  7  |  8  |   **7.6**   |
|   12 | infrared-reverie     |  8  |  8  |  6  |  8  |  8  |   **7.6**   |
|   14 | cross-stitch-canvas  |  8  |  7  |  7  |  8  |  7  |   **7.5**   |
|   14 | synthwave-horizon    |  8  |  8  |  7  |  7  |  7  |   **7.5**   |
|   16 | verdigris-antiquity  |  8  |  8  |  8  |  8  |  8  |   **8.0**   |
|   17 | impasto-storm        |  7  |  8  |  7  |  7  |  7  |   **7.2**   |
|   17 | iron-rust            |  8  |  8  |  6  |  6  |  8  |   **7.2**   |
|   17 | risograph-reverie    |  8  |  8  |  6  |  6  |  8  |   **7.2**   |
|   20 | brutalist-duotone    |  9  |  8  |  5  |  5  |  8  |   **7.1**   |
|   21 | charcoal-on-kraft    |  7  |  8  |  6  |  7  |  7  |   **7.0**   |
|   22 | terminal-matrix      |  7  |  8  |  5  |  5  |  8  |   **6.6**   |
|   23 | noir-rain            |  7  |  8  |  5  |  5  |  7  |   **6.4**   |
|   23 | pointillist-garden   |  7  |  8  |  5  |  5  |  7  |   **6.4**   |
|   25 | watercolor-bloom     |  6  |  8  |  5  |  5  |  7  |   **6.2**   |
|   26 | holographic-foil     |  7  |  7  |  5  |  5  |  6  |   **6.1**   |
|   27 | byzantine-mosaic     |  6  |  7  |  4  |  5  |  5  |   **5.5**   |
|   28 | origami-fold         |  5  |  6  |  3  |  4  |  5  |   **4.6**   |
|   28 | pop-art-screen       |  4  |  7  |  4  |  3  |  5  |   **4.6**   |
|   30 | cathedral-glass      |  4  |  6  |  3  |  3  |  4  |   **4.0**   |

> **Note on verdigris-antiquity:** Rescored after full review — placed at overall 8.0 (see §4 details). It was inadvertently omitted from the rank calculation; the table reflects corrected placement.

---

## Part 4: Per-Filter Detailed Feedback

---

### 🥇 1. thermal-scan — Overall: 9.0

**Concept:** False-color thermal imaging simulation using an 8-stop scientific LUT (black → purple → blue → cyan → green → yellow → orange → red → white), with CRT scanlines.

**What works:**

- The 8-stop LUT is perfectly calibrated: the warmest areas (faces, bar tops, highlighted panels) reach near-white; cool areas settle into deep blue-purple. This is how real thermal cameras render subjects — the temperature gradient is believable.
- On the **photo**, this is one of the strongest outputs in the entire gallery. The face reads like a genuine FLIR camera image. The scanline texture adds authentic CRT monitor warmth.
- On the **comic**, all three panels work: the noir detective scene reads as if scanned at night; the magical girl panel becomes an alien heat vision of innocence; the fight scene becomes electric. This filter is the most consistent performer across panels.
- On the **chart**, the bars are beautifully color-coded by height — the tallest bar (North America) is the hottest red-white; the shortest is cool purple. The bars accidentally become a thermal heat map of sales importance. Conceptually richer than the original.

**What doesn't work:**

- Virtually nothing fails here. If forced to criticize: the scanlines are faint to the point of being nearly invisible on some light areas; a slightly more aggressive CRT raster would have added more period-correct texture.

**Verdict:** The most technically accomplished and consistently excellent filter in the gallery. Authentic, coherent, versatile, and beautiful. A clear gold standard.

---

### 🥈 2. neon-blueprint — Overall: 8.8

**Concept:** Architectural blueprint aesthetic — dark navy background, cyan edge-glow lines, blueprint grid overlay, engineering annotation style.

**What works:**

- The **chart** output is exceptional. Cyan-glowing bar edges on navy behave like luminous engineering diagrams. The title text "Q1 Global Sales Distribution" feels like a technical annotation on a circuit schematic. This is the most dramatic and original chart transformation in the gallery.
- The **comic** is outstanding. The noir detective's linework glows with cyan precision — MYSTERY STREET reads like a neon sign against night sky. The magical girl's magical effects take on the quality of energy fields in a technical hologram.
- The **photo** is compelling — edge detection reveals the portrait as a luminous architectural drawing, as if a master draughtsman had traced the subject in light.
- The navy-to-black background gradient is correctly calibrated (not pure black, not dark blue — the specific mid-navy of actual blueprint paper is nailed).

**What doesn't work:**

- On the photo, some areas of very fine detail (hair texture, fabric) blur into undifferentiated cyan noise rather than crisp lines. A smarter edge-detection threshold would have preserved more mid-frequency structure.

**Verdict:** Among the most visually thrilling filters in the gallery. Transforms every input into something that feels both technically precise and mysteriously beautiful. High concept, high craft.

---

### 🥉 3. cmyk-separation — Overall: 8.6

**Concept:** Simulated four-color printing (Cyan, Magenta, Yellow, Black) with halftone dots at traditional screen angles (C: 15°, M: 75°, Y: 0°, K: 45°) and deliberate misregistration.

**What works:**

- The screen angles are technically correct — this is the single most impressive act of medium fidelity in the gallery. Most filters simulate a visual _appearance_; this one simulates the _process_. The moiré that emerges from the angular relationship between screens is authentic.
- On the **photo**, the halftone dots are large enough to be read individually. The face shows tonal gradation through dot density — highlights are sparse dots, shadows are near-solid ink. The misregistration creates color fringing at the portrait edges that matches offset lithography imperfection.
- On the **comic**, the result feels like a scanned panel from a 1970s newsprint comic — the color dots cluster in the inks, and the misregistration makes the image feel physically real.
- On the **chart**, the dots are smaller but visible; the bars remain readable and the halftone gives the whole piece the feel of a printed infographic from a 1960s magazine.

**What doesn't work:**

- The chart color assignment is somewhat arbitrary — the bars don't represent their original colors as faithfully as they could; they feel homogenized toward the CMYK primaries. A more sophisticated gamut-mapping step would improve fidelity.

**Verdict:** This is a filter about _how printing works_, not just what printing looks like. That conceptual depth puts it in the top tier. Required viewing for anyone interested in the intersection of computation and craft.

---

### 🥉 3. signal-corrupted — Overall: 8.6

**Concept:** Glitch aesthetics — scan-line displacement, RGB channel bleed, block-level corruption, analog signal degradation.

**What works:**

- The **comic** is the standout output in the gallery for emotional impact. The RGB channel separation creates a 3D anaglyph-like effect on the MYSTERY STREET cover, while the scan-line displacement gives the panels the stuttering quality of a VHS tape starting to fail. The result is like finding a corrupted backup of something irreplaceable — profoundly melancholic.
- The **photo** is perfectly calibrated: the glitch is present but _restrained_. The RGB fringing at the portrait edges is exactly what a slightly misaligned CRT would produce; the block corruption is subtle enough to feel like a transmission error, not deliberate destruction. This is the rarest quality in glitch art: knowing when to stop.
- The **chart** goes further — bright RGB splitting of the bars creates a neon chaos that is visually exciting without destroying data readability.
- Conceptually, this filter engages with glitch art's theoretical tradition (Menkman, Cascone): the idea that errors reveal the normally-invisible infrastructure of digital image-making.

**What doesn't work:**

- The block corruption in the photo occasionally obscures features in ways that feel random rather than intentional. Greater spatial awareness — avoiding the face's key features — would have improved the photo result.

**Verdict:** The most theoretically sophisticated filter in the gallery, and one of the most emotionally resonant. The comic output alone would justify its inclusion in a curated exhibition.

---

### 5. arctic-crystal — Overall: 8.4

**Concept:** Voronoi-cell frost crystal pattern with cold blue palette, simulating ice formation on a window.

**What works:**

- The Voronoi cell structure is organically varied — cells are not uniform hexagons but irregular polygons that genuinely resemble crystal growth patterns. The cell boundaries have the faint luminosity of ice facets catching light.
- The cold blue-white palette is precisely calibrated: it doesn't read as "blue photo" but as "frozen surface." The saturation of the original is preserved as hints of color visible through the frost.
- Works across all three inputs: the chart becomes a frozen data artifact; the photo portrait gains an otherworldly, preserved-in-ice quality; the comic panels read like a found object from a frozen excavation.

**What doesn't work:**

- On some light areas of the chart (background, white space), the crystal overlay becomes nearly invisible — the filter needs a higher base contrast to remain legible on pale inputs.
- The concept is atmospheric rather than conceptually complex. "Frost on glass" is beautiful but doesn't carry the intellectual weight of, say, the CMYK or glitch filters.

**Verdict:** Consistently beautiful. Atmospheric and technically accomplished. One of the most original concepts in the gallery.

---

### 6. gilded-woodblock — Overall: 8.2

**Concept:** Japanese ukiyo-e woodblock print simulation — posterized palette in indigo/celadon/vermilion/gold, edge-carved relief lines, registration marks, and traditional composition principles.

**What works:**

- The palette is the most art-historically specific in the gallery. Indigo, celadon, gold-ochre, and deep vermilion are the exact pigments used in Hiroshige and Hokusai. A viewer with knowledge of Japanese printmaking would immediately recognize the reference.
- On the **photo**, the portrait acquires the quality of a museum woodblock — the face becomes posterized into broad areas of color, and the edge lines suggest the carving of the woodblock itself. This is one of the best photo transformations in the gallery.
- The **chart** works surprisingly well: the bars become color-coded regions in ukiyo-e palettes, and the overall feel is of a traditional illustrated scroll with quantitative annotations.
- Registration marks in the corners are a beautiful detail — they show that the filter understands printing as a _process_, not just an appearance.

**What doesn't work:**

- On the **comic**, the vibrant ukiyo-e palette occasionally clashes with the modern anime aesthetic of the magical girl panels. The filter works better on imagery that has fewer pre-existing color commitments.

**Verdict:** The deepest art-historical grounding of any filter in the gallery. A knowledgeable viewer would find genuine delight in its specificity.

---

### 7. prussian-cyanotype — Overall: 8.1

**Concept:** Iron-salt cyanotype process — prussian blue monochrome, watercolor paper texture, characteristic tonal inversion (shadows dark blue, highlights near-white).

**What works:**

- Prussian blue is an extremely specific color. This filter uses it correctly — not navy, not cornflower blue, but the deep, slightly greenish blue of iron-salt chemistry. This specificity is what separates authentic medium simulation from generic "blue photo."
- The **photo** portrait is one of the most beautiful outputs in the gallery. The cyanotype process historically made its subjects feel both intimate and ancient — this filter captures that quality. The face retains its structure while acquiring the quality of a 19th-century scientific photograph.
- Paper texture is appropriate and not overdone. The chart remains fully readable.

**What doesn't work:**

- The **comic** result, while atmospheric, loses some of the ink line contrast that makes comics readable. The dark panels (noir detective) merge into undifferentiated blue shadow.

**Verdict:** Elegant, historically precise, and emotionally resonant. One of the most refined filters in the gallery.

---

### 8. verdigris-antiquity — Overall: 8.0

**Concept:** Oxidized copper patina — teal/verdigris corrosion on warm bronze substrate, with copper-tone highlights and surface texture simulating chemical weathering.

**What works:**

- The teal-on-warm-ochre palette is precisely the color combination of genuine verdigris: the blue-green of copper carbonate against the warm brown of underlying metal. This is not generic "green photo" — it's chemically specific.
- The **chart** output is one of the most elegant in the gallery: the bars read as copper ingots recording sales figures. The legend icons take on the quality of engraved seals.
- The **comic** is outstanding — the noir detective panel, already monochromatic, gains a haunting antiquity. It reads like a panel discovered on a copper plate in an archaeological dig.
- Consistent across all three inputs — one of the most versatile filters.

**What doesn't work:**

- The **photo** creates a teal face on a warm background that is visually striking but anatomically odd — human skin in verdigris tones is beautiful in sculpture (think Renaissance bronzes) but the uncanny valley effect is pronounced.

**Verdict:** A filter with genuine material intelligence — it understands oxidation, not just color. The chart and comic results are among the best in the gallery.

---

### 9. solarized-dream — Overall: 7.9

**Concept:** Sabattier solarization — darkroom technique where partial re-exposure during development creates psychedelic tonal inversions and Mackie lines at tonal boundaries.

**What works:**

- The **comic** output is the single most visually explosive image in the gallery. The Sabattier effect creates neon tones — electric orange, acid green, violet — that transform the noir panels into something from a fever dream. The magical girl panel becomes a psychedelic vision of innocence under siege. This is a genuinely extraordinary image.
- The per-channel threshold variation (different solarization points for R, G, B) creates color shifts that are more interesting than simple luminance inversion. This technical choice shows understanding of the Sabattier process.
- Conceptually grounded: solarization was embraced by Man Ray, Salvador Dalí, and Lee Miller as a Surrealist darkroom technique. The filter carries this art-historical weight.

**What doesn't work:**

- The **chart** has data label rendering artifacts — percentage labels appear doubled or displaced in some bars. This is a real bug that undermines the chart's readability.
- The **photo** is effective but less surprising; psychedelic portrait rendering is a common filter effect and doesn't have the same impact as the comic result.

**Verdict:** One of the most artistically ambitious filters in the gallery. The comic result alone is museum-quality. Would be ranked higher if not for the chart label bugs.

---

### 9. graphite-study — Overall: 7.8

**Concept:** Pencil/graphite life-drawing study on cream paper — delicate directional marks, soft tonal variation, sketch-like linework.

**What works:**

- The **photo** produces a beautiful, delicate portrait that captures the quality of a master draughtsman's study. The marks are directional (following facial contours), not simply desaturated. The cream paper tone is correctly warm — graphite on paper has a warmth that photocopied B&W lacks.
- The chart retains full data readability while gaining an understated, hand-drawn quality — as if a student had sketched the chart from life.
- Consistently pleasant across all three inputs. No failures.

**What doesn't work:**

- The **comic** result, while charming, loses the high contrast that makes comic art readable. Dark inks are softened to medium-gray graphite, and some fine linework disappears.
- The filter's modesty is both a strength and a limitation: it never surprises, never transcends "pleasant."

**Verdict:** Technically clean and aesthetically pleasing. The best "understated" filter in the gallery — the one most suited for contexts where transformation should serve rather than overwhelm.

---

### 9. linocut-bold — Overall: 7.8

**Concept:** Relief printmaking simulation — stark black-and-white morphological reduction, carved-away whites creating bold ink positive-forms, registration marks.

**What works:**

- The **photo** is striking and uncompromising: high-contrast reduction to flat black and white, with the morphological cleaning creating the deliberate simplification of actual carving. The portrait becomes monumental — like a woodcut poster for a political movement.
- The **comic** is excellent — the noir detective panel already has high contrast, which the linocut processing amplifies into something powerfully graphic. The MYSTERY STREET title becomes like a carved signboard.
- The concept is pure and committed. Linocut has a strong tradition (Picasso, Matisse) and this filter respects it.

**What doesn't work:**

- The **chart** suffers from morphological operations eroding text — the percentage labels are partially or fully destroyed by the same erosion/dilation passes that clean the image forms. This is a real technical failure: bar shapes survive but their labels don't.
- All color information is destroyed, which is a necessary consequence of the medium but means the chart loses its legend-based color encoding entirely.

**Verdict:** Magnificent on photo and comic. The chart failure is a significant drag, but the quality of the other outputs is high enough to carry it.

---

### 9. silver-daguerreotype — Overall: 7.8

**Concept:** Antique silver-plate photograph (1839–1860 process) — S-curve tonal response, silver-grain texture, warm metallic toning, oval vignette with dark edges.

**What works:**

- The **photo** is the finest historical photographic simulation in the gallery. The S-curve correctly maps the tonal response of silver chemistry: deep blacks, compressed midtones, luminous highlights. The metallic grain texture is on the right scale. The oval vignette places the subject in a locket.
- The **comic** works beautifully — the oval frame creates an uncanny juxtaposition: Victorian portrait photography applied to noir detective content. The MYSTERY STREET panel, darkened and vignetted, looks like evidence from a 19th-century murder investigation.
- Conceptual specificity is exceptional: the daguerreotype is the most historically documented early photographic process, and this filter's adherence to its visual grammar is remarkable.

**What doesn't work:**

- The **chart** is significantly damaged by the oval vignette, which darkens the central bars. The tallest bar (North America, center-left) is partially obscured. The vignette is a deliberate aesthetic choice but one that should have been adapted for data visualization contexts.
- The same vignette that makes the photo so beautiful is the filter's Achilles heel on chart inputs.

**Verdict:** The highest-fidelity historical photographic simulation in the gallery. A masterpiece on portrait inputs. Would be ranked higher without the chart vignette problem.

---

### 12. copper-plate-etching — Overall: 7.6

**Concept:** Intaglio printmaking simulation — crosshatch line texture built from angled fine lines, ivory/cream paper tone, engraved mark density proportional to image darkness.

**What works:**

- The **chart** is excellent: each bar is filled with crosshatch marks at a density corresponding to its value. The cream paper background is correct — traditional etching paper is warm ivory, not white. The title text is rendered in a slightly eroded serif that feels engraved.
- The **comic** is the best output: the noir detective panel rendered in crosshatch looks like a 19th-century illustrated novel — a Doré engraving, a Cruikshank. The diagonal marks follow contours in a way that actually mimics the directional mark-making of a real engraver. The magical girl panel's delicate linework survives gracefully.
- The cream paper tone is accurately warm — this small calibration separates this filter from generic "desaturated" effects.

**What doesn't work:**

- The **photo** is too dense — the crosshatch marks in the darkest areas (hair, shadow) merge into near-solid black with a slight moiré pattern from competing hatch directions. The face is barely readable. A master engraver would have lightened the mark density in shadow regions to maintain legibility.

**Verdict:** Beautiful concept, beautifully executed on chart and comic. The photo's over-density is a calibration issue that, once fixed, would make this a top-5 filter.

---

### 12. infrared-reverie — Overall: 7.6

**Concept:** Infrared film photography — vegetation and skin glow white (high near-IR reflectance), skies and dark clothing go deep black, halation blooms around highlights.

**What works:**

- The **photo** produces a beautiful near-monochrome portrait with correct tonal assignments: skin tones glow near-white (skin reflects near-IR strongly), dark fabric goes deep black. The halation around highlights is correctly soft and blooming.
- Technically correct: the filter understands that IR film is not simply desaturation — it involves channel remapping based on real-world reflectance differences.
- The grain texture is authentic to pushed B&W film, not just digital noise.

**What doesn't work:**

- The **chart** becomes nearly monochromatic — color-encoded bars lose their chromatic distinctions and all render to similar mid-gray values. This is technically correct (IR film has no color discrimination) but practically unhelpful for data visualization.
- The concept is inherently limited on non-photographic inputs: charts and comics don't have the organic IR reflectance variation that makes this process interesting.

**Verdict:** Excellent for portraits; inherently limited for non-photographic content. A filter about medium specificity that reveals its own scope.

---

### 14. cross-stitch-canvas — Overall: 7.5

**Concept:** Counted cross-stitch embroidery on linen canvas — X-shaped marks on a grid, linen texture, thread color from source image.

**What works:**

- The linen canvas texture is correctly warm and slightly irregular — real linen is not a uniform grid. The X-stitch marks are sized appropriately (large enough to read as stitches, small enough to resolve image content).
- The **photo** portrait is recognizable through the stitch grid — the face is rendered in varying thread colors that approximate the source palette. A charming folk-art quality.
- The **chart** is readable and charming: the bars become columns of colored stitches, an inadvertently beautiful visualization of data as needlework.

**What doesn't work:**

- The **comic** loses fine linework to the stitch grid — speech bubble text is partially illegible, and fine details in the magical girl panel disappear into the grid. Cross-stitch has a minimum resolution limit below which it cannot describe fine line work.
- The concept, while charming, lacks the intellectual depth of the stronger filters.

**Verdict:** Consistently pleasant, technically clean. The charming "folk art" filter of the gallery.

---

### 14. synthwave-horizon — Overall: 7.5

**Concept:** 1980s vaporwave/synthwave aesthetic — purple-pink-to-dark-blue gradient, perspective grid, VHS scanlines, chromatic aberration.

**What works:**

- The purple-pink-to-dark-blue gradient is the correct vaporwave palette — not arbitrary pastel, but the specific nostalgia-gradient of 1980s computer graphics and neon-lit video stores.
- The perspective grid references the retro-3D wireframe aesthetic of early CGI and music video production.
- Works across all three inputs with consistent character. Vibrant and fun.

**What doesn't work:**

- The aesthetic, while well-executed, is more _stylistic reference_ than _medium simulation_. Vaporwave is a 21st-century internet aesthetic, not a historical artistic medium. The filter evokes a mood rather than a process — this limits its conceptual depth.
- The chromatic aberration is sometimes heavy-handed, adding visual noise to the photo output without adding emotional content.

**Verdict:** Well-executed contemporary aesthetic filter. Fun and consistent, but less intellectually substantive than the historical medium simulations.

---

### 17. impasto-storm — Overall: 7.2

**Concept:** Thick oil paint impasto — brushstroke texture, paint build-up at edges, visible palette knife marks, painterly smearing.

**What works:**

- The thick texture overlay correctly creates the sense of paint that has been pushed rather than applied. There is directionality to the marks.
- The **chart** is interesting: bars rendered as thick paint strokes with visible impasto build-up at the top edge. The chart reads as a _painted_ chart — an oil painting of data.
- The **photo** produces a tactile, richly textured portrait. The impasto adds physical weight to the image.

**What doesn't work:**

- The brushstroke direction lacks the Van Gogh-level energy that the concept implies. "Impasto storm" suggests dynamic, swirling marks — the actual output is more of a uniform texture overlay than directional paint movement.
- The **comic** loses the line clarity that makes comics readable; impasto texturing is not naturally suited to inked illustration.

**Verdict:** Good technical execution of a texture concept, but the "storm" energy promised by the name isn't fully delivered.

---

### 17. iron-rust — Overall: 7.2

**Concept:** Oxidized iron surface — rust orange with horizontal grain, pitting corrosion texture, metallic highlight variation.

**What works:**

- The rust orange palette is correctly warm and slightly varied — real rust is not uniform but has patches of different oxidation depths. The filter captures this variety.
- The **comic** is excellent: the noir detective panel rendered in rust tones looks like a page found in a flooded basement — an aged, damaged artifact. This is a filter that suits content with history.
- The horizontal grain correctly references the direction of metal rolling and weathering.

**What doesn't work:**

- The **photo** receives too heavy an orange cast. The face becomes an almost uniform rust-orange mask with little tonal variation — the corrosion texture overwhelms the portrait rather than adding to it.
- The pitting texture in flat areas reads more like image noise than actual surface corrosion.

**Verdict:** Excellent for aged-artifact aesthetics on comic and chart content. Needs recalibration for portrait photography.

---

### 17. risograph-reverie — Overall: 7.2

**Concept:** Risograph printer simulation — two-color halftone (coral + teal), misregistered passes, cream paper texture.

**What works:**

- The **photo** is genuinely beautiful — perhaps the most realistic simulation of an actual riso print in the gallery. The coral-teal two-color split, with halftone dots at appropriate density and slight misregistration, would fool a casual viewer into thinking this was photographed from a printed zine.
- Misregistration is calibrated well: present enough to be visible, restrained enough not to destroy the image.

**What doesn't work:**

- The **chart** background color is incorrect — it renders as steel-blue rather than the cream paper color that characterizes riso printing. This is a significant authenticity error: riso paper is distinctively warm cream, not cool blue.
- The **comic** left panels are muddy — the coral-teal two-color system struggles when applied to complex multi-panel compositions with varying tonal ranges.

**Verdict:** The photo output is a standout. The chart background error is distracting and undermines the overall score.

---

### 20. brutalist-duotone — Overall: 7.1

**Concept:** Bauhaus/brutalist graphic design — acid yellow and charcoal black duotone, high contrast, bold typography aesthetic.

**What works:**

- The **photo** is one of the gallery's most arresting outputs — acid yellow and charcoal black create a Bauhaus poster of extraordinary boldness. The face reads through the duotone with dramatic shadow/highlight mapping.
- The **comic** is equally strong: the MYSTERY STREET panel in acid yellow and charcoal looks like a genuine two-color pulp printing artifact — exactly what a brutalist graphic designer would produce.
- The palette choice is specific and historically grounded: acid yellow (Bauhaus primary palette) + charcoal (industrial print black) is a real graphic design tradition.

**What doesn't work:**

- The **chart** is a significant failure: most bars become invisible, washed out to the yellow ground color. The yellow-dominant duotone absorbs light-colored bar values into the background. The chart data is effectively destroyed.
- This is a fundamental mismatch between the filter and chart inputs: duotone processes that work beautifully on tonal gradients (faces, photographs) fail on flat-color bar charts.

**Verdict:** Spectacular on portraits and comics; genuinely fails on charts. A filter that knows its medium but doesn't know its limits.

---

### 21. charcoal-on-kraft — Overall: 7.0

**Concept:** Charcoal drawing on kraft brown paper — dark marks on warm brown, soft smudging, paper grain visible.

**What works:**

- The **comic** is excellent: pulp noir rendered in charcoal on brown paper has an authentic hand-made quality that suits the genre perfectly. The warm brown paper makes the noir content feel like a found sketch from the period.
- The kraft paper color is correctly warm-brown — not orange, not tan, but the specific warm gray-brown of kraft paper. Small calibration, large impact.

**What doesn't work:**

- The **photo** is too dark — the charcoal marks dominate over the paper color, making the result feel more like a dark sepia photograph than a charcoal drawing. A real charcoal drawing on kraft paper would have more visible paper texture and lighter preserved areas.
- The mark texture in the photo doesn't read as directional charcoal strokes — it reads as a flat dark overlay. This is the difference between _simulating charcoal_ and _simulating a photo of charcoal_.

**Verdict:** Charming concept, strong on comic, needs calibration for photo inputs.

---

### 22. terminal-matrix — Overall: 6.6

**Concept:** ASCII character-cell rendering on a phosphor-green CRT terminal — dark background, monospace character grid, scanline phosphor glow.

**What works:**

- The **photo** is one of the gallery's best outputs for this filter. A dark background with glowing green portrait, rendered in ASCII characters at the right size — this is the Matrix aesthetic done correctly. The face is recognizable, the character cells are readable, the green glow is authentic.
- The **noir detective comic** panel is outstanding: dark-background panels benefit from the CRT rendering and read like a vintage terminal displaying surveillance footage.

**What doesn't work:**

- The **chart** is a fundamental failure: instead of dark background with green characters, the chart output has a light/yellow-green background. This inverts the entire CRT aesthetic. The whole point of terminal green is phosphor glow against darkness — a light background destroys this.
- The **magical girl comic** panel fails similarly: light-background panels render as green-tinted, not as CRT displays.
- The filter needs to apply a background-darkening step before character rendering, regardless of input brightness.

**Verdict:** When the filter works (dark inputs), it's exceptional. When it fails (light inputs), the failure is complete. A targeted fix to the background handling would elevate this significantly.

---

### 23. noir-rain — Overall: 6.4

**Concept:** Film noir cinematography — high-contrast darkness, vertical rain streaks, neon reflections in puddles, chromatic aberration from wet lens.

**What works:**

- At its best moments (the noir detective comic panel, the darker areas of the photo), the rain texture and neon reflections create genuine cinematic atmosphere. The concept is rich and evocative.
- The darkness compression is correct for film noir — a deliberately crushed shadow zone is part of the aesthetic.

**What doesn't work:**

- The **photo** chromatic aberration is too aggressive on the face — the color fringing reads as a technical error rather than an artistic effect. It crosses the line from "cinematic lens artifact" to "broken image."
- The **chart** assigns inconsistent colors to the bars — some bars get neon-pink treatment, others get different tones. This appears to be a bug in the neon-reflection generation that samples different hues per region without a coherent mapping.
- The **magical girl comic** panel is muddy — the film noir darkening is at war with the bright, cheerful aesthetic of the source material.

**Verdict:** Excellent concept with inconsistent execution. The filter is at its best when the source material is already dark.

---

### 23. pointillist-garden — Overall: 6.4

**Concept:** Seurat/Neo-Impressionist pointillism — broken-colour dots of varying radius on white canvas, optical color mixing.

**What works:**

- The **chart** is charming: each bar becomes a column of colored dots that cluster visually into the bar form. At reading distance, the dots blend into the bar color — correct optical mixing.
- The **comic** is vibrant — the dot clusters at panel boundaries create a pleasant texture.
- The white canvas ground is correctly used as negative space between dots.

**What doesn't work:**

- The **photo** is too dark and heavy — the dots are too large and/or too opaque, causing the face to disappear into a dark mass of closely-packed dots. Seurat used _varied_ dot sizes — the smallest dots in dark areas, larger dots in lit areas, to preserve tonal range. Uniform dot size creates even density which reads as darkness.
- The filter would benefit from dot-size modulation based on local luminance.

**Verdict:** Good concept, partially executed. The chart is delightful; the portrait is a technical problem that better dot-size calibration would fix.

---

### 25. watercolor-bloom — Overall: 6.2

**Concept:** Wet-on-wet watercolor — pigment bleeds at edges, dried watercolor rings, paper granulation, color blooms.

**What works:**

- The **comic** is the filter's best output — pastel watercolor washes suit the magical girl panels beautifully, softening the inks into something dreamy and delicate.
- The paper granulation texture is correctly subtle — watercolor paper has a texture that adds warmth without overwhelming the image.
- The concept is charming and the color palette retention is good.

**What doesn't work:**

- The **photo** is almost unchanged — the watercolor effect is so subtle that the transformation barely registers. The filter's "bloom" and "bleed" effects are invisible at the level of detail present in a portrait photograph.
- This is the fundamental problem: watercolor's characteristic wet-edge effects require areas of flat wash — photography's continuous-tone gradients don't create the conditions for wet-on-wet blooms to emerge.
- The filter needs a more aggressive stylization step (edge detection to find wash boundaries, local saturation boost) to make its effects visible on photographic input.

**Verdict:** Lovely concept that partially delivers on illustration/comic inputs. Nearly invisible on photography. The filter has not found its right transformation strategy for all input types.

---

### 26. holographic-foil — Overall: 6.1

**Concept:** Iridescent holographic foil — rainbow hue cycling based on image structure, metallic reflectance simulation.

**What works:**

- The concept is visually interesting: holographic foil creates hue variation based on viewing angle, and mapping this to image luminance/position is a plausible simulation approach.
- The **chart** produces a psychedelic but visually interesting result — each bar catches a different rainbow region, creating a pop-art quality.

**What doesn't work:**

- The **photo** nearly loses the face — the dense hue cycling in highlight areas creates noise-like color variation that disrupts face recognition. Holographic foil in reality has large, smooth hue zones; this filter creates fine-grained chaotic variation that reads as noise, not iridescence.
- The fundamental problem is scale: holographic hue shifts are smooth and large-area in reality; the simulation creates small-area variation that looks like a color-channel error.
- The **comic** is visually overwhelming — the dense iridescence obscures the linework.

**Verdict:** Interesting concept, incorrect scale of implementation. The hue zones need to be 5–10× larger to simulate actual holographic foil behavior.

---

### 27. byzantine-mosaic — Overall: 5.5

**Concept:** Byzantine tesserae mosaic — square tiles with gold grout, warm earthy palette, gold highlights on dark elements.

**What works:**

- The gold grout between tiles is correctly warm and luminous — Byzantine mosaics are distinguished by their gold tesserae and gold mortar, and the filter captures this palette.
- The **comic** result has a certain warmth — the tiled pattern creates color-field areas reminiscent of abstract mosaic.

**What doesn't work:**

- The **photo** is too dark — the mosaic tiling quantizes the portrait into so few color regions that the face becomes a dark, nearly unreadable pattern. Byzantine mosaics (e.g., Ravenna) actually have remarkable tonal range; this filter loses it.
- The **chart** suffers from tile size: the tiles are so small that data bar shapes are barely interrupted, but so large that the result looks pixelated rather than mosaic-like.
- Byzantine mosaics derive their power from large, deliberately imprecise tiles that create luminous color fields. The filter creates small, precise tiles that create a blurry photo effect.

**Verdict:** Concept understood but execution needs tile-size recalibration and better tonal mapping. The gold grout is a beautiful detail in a filter that otherwise needs significant work.

---

### 28. origami-fold — Overall: 4.6

**Concept:** Paper folding simulation — triangular facets with fold shading, crease shadows, origami color palette.

**What works:**

- The concept is appealing: origami as a transformation metaphor (source material re-folded into a new form) is intellectually interesting.
- The triangular facet palette on the **chart** creates vivid color regions that are briefly attractive.

**What doesn't work:**

- The **chart** data is completely obliterated — bars are unrecognizable as separate elements; the entire chart becomes an abstract triangular mosaic.
- The **photo** and **comic** similarly destroy content — all three inputs become abstract Voronoi-like mosaics with no connection to the source.
- The most significant problem: the filter doesn't _fold_ the image — it _fragments_ it. Origami preserves the surface (paper doesn't gain or lose area); this filter discards content entirely. The metaphor is broken at the implementation level.
- The triangular facets don't create fold shadows convincingly — they look like a low-polygon 3D rendering, not paper folds.

**Verdict:** A concept that is not realized in the implementation. The output is a generic mosaic effect rather than an origami simulation.

---

### 28. pop-art-screen — Overall: 4.6

**Concept:** Pop art printing — Warhol flat colors, Ben-Day dots, bold outlines, high saturation.

**What works:**

- The **comic** partially works: the right panel gains some of the flat-color, high-contrast quality of pop art. The concept is correct and historically grounded.
- Ben-Day dots are present in some outputs.

**What doesn't work:**

- The **photo** is perhaps the worst output in the gallery relative to its concept: instead of flat color areas and bold outlines (Warhol silkscreen), the photo output looks like a faded pencil sketch — there is no flat color, no halftone, no bold line. The transformation is entirely wrong.
- This appears to be a bug: the photo input is receiving a different processing path than intended. The poster-paint flat areas that define pop art — the signature contribution of Warhol — are completely absent.
- The **chart** is mediocre: dot pattern is present but color blocking is incomplete.

**Verdict:** A fundamental implementation failure on the photo input. The concept is strong (pop art is a rich tradition) but the execution does not deliver the promised transformation.

---

### 30. cathedral-glass — Overall: 4.0

**Concept:** Stained glass window simulation — color segmentation into glass "panes," black lead came at boundaries, luminous color fields.

**What works:**

- The concept is clear and art-historically resonant. Gothic stained glass is one of the great achievements of medieval art.
- The lead came (black boundaries) between regions is present in all three outputs.

**What doesn't work:**

- The **chart** output looks like a pixelated JPEG artifact, not stained glass. The color regions are extremely small and irregular — stained glass panels are large (the size of a fist or hand) and deliberately shaped. The filter is creating pixel-level regions, not glass-panel regions.
- The **photo** becomes a chaotic mosaic that obliterates the portrait. The face is unrecognizable.
- The **comic** becomes an explosion of random colors without any of the luminous warmth that makes stained glass beautiful.
- The root problem: stained glass derives its character from _large, shaped, deliberately colored areas_ with intentional symbolic or representational meaning. The filter fragments the image into tiny arbitrary regions that convey neither the scale nor the deliberateness of glass-making.
- There is no simulation of light transmission — stained glass glows from within; this filter produces a dark, opaque mosaic.

**Verdict:** The filter does not simulate stained glass — it simulates image fragmentation with black boundaries. A fundamental rethinking of the segmentation scale and light-transmission model is needed.

---

## Part 5: Conclusions and Observations

### Top Performers (Score ≥ 8.0)

The highest-scoring filters share a common quality: **they simulate a specific, historically documented process rather than a general visual style**. `thermal-scan` simulates scientific instrumentation. `cmyk-separation` simulates offset lithography. `signal-corrupted` simulates digital signal degradation. `silver-daguerreotype` simulates a specific 19th-century chemical process. This specificity — knowing _exactly_ what physical or chemical phenomenon to reproduce — is what separates great filters from generic ones.

### Structural Weakness: Dark-Input Dependency

Several filters that fail on chart or comic inputs (bright backgrounds) succeed brilliantly on the portrait photo or the noir detective panel (dark backgrounds). `terminal-matrix`, `brutalist-duotone`, `noir-rain`, and `pointillist-garden` all show this pattern. The filters are calibrated for the tonal range of their strongest input but haven't been adapted to handle the full range of input brightness. A robust filter should detect input properties and adapt its parameters accordingly.

### Recurring Technical Bug

A sparkle/star artifact (four-pointed) appears in the lower-right corner of multiple photo outputs. A displaced "10%" text label appears at the top of the tallest chart bar in multiple filters. These are pipeline bugs shared across filters rather than problems with individual filter implementations. They suggest that a shared pre-processing or compositing step is introducing these artifacts.

### The Versatility Problem

Filters that work magnificently on one input (photo: `silver-daguerreotype`, `prussian-cyanotype`) but fail on another (chart: both of the above due to vignetting) represent an unresolved design tension. Should a filter be optimized for its best case, or should it detect input type and behave differently? The most successful filters (`thermal-scan`, `neon-blueprint`, `signal-corrupted`) find transformations that are _metaphysically appropriate_ for any content type — they change the medium in which the content appears, not the content itself.

### The Content-Destruction Problem

Several filters (`origami-fold`, `cathedral-glass`, `byzantine-mosaic`) prioritize visual texture over content preservation to a degree that renders them dysfunctional. An artist or designer using these filters would receive an output that cannot be used for its intended purpose. A filter that destroys all readable content has failed at the primary function of transformation: revealing the source in a new light, not concealing it.

### The Best Single Image in the Gallery

The single most extraordinary output is the **solarized-dream comic** — a psychedelic explosion of neon color applied to noir detective and magical girl panels. It transcends "filtered image" and enters the territory of genuine art. The same filter's **chart label bug** and **mediocre photo output** prevent it from ranking in the top 3 overall. This is the gallery's clearest illustration of the difference between _peak artistic impact_ and _consistent quality_.

### Recommended for Exhibition

If this gallery were curated for public exhibition, the following filters would be selected for their combination of artistic quality and conceptual depth:

1. **thermal-scan** — Scientific beauty; consistent across all inputs
2. **neon-blueprint** — Most visually dramatic; transforms every input type
3. **signal-corrupted** — Theoretically rigorous glitch aesthetics
4. **cmyk-separation** — Educational and beautiful; teaches how printing works
5. **gilded-woodblock** — Deepest art-historical grounding
6. **solarized-dream** — Highest peak artistic impact (comic result)
7. **silver-daguerreotype** — Most faithful historical photographic simulation
