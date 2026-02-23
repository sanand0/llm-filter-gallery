# GPT Filter Evaluation

## Scope

This judges **30 filters** at the **filter level** (not single-image wins), using each filter's `photo`, `comic`, and `chart` outputs.

## Transparent, Reproducible Process

### 1) Build the evaluation set

- Enumerated all filter specs from `filters/*.md` (**30 filters**).
- Verified each filter had exactly three outputs in `output/`: `photo-<filter>.webp`, `comic-<filter>.webp`, and `chart-<filter>.webp` (**90 evaluated images**, 0 missing).
- Grouped evidence by filter (not by image) so each score reflects cross-input behavior.

### 2) Derive criteria from researched foundations

- Reviewed established references on: Gestalt perception, visual hierarchy, color theory/contrast, non-photorealistic rendering, graphical perception (Cleveland-McGill), and perceptual image quality framing (SSIM/IQA).
- Mapped those foundations into a practical 7-part expert rubric:
  1. Concept coherence
  2. Visual impact
  3. Color & tonal mastery
  4. Structure legibility
  5. Texture/material quality
  6. Cross-input robustness
  7. Artifact control
- Applied fixed weights (15/20/15/15/10/15/10) to emphasize both artistic strength and practical readability.

### 3) Evaluate each filter with a fixed protocol

- For every filter, reviewed **photo + comic + chart together** before assigning scores.
- Scored each criterion on a **1-10 scale** (decimals allowed), then produced an overall weighted score.
- Recorded filter-level strengths and weaknesses with concrete visual evidence (e.g., hierarchy retention, chart text loss, haloing, clipping, moire, banding).
- Added a short judge rationale to explain why the score was deserved, including where the filter excels and where it collapses.

### 4) Decide "really good" filters

- Defined "really good" as the top tier by weighted score with strong concept integrity and cross-input performance.
- Included filters that remain compelling beyond one hero image and still preserve enough structure on difficult inputs.

### 5) Reproducibility notes

- Inputs and outputs are fully local and versioned by file name; no hidden sampling was used.
- The same rubric, weight vector, and per-filter 3-image protocol can be rerun to reproduce rankings and rationale structure.
- Reproducibility target is **method-level consistency** (same criteria, same evidence, same weighting), while close scores may shift slightly with different judges.

## Expert Criteria (What Beginners Often Miss)

The rubric combines visual-art criticism with perception/data-viz research (Gestalt grouping and figure-ground, visual hierarchy, Bertin visual variables, Cleveland-McGill graphical perception, and perceptual quality work such as SSIM).

| Criterion                | Weight | What an expert checks                                                      |
| ------------------------ | -----: | -------------------------------------------------------------------------- |
| Concept coherence        |    15% | Consistency of style language across all outputs, not just one hero image. |
| Visual impact            |    20% | Whether focal hierarchy and emotional pull survive stylization.            |
| Color & tonal mastery    |    15% | Control of value range, harmony, and highlight/shadow behavior.            |
| Structure legibility     |    15% | Preservation of shape, figure-ground clarity, and chart readability.       |
| Texture/material quality |    10% | Believability of simulated medium (etch, ink, stitch, patina, etc.).       |
| Cross-input robustness   |    15% | How well the same filter performs on photo + comic + chart.                |
| Artifact control         |    10% | Suppression of halos, banding, clipping, moire, and aliasing distractions. |

### Signals experts look for (that beginners miss)

- Whether stylization preserves **hierarchy** (main subject vs. background), not just whether it looks cool at first glance.
- Whether the filter's texture is **materially plausible** (e.g., true print/ink behavior) vs. generic noise overlay.
- Whether color remapping keeps **semantic clarity** for charts/labels and doesn't destroy data reading.
- Whether high drama comes from intentional tonal design rather than accidental clipping/posterization.
- Whether the filter is robust across very different inputs or only flattering to one category.

## Filters That Are Really Good

These are the strongest exhibition-level entries by weighted score and cross-input performance:

- **terminal-matrix** (78.85/100): Very consistent concept: every variant convincingly reads as monochrome phosphor-green ASCII/character-cell rendering on black CRT.
- **thermal-scan** (78.25/100): Consistent false-color palette (deep purples -> hot yellows) that convincingly reads as thermal across all three variants.
- **neon-blueprint** (78.05/100): Clear and consistent concept: the cyan-on-deep-navy palette and glowing contour lines successfully evoke a technical schematic and circuit-board aesthetic across all three variants.
- **risograph-reverie** (77.65/100): Consistent two-colour risograph look across all three outputs - coral and teal are well chosen and evoke authentic misregistration.
- **verdigris-antiquity** (76.60/100): Clear and consistent verdigris copper concept across all three variants - the teal-green patina and warm brown base read immediately as oxidized metal.
- **linocut-bold** (76.25/100): Very clear black-on-off-white linocut aesthetic across all variants - strong figure/ground separation and high-contrast silhouettes.
- **graphite-study** (76.02/100): Consistent pencil-on-cream paper palette across all three variants; warm paper tone and desaturated graphite lines communicate the intended aesthetic strongly.

## Scoring Table

| Rank | Filter               | Overall | Verdict   | Concept | Impact | Color/Tone | Structure | Texture | Robustness | Artifacts |
| ---: | -------------------- | ------: | --------- | ------: | -----: | ---------: | --------: | ------: | ---------: | --------: |
|    1 | terminal-matrix      |   78.85 | Strong    |     9.0 |    8.0 |        8.5 |       7.0 |     7.5 |        7.0 |       7.0 |
|    2 | thermal-scan         |   78.25 | Strong    |     9.0 |    8.5 |        8.0 |       7.0 |     7.5 |        7.0 |       6.5 |
|    3 | neon-blueprint       |   78.05 | Strong    |     8.5 |    8.0 |        8.0 |       7.0 |     7.0 |        7.5 |       6.5 |
|    4 | risograph-reverie    |   77.65 | Strong    |     9.0 |    8.5 |        8.0 |       6.5 |     8.5 |        6.0 |       6.5 |
|    5 | verdigris-antiquity  |   76.60 | Strong    |     8.2 |    8.5 |        8.0 |       7.1 |     8.6 |        6.8 |       6.4 |
|    6 | linocut-bold         |   76.25 | Strong    |     8.5 |    8.0 |        8.0 |       7.0 |     8.5 |        6.5 |       6.0 |
|    7 | graphite-study       |   76.02 | Strong    |     8.5 |    7.2 |        8.0 |       7.0 |     8.6 |        6.8 |       6.5 |
|    8 | prussian-cyanotype   |   75.25 | Strong    |     8.0 |    8.5 |        8.0 |       7.0 |     7.5 |        6.0 |       6.5 |
|    9 | copper-plate-etching |   75.18 | Strong    |     8.5 |    7.5 |        8.0 |       6.2 |     8.8 |        6.0 |       6.5 |
|   10 | cross-stitch-canvas  |   74.95 | Strong    |     8.5 |    7.2 |        7.0 |       6.8 |     8.0 |        7.0 |       6.5 |
|   11 | silver-daguerreotype |   74.25 | Strong    |     8.5 |    8.0 |        8.0 |       6.5 |     7.5 |        6.0 |       6.0 |
|   12 | infrared-reverie     |   73.75 | Strong    |     8.0 |    8.5 |        7.5 |       6.5 |     6.0 |        6.0 |       6.5 |
|   13 | watercolor-bloom     |   73.50 | Strong    |     8.5 |    8.0 |        7.5 |       6.5 |     7.8 |        6.2 |       6.0 |
|   14 | origami-fold         |   73.16 | Strong    |     8.2 |    7.6 |        7.4 |       6.3 |     8.0 |        6.7 |       6.8 |
|   15 | impasto-storm        |   73.13 | Strong    |     8.0 |    8.6 |        7.8 |       6.2 |     8.4 |        6.0 |       6.5 |
|   16 | gilded-woodblock     |   73.00 | Strong    |     8.0 |    8.5 |        7.0 |       6.5 |     8.0 |        6.0 |       5.5 |
|   17 | arctic-crystal       |   72.85 | Strong    |     8.5 |    8.0 |        8.0 |       6.0 |     7.5 |        6.0 |       6.5 |
|   18 | byzantine-mosaic     |   72.65 | Strong    |     8.5 |    7.8 |        7.0 |       6.2 |     8.0 |        6.0 |       6.5 |
|   19 | signal-corrupted     |   72.25 | Strong    |     9.0 |    8.0 |        7.0 |       5.5 |     7.0 |        6.0 |       6.0 |
|   20 | brutalist-duotone    |   72.15 | Strong    |     8.5 |    8.0 |        7.0 |       6.5 |     6.0 |        6.0 |       5.5 |
|   21 | cmyk-separation      |   72.05 | Strong    |     9.0 |    8.0 |        7.5 |       6.5 |     7.0 |        6.0 |       6.5 |
|   22 | synthwave-horizon    |   71.64 | Strong    |     8.5 |    8.0 |        8.2 |       6.6 |     7.0 |        6.0 |       6.8 |
|   23 | cathedral-glass      |   71.21 | Strong    |     8.2 |    8.5 |        7.3 |       6.2 |     7.0 |        6.0 |       5.8 |
|   24 | pop-art-screen       |   70.95 | Strong    |     8.0 |    7.5 |        6.8 |       7.0 |     7.2 |        6.0 |       6.5 |
|   25 | charcoal-on-kraft    |   70.05 | Strong    |     8.0 |    7.5 |        7.0 |       6.0 |     8.0 |        6.0 |       6.5 |
|   26 | iron-rust            |   68.35 | Promising |     8.0 |    7.5 |        7.0 |       5.5 |     8.2 |        6.0 |       5.0 |
|   27 | noir-rain            |   68.05 | Strong    |     8.0 |    7.5 |        7.0 |       6.0 |     6.5 |        6.0 |       5.5 |
|   28 | holographic-foil     |   65.25 | Promising |     7.5 |    8.0 |        7.0 |       6.0 |     6.5 |        5.5 |       5.0 |
|   29 | solarized-dream      |   64.25 | Promising |     8.0 |    8.5 |        6.5 |       5.5 |     6.0 |        5.0 |       5.0 |
|   30 | pointillist-garden   |   62.25 | Promising |     7.0 |    7.5 |        6.5 |       5.5 |     7.0 |        5.0 |       4.5 |

## Per-Filter Feedback (Judge Notes)

### 1. terminal-matrix - 78.85/100 (Strong)

**What's good**

- Very consistent concept: every variant convincingly reads as monochrome phosphor-green ASCII/character-cell rendering on black CRT.
- High visual presence: strong silhouette and glow-like green highlights give a moody, retro-computing aesthetic.
- Color and tonal control are well handled: limited palette maintains contrast between bright glyphs and deep black background.
- Texture effect is believable: grid cells, cross-hatching and vertical scanlines convincingly emulate character-cell and CRT artifacts.

**What's not good**

- Legibility drops in dense-detail inputs (comic variant): fine line art and small text collapse into noisy patches, reducing narrative clarity.
- Chart variant over-simplifies numeric/text information - axis labels and small annotations become hard to read at this cell size.
- Some aliasing and periodic banding of vertical scanlines produce distracting patterns in shadow areas, slightly reducing perceived fidelity.
- Cross-input robustness uneven: photo portrait maintains subject recognition, but graphic/comic details sometimes lose hierarchies between figure and ground.

**Judge rationale:** Terminal-matrix is an effective, narrowly focused aesthetic that sells the phosphor CRT metaphor across all three inputs. It excels in atmosphere and tonal restraint, but the cell/grid resolution chosen trades away small-detail legibility in structured graphics and comics. With adaptive cell-sizing or selective anti-aliasing for fine text, this filter would move from strong to excellent in cross-input utility.

### 2. thermal-scan - 78.25/100 (Strong)

**What's good**

- Consistent false-color palette (deep purples -> hot yellows) that convincingly reads as thermal across all three variants.
- High visual drama on photographic and comic inputs: warm highlights create strong figure-ground separation and focal emphasis (especially faces and hero figures).
- The filter preserves expressive non-photoreal line work in the comic variant while adding believable emissive highlights that boost mood.
- Subtle scanning lines and vignetting enhance the sensor-readout aesthetic and give a coherent material texture.

**What's not good**

- Chart variant loses some data legibility: original bar color distinctions and small legend text are muted and reduced contrast makes numeric labels harder to read.
- Artifacts: banding and haloing around high-contrast edges (notably hair and comic black inks) occasionally look clipped rather than smoothly thermal.
- Color mapping sometimes overrides semantic color in the comic panel (e.g., yellow areas become mid-tone orange/purple shifts) which can obscure intended iconography.
- Cross-input balance: while strong on portrait and stylized comic art, the filter is less suitable for information graphics where precise color/value differences must remain unambiguous.

**Judge rationale:** Thermal-scan succeeds as a persuasive false-color treatment, providing cinematic emphasis and a clear central focal read on pictorial inputs. Its expressive texture and vignetting sell the sensor readout concept, but the aggressive remapping reduces functional legibility for charts and introduces occasional banding around high-contrast edges. For exhibition use, it is excellent as an atmospheric visual effect but should be tuned or optionally softened when applied to data-critical graphics.

### 3. neon-blueprint - 78.05/100 (Strong)

**What's good**

- Clear and consistent concept: the cyan-on-deep-navy palette and glowing contour lines successfully evoke a technical schematic and circuit-board aesthetic across all three variants.
- High visual presence: the neon outlines create strong figure-ground separation and memorable silhouettes, especially in the photo and comic variants.
- Expressive line work: the filter produces convincing engraved/plotter-like hatch marks and contour strokes that give the outputs a crafted, non-photoreal technical feel.
- Good tonal hierarchy in the chart: the bar shapes, gridlines and labels remain distinguishable and preserve the data-oriented look expected from a schematic plot.

**What's not good**

- Over-etching on faces: the photo variant's face detailing becomes visually noisy in midtones, reducing natural facial modeling and creating slightly uncanny banding.
- Comic panel inconsistencies: while line clarity is strong, the uniform glow sometimes flattens panel depth and obscures small internal lettering or texture in dense areas.
- Residual artifacts: halos and localized glow bleed (notably around thin type and fine hatch) reduce crispness and can impair readability at small sizes.
- Occasional structure loss: very dark regions collapse into near-black with only faint cyan speckling, which undermines legibility of fine background elements in some inputs.

**Judge rationale:** neon-blueprint is a well-realized stylistic filter that convincingly translates imagery into a circuit-board schematic language with a compelling neon aesthetic. It handles graphic and chart content reliably, but photographic subjects suffer from over-etching and glow bleed that erode subtle form. With tighter artifact control and reduced midtone stroking this filter would move from strong to excellent in cross-input consistency.

### 4. risograph-reverie - 77.65/100 (Strong)

**What's good**

- Consistent two-colour risograph look across all three outputs - coral and teal are well chosen and evoke authentic misregistration.
- Halftone dot patterning convincingly simulates letterpress/risograph texture with pleasing tactile quality and believable paper cream base.
- High visual character: the misregistration adds a lively, analog feel and strong emotional/artistic presence, especially in the photo and comic variants.
- Good tonal separation in pictorial inputs: the photo retains face modeling and the comic retains panel borders and illustrative contrast.

**What's not good**

- Chart variant suffers legibility loss - axis labels and smaller numeric text are poorly preserved by the heavy dot pattern and channel offset.
- Misregistration, while expressive, creates ghosting on small-scale details (thin text, fine lines) causing reading difficulty.
- Cross-input consistency drops for information-dense graphics: the same parameters that flatter photographs hamper data fidelity.
- Some haloing and localized clustering of dots near high-contrast edges produces distracting micro-artifacts in areas that require crispness.

**Judge rationale:** This filter delivers a convincing risograph aesthetic with delightful tactile halftone and color interplay; its strengths are greatest on portrait and illustrative inputs where texture and misregistration contribute character. However, the design decisions reduce functional legibility for data-rich images - small type and precise chart geometry lose fidelity. For exhibition display, pair this filter with pieces where expressive surface and mood are priorities, and avoid using it for documents that require exact readability.

### 5. verdigris-antiquity - 76.60/100 (Strong)

**What's good**

- Clear and consistent verdigris copper concept across all three variants - the teal-green patina and warm brown base read immediately as oxidized metal.
- High aesthetic punch in photo and comic: dramatic highlights on faces and linework create attractive figure-ground separation and mood.
- Texture rendering is multi-scale and believable: fine grain, larger corrosion blotches, and metallic sheen are present and varied.
- Comic variant preserves ink lines and panel structure well, integrating patina without losing stylistic intent.

**What's not good**

- Chart variant loses some numeric legibility - subtle paper texture and low contrast make small labels and thin gridlines hard to read.
- Photo variant sometimes maps the patina too aggressively onto skin highlights, flattening subtle facial modeling in places.
- Artifact control shows occasional banding and posterization in midtones, especially in uniform areas like background walls and chart fills.
- Cross-input consistency uneven: filter excels on highly textured or inked images but compromises informational clarity on data graphics.

**Judge rationale:** Verdigris-antiquity convincingly sells an oxidized-copper aesthetic with rich multi-scale corrosion and metallic highlights; it is especially effective on portraits and illustrated linework where the patina adds mood without destroying structure. However, its tonal compression and textured overlays can impede legibility in data-driven assets - a lighter, lower-frequency treatment or adaptive contrast for thin strokes and small type would improve cross-input robustness.

### 6. linocut-bold - 76.25/100 (Strong)

**What's good**

- Very clear black-on-off-white linocut aesthetic across all variants - strong figure/ground separation and high-contrast silhouettes.
- Photo variant preserves portraital form and facial features with expressive, clean cut edges suited to relief printing.
- Comic variant translates panels and line art into bold, authentic woodcut/linocut motifs; lettering and halftone feel consistent with the concept.
- Paper grain and slight mottling add believable tactile materiality, reinforcing the relief-print illusion.

**What's not good**

- Chart variant loses some numeric and label legibility: small type and legend are clipped or roughened by the heavy binarization.
- Over-thick blocking in shadowed areas (especially in the portrait) removes midtone detail that would aid subtle modeling.
- Artifacts around fine shapes (thin text, small icons, and some comic details) show occasional haloing and jagged clipping.
- Cross-input consistency dips when rendering tiny typographic elements and chart bars - the filter favors bold shapes at the expense of fine information.

**Judge rationale:** Linocut-bold convincingly delivers a stark relief-print mood and tactile paper texture; it reads immediately as an intentional black-ink linocut. The filter excels on high-contrast photographic and comic inputs, but it is less forgiving for information-dense graphics: small text, legends, and fine chart details are frequently destroyed by aggressive binarization. For exhibition use, this is a strong stylistic tool best applied where pictorial boldness is the goal rather than precise data legibility.

### 7. graphite-study - 76.02/100 (Strong)

**What's good**

- Consistent pencil-on-cream paper palette across all three variants; warm paper tone and desaturated graphite lines communicate the intended aesthetic strongly.
- Variable crosshatching is expressive and well-tuned in organic regions (portrait hair, detective coat) giving convincing volumetric shading.
- Texture simulation is high quality: believable paper grain and pencil mark variety (fine strokes, dense hatching) increase tactile presence.
- Comic panel linework remains crisp and decorative borders are preserved, supporting the stylized intent for that variant.

**What's not good**

- Chart variant loses some data legibility due to heavy hatch patterns overlaying numeric labels and thin gridlines, making precise reading harder.
- Photo variant shows occasional over-crosshatching in midtones (face and background) which flattens some facial detail and reduces subtle contrast.
- Comic variant presents tiled or pixel-like artifacts in flat-tone regions (background blocks) that distract from hand-drawn illusion.
- Artifact control inconsistent: moire-like repeating patterns appear in low-detail areas, and halation around thin type reduces crispness.

**Judge rationale:** Graphite-study succeeds as a convincingly tactile pencil-sketch filter: paper tone, stroke variety, and crosshatch directionality read as an intentional studio process. It is most successful on subjects with clear organic form (portrait, illustrated comics) but shows limitations on dense information graphics where hatch density competes with text and axes. With refined hatch scaling and improved artifact suppression in flat or small-type regions, this filter would be exhibition-ready across all three use cases.

### 8. prussian-cyanotype - 75.25/100 (Strong)

**What's good**

- Consistent Prussian-blue monochrome across photo, comic and chart that convincingly reads as an iron-salt cyanotype print.
- Photo variant: rich mid-to-deep blues preserve facial modelling and create a pleasing photographic portrait mood.
- Comic variant: linework remains clear and the duotone enhances noir and whimsical panels in an artistically appropriate way.
- Chart variant: maintains a restrained, professional look - background wash and tonal gradation give a paper-like feel without overwhelming the data.

**What's not good**

- Highlights and blown whites in the photo lose subtle detail (especially on the cheek and sweater) producing a slightly posterized look.
- Comic panels show uneven contrast - some thin ink lines become faint against midtones, reducing fine-line legibility in busy areas.
- Chart labels and some percentage text suffer mild banding and contrast loss against the paper wash, reducing immediate readibility.
- Occasional haloing and posterization around high-contrast edges across variants indicate limited artifact control on high-frequency detail.

**Judge rationale:** prussian-cyanotype accomplishes its intention admirably: the single prussian-blue palette unifies diverse source imagery and evokes a convincing cyanotype-on-watercolour texture. It is strongest as a photographic and narrative treatment but requires finer tonal mapping and anti-aliasing to preserve thin ink lines and small type at scale. With refined highlight rolloff and improved edge artifact suppression this filter would be exhibition-ready across all three domains.

### 9. copper-plate-etching - 75.18/100 (Strong)

**What's good**

- Consistent warm cream ground and dark-brown line tone convincingly evoke intaglio/copper-plate paper across all three variants.
- Crosshatch density modulation reads naturally on curved surfaces (portrait hair, comic figure shading, chart bars) producing a persuasive engraving look.
- Fine dot-and-line textures have high material believability - micro-roughness and plate grain feel authentic.
- Visual drama is strong in the photo and comic variants where line direction and density create good form modeling and depth.

**What's not good**

- Legibility of precise structure suffers in the chart variant: axis text and small numbers are weakened or lost by the heavy crosshatch overlay.
- Cross-input consistency is uneven: comic and photo retain strong line-art detail, but the chart loses contrast and becomes hard to read.
- Some moire-style interference patterns appear in flat tonal areas (backgrounds, uniform highlights) creating distracting wave artifacts.
- Edge crispness around small text and thin strokes is sometimes ragged, reducing typographic fidelity for data/infographic use.

**Judge rationale:** This filter very effectively translates a copper-plate engraving aesthetic to photographic and illustrated inputs - tone, warmth and hatching feel intentional and crafted. However, its aggressive crosshatch algorithm can collapse small-scale information (charts, fine typography) and produce periodic interference in flat fields. For exhibition use the filter excels on portraits and line art but should be tuned or paired with a legibility pass when applied to data graphics.

### 10. cross-stitch-canvas - 74.95/100 (Strong)

**What's good**

- Clear and consistent X-stitch motif applied across all three variants, reinforcing the hand-embroidery concept.
- Linen background tone is convincing and supports a craft-like aesthetic without calling attention away from stitched forms.
- Stitch density and scale are well chosen to suggest woven thread; small color accents translate well into cross-stitch marks.
- Chart variant preserves intended elements (bars, legend) while adopting the painterly stitched look, suitable for decorative data presentation.

**What's not good**

- Human features in the photo variant lose fine facial detail - important identity cues collapse into coarse Xs, reducing portrait legibility.
- Comic variant shows some local color bleeding where adjacent stitch colors compete, reducing crispness of drawn lines and halving the intended line weight hierarchy.
- Chart axis labels and small text become marginal and faint through the stitch overlay; microtypography is not reliably legible.
- Occasional moire-like interference and haloing appear at high-contrast edges (black X over light areas), creating visual jitter.

**Judge rationale:** This filter delivers a convincing cross-stitch textile look that reads immediately as embroidered linen and works well as a decorative treatment for diverse image types. It excels at preserving large color blocks and conveying material tactility, but it is less forgiving with fine detail and small text - where the X-grid overwhelms information. For exhibition use, pair with images that rely on shape and color rather than micro-detail, or consider adaptive grid scaling to protect typographic legibility.

### 11. silver-daguerreotype - 74.25/100 (Strong)

**What's good**

- Portrait (photo) variant: convincing S-curve toning and metallic sheen that enhance subject modelling and create an authentic antique feel.
- Oval vignette applied consistently creates a focused figure-ground separation that reads well on the photo and comics.
- Metallic grain texture provides tactile richness on detailed areas (hair, coat folds) without overwhelming midtones in the portrait.

**What's not good**

- Comic variant: vignette and heavy desaturation obscure panel borders and flatten linework contrast in places, reducing narrative clarity.
- Chart variant: intense central bleaching and vignette collapse important labels and bars at the image center, harming data legibility.
- Artifact control inconsistent - visible hard clipping and haloing where vignette meets imagery, and uneven noise across tonal ranges.

**Judge rationale:** The filter delivers a very persuasive silver-plate portrait effect: tonal S-curve, cool metallic highlights, and a tasteful oval vignette create strong period character. However, the same processing choices that flatter photographic subjects-central burn and pronounced vignette-compromise readability for high-contrast line art and informational graphics. For broad applicability, the vignette falloff and center exposure should be made adaptive to preserve structure in comics and charts.

### 12. infrared-reverie - 73.75/100 (Strong)

**What's good**

- Portrait (photo variant) - compelling infrared look: bright, glowing highlights on skin and convincing darkened mid/blues that push the subject forward, creating a strong figure-ground separation.
- Comic variant - moody, cinematic conversion that preserves linework and adds halation in highlights, which enhances noir panels and gives playful contrast to the lighter manga-like panel.
- Consistent highlight bloom aesthetic across inputs - visible soft halation and slightly desaturated, warm-ivory paper tone ties the three outputs into a recognizable family.

**What's not good**

- Chart variant - aggressive highlight lift and bloom reduce contrast and reduce text/label legibility; small labels and pale ticks almost vanish against the bleached background.
- Texture handling - in high-detail areas (hair, fine ink lines) the filter sometimes softens micro-contrast, causing mild loss of crispness and edge definition.
- Artifact control - faint banding and haloing around high-contrast edges in the comic and portrait (notably near bright window/sky) are perceptible and occasionally distract.

**Judge rationale:** Infrared-reverie successfully delivers a distinct, cinematic infrared film identity with consistent halation and warm paper toning that reads well across photographic and illustrative material. It excels at creating depth and mood in portraits and narrative art, but its aggressive bloom and highlight treatment undermine information density in data visuals and can blur fine detail. For exhibition use, recommend a 'low-bloom' mode for charts and an optional sharpening pass to recover ink and hair micro-contrast.

### 13. watercolor-bloom - 73.50/100 (Strong)

**What's good**

- Clear, consistent wet-on-wet look across variants with believable pigment bleeds and softened edges that read as watercolor.
- Dried-edge darkening is applied selectively, creating good figure-ground separation in the photo and comic panels.
- Paper granulation texture is visually convincing on the portrait and comic, adding tactile richness.
- Color harmony is warm and restrained in the photo and comic, producing a pleasing, museum-like palette.

**What's not good**

- Chart variant loses important structural legibility - axis lines, labels and small numerals are softened to the point of being hard to read.
- Comic linework sometimes acquires a haloed softening that reduces crisp inking contrast expected in that style.
- On the portrait, fine facial details (hair strands, jewelry) are slightly over-blurred, reducing photographic fidelity.
- Artifact control shows light banding/halos around hard edges in high-contrast areas (chart text, comic inks).

**Judge rationale:** watercolor-bloom succeeds as an evocative wet-on-wet interpreter: it produces convincing pigment diffusion, granulated paper feel, and moody edge darkening that flatter portrait and illustrative inputs. However, the same painterly diffusion undermines informational graphics where crispness and numeric legibility are paramount. For multi-domain use the filter is excellent for expressive and editorial work but should be adjusted or switched off for charts and small-type documents.

### 14. origami-fold - 73.16/100 (Strong)

**What's good**

- Consistent triangular tessellation applied across all three variants, giving a clear origami/faceted concept.
- Crease-like internal shading and thin dark cell borders simulate fold shadows convincingly on cream paper ground.
- Texture rendering creates believable paper relief; highlights and lowlights read as plausible folded planes.
- Maintains recognizable color blocks in the chart and comic inputs, preserving semantic information (bars, panels).

**What's not good**

- Portrait detail is softened to the point that facial features lose fine definition and some identity cues are obscured.
- Comic variant shows occasional over-contrast between facets (hard black seams) that break local shape continuity.
- Chart variant's fine text and thin lines are reduced to fragmented tesserae making small labels illegible.
- Minor haloing and irregular cell sizes at image edges create a patchy border that reduces compositional cleanliness.

**Judge rationale:** Origami-fold is a coherent, well-realised NPR treatment that convincingly simulates triangular paper facets with angular shading. It excels at producing tactile materiality and preserves strong color masses, but it sacrifices small-scale legibility - especially text and fine facial detail - in service of the effect. For exhibition use where mood and surface matter more than microstructure, it is a strong choice; for information-dense images (charts, typographic comics) the algorithm needs tweaks to preserve thin-line fidelity.

### 15. impasto-storm - 73.13/100 (Strong)

**What's good**

- Consistent heavy impasto texture across all three variants - visible canvas grain and directional brush/knife marks impart tactile presence.
- High visual punch in photo and comic variants: saturated, warm color boosts and dramatic highlights create strong emotional emphasis.
- Material simulation is convincing in figurative imagery: hair, fabric, and painted sky read as thick paint with clear stroke orientation.
- Retention of comic linework and panel separations while adding painterly weight preserves the comic's expressive energy.

**What's not good**

- Chart variant suffers legibility loss: text and small numeric labels are softened and partially obscured by texture, reducing information utility.
- Over-saturation in the photo leads to blown warm midtones (skin highlights) and some local color shifts that alter natural appearance.
- Cross-input consistency uneven: excels on photographic and illustrated inputs but compromises functional clarity on data visuals.
- Noticeable haloing and low-frequency posterization in flat areas (backgrounds and white space) introduce distracting artifacts.

**Judge rationale:** Impasto-storm convincingly translates a palette-knife/oil aesthetic to photographs and illustrated comics, delivering strong tactile and chromatic expression. However the same aggressive texture and saturation that benefit portraits and panels undermines the chart's legibility and produces halos in flat fields. For exhibition, I recommend a tuned 'data-safe' mode that reduces texture scale and preserves edge contrast for informational graphics.

### 16. gilded-woodblock - 73.00/100 (Strong)

**What's good**

- Consistent ukiyo-e inspired palette across all three variants - warm sepia/gold tones evoke aged hand-printed paper effectively.
- Photo and comic variants carry strong, expressive contouring and bold flat planes that read like carved woodblock layers.
- Simulated grain and edged ink bleed produce convincing tactile woodblock texture and believable mark-making.

**What's not good**

- Chart variant loses important numeric and text legibility: thick outlines, posterization and texture overwhelm small type and axis marks.
- Colors reduce to a narrow tonal banding that flattens midtone nuance; some highlights clip to harsh pale shapes.
- Cross-input inconsistency: the filter handles figurative and comic linework well but collapses fine detail and annotations in data-dense imagery.
- Visible artifacting around text and thin lines (haloing and irregular jagged edges) undermines precision work.

**Judge rationale:** Gilded-woodblock is a convincing stylistic translation for portraits and comic panels: it preserves figure-ground separation and yields high-impact, print-like surfaces. However, the algorithm sacrifices micro-legibility and smooth tonal transitions required for charts and small type, producing banding and jagged artifacting that hamper informational clarity. In an exhibition context this filter reads as a compelling aesthetic treatment best reserved for narrative imagery rather than data visualization.

### 17. arctic-crystal - 72.85/100 (Strong)

**What's good**

- Clear, consistent Voronoi/crystal motif applied across all three variants - the angular cell borders read as 'frost' and carry a specular highlight that matches the intended cold, crystalline aesthetic.
- Palette is tightly controlled to cool blues and high-contrast whites; highlights and subtle gradients produce believable sparkle and a convincing icy sheen.
- On the photo and comic variants the filter enhances mood and adds dramatic figure-ground layering: faces and important shapes remain perceptible through the pattern, creating an interesting interplay between subject and ornamentation.

**What's not good**

- Chart variant: the strong, high-contrast cell lines and bright specular shards significantly reduce readability of text and numeric labels - key data elements are obscured.
- In places the Voronoi segmentation cuts through important facial and line-art details (particularly eyes and speech balloons), producing awkward fragmentations that impair visual hierarchy.
- Occasional over-bright hotspot clipping at cell intersections produces small blown-out areas that distract from subtle midtone information, especially on photographic skin tones.

**Judge rationale:** Arctic-crystal is conceptually coherent and visually striking - it successfully translates a frozen Voronoi language into specular, icy surfaces. The filter performs best on image-driven and illustrative inputs where ornamentation can be treated as a compositional layer; it is less appropriate for information-dense materials like charts where legibility must be preserved. Minor artifacting around bright shards and fragmentations through faces should be addressed to increase broad applicability.

### 18. byzantine-mosaic - 72.65/100 (Strong)

**What's good**

- Consistent tiled tesserae motif across all three variants with convincing gold grout that sells the Byzantine mosaic idea.
- Tile size and chunky tesserae create an immediate sculptural texture and pleasing tactile quality in the photo and comic variants.
- Brightness variation applied per-tile adds believable hand-made irregularity rather than uniform cell-shading.
- Color accents (blues, pinks, greens) remain readable through the grid, preserving important visual cues, especially in the chart.

**What's not good**

- Figure-ground separation suffers in the photo variant where gold grout and dark tiles collapse midtone detail, muting facial feature clarity.
- Comic variant retains color but loses some midlevel contrast; outlines and important graphic edges are softened by the uniform grid.
- Chart variant's white background plus heavy gold grout over-saturates whitespace, reducing numeric/typographic legibility and creating visual noise behind bars.
- Some visible aliasing and uniform square boundaries produce a mechanical regularity that undercuts the intended hand-cut tesserae at close inspection.

**Judge rationale:** This filter confidently delivers the Byzantine mosaic concept with a strong material presence: gold grout and chunky tiles read immediately and evocatively. It performs best where painterly color and broad shapes dominate (photo, comic) but is less successful for information-dense inputs like charts where the grid competes with data clarity. A refinement to grout translucency and adaptive tile size or edge irregularity would raise legibility and reduce the mechanical artifacting without sacrificing the expressive mosaic identity.

### 19. signal-corrupted - 72.25/100 (Strong)

**What's good**

- Consistent glitch vocabulary across all three variants: horizontal scan lines, RGB channel displacement, and neon block artifacts create a clear, recognizable aesthetic.
- High visual drama in the photo and comic variants - the displacement and chromatic separation add cinematic tension and retro-digital atmosphere.
- Texture feels deliberate: grain, halftone-like noise, and small block corruptions reinforce the intended digital-noise materiality.
- Color accents (cyan/magenta/yellow) are used economically to punctuate composition without overwhelming the base image.

**What's not good**

- Legibility suffers in the chart variant - repeated horizontal bands and color offsets obscure numeric labels and legend items, undermining informational clarity.
- Over-application of uniform horizontal lines occasionally flattens depth in the photo variant, eroding important figure-ground separation around the face.
- Comic panel details (fine line art and text) are softened and sometimes doubled by chromatic shifts, reducing line crispness critical to that style.
- Artifact control is uneven: some corrupt blocks read as purposeful, but others appear as distracting clipping/banding (especially where thin text overlaps heavy lines).

**Judge rationale:** Signal-corrupted succeeds as a coherent glitch filter with a strong stylistic voice; its scan-line and RGB bleed motifs are applied consistently and with aesthetic conviction. However, the treatment is aggressive for data-dense or line-art inputs - it compromises readability where precise structure matters. In exhibition terms this is a memorable and evocative filter best used for portraiture and dramatic illustration rather than charts or small-type graphics.

### 20. brutalist-duotone - 72.15/100 (Strong)

**What's good**

- Very faithful to the stated concept: uncompromising two-colour palette (acid yellow vs charcoal) across all three variants.
- High visual punch in photographic and comic variants - bold figure/ground separation creates immediate Bauhaus-like presence.
- Comic variant preserves linework and panel hierarchy well; halftone grain adds a convincing printed-comic texture.
- Photographic portrait gains a striking silhouette and strong eye-line emphasis, turning a photo into an iconic poster.

**What's not good**

- Chart variant suffers: flat yellow background with heavy grain erodes text and data legibility (percent labels and small legend items are borderline illegible).
- Texture/grain is inconsistent - attractive in comic but noisy in photo and destructive in the chart where it competes with typography.
- Some midtone detail loss in the photo (hair and necklace areas) reduces subtlety; edges in shadows exhibit stair-stepping/artifacting.
- High-contrast conversion sometimes collapses small shapes into blobs (notably small icons and thin chart ticks), harming functional use-cases.

**Judge rationale:** This filter successfully commits to a militant two-colour identity that reads as purposefully Bauhaus and aggressive; it excels as a poster/comic aesthetic. However, its aggressive grain and clipping strategy, while expressive for imagery, undermines information graphics and fine typographic elements. For exhibition use, pair this filter with designs meant to be bold and symbolic rather than detail-dependent.

### 21. cmyk-separation - 72.05/100 (Strong)

**What's good**

- Clear and consistent halftone concept: distinct CMYK dot screens and slight misregistration are evident across all variants.
- High visual character in photo and comic variants - the dot screens create an evocative retro print aesthetic with pleasing contrast and silhouette retention.
- Color separation produces recognizable cyan/yellow/magenta accents that enhance form and mood, especially in the comic panels where colors remain distinct.
- Material quality: dots retain believable halftone grain and tactile sense rather than looking like simple pixelation.

**What's not good**

- Structure legibility suffers in the chart variant - small text and thin lines break down and become difficult to read because dot patterns and registration obscure fine detail.
- Cross-input consistency: while expressive on photo and comic inputs, the filter fails to preserve data clarity for analytical graphics (bars, legend text).
- Artifact control: minor moire and local over-inking appear in dense dark areas (notably in the noir panel and hair in the portrait), producing slight mushiness.
- Color tonal mastery occasionally flattens midtones - skin and subtle gradients lose some nuance to the dot matrix, reducing depth.

**Judge rationale:** This implementation is a convincing and visually delightful CMYK halftone emulator that nails the nostalgic press look for photographic and illustrative content. However, its application to informational graphics reveals limitations: fine typographic and chart elements are degraded by dot screening and misregistration. For exhibition use, it excels as an expressive stylistic filter but should be adjusted or masked when preserving legibility of data or small type is required.

### 22. synthwave-horizon - 71.64/100 (Strong)

**What's good**

- Consistent 1980s vaporwave palette (purple->pink->cyan) applied across all three variants, which reinforces the intended aesthetic.
- Strong cinematic scanline and chromatic-aberration treatments give the photo and comic variants an evocative retro-electronic atmosphere.
- Grid/floor perspective is most successful on the chart: the perspective floor grid is visible and helps tie the composition to the synthwave concept.
- Linework and halftone-like texture in the comic variant remain readable and energetic, preserving panel hierarchy and pop-art expressiveness.

**What's not good**

- Photo variant: facial detail and small features suffer from over-shifted chromatic aberration and horizontal banding, which cuts into figure-ground clarity.
- Chart variant: color shifts reduce contrast on text and small numbers, impairing legibility of fine typography and legend elements.
- Cross-input inconsistency: treatment intensity varies (photo and comic are strong; chart is stylized but loses critical data legibility).
- Artifacts: horizontal scanlines sometimes align with important labels and bar values, creating distracting visual collisions.

**Judge rationale:** The filter delivers a convincing vaporwave identity-rich magenta/purple gradients, scanline texture, and a usable grid-making the comic and photographic inputs visually striking. However, aggressive aberration and scanline placement occasionally undermine essential information (facial micro-contrast, numeric labels) in the photo and chart variants. For exhibition use, tune the chromatic offset and line density adaptively per input to preserve legibility while retaining the aesthetic punch.

### 23. cathedral-glass - 71.21/100 (Strong)

**What's good**

- Clear stained-glass concept: bold flat color regions separated by dark lead-like borders are consistently present in all three variants.
- High visual punch: backlit glow and saturated hues (especially in the comic panel) create immediate emotional and decorative appeal.
- NPR expressiveness: the filter simplifies forms into readable mosaics, giving photographic subjects a decorative, iconographic quality.
- Color separation works well in colorful inputs (comic, chart) where palette blocks remain distinct.

**What's not good**

- Facial/figure detail suffers: in the photo variant the lead borders fragment faces into pixelated blocks that reduce important facial features and expression.
- Chart/typography legibility is compromised: the filter converts small text and fine lines into blocky artifacts making numeric labels unreadable in the chart variant.
- Inconsistent border weight and occasional haloing: some borders become uneven or semi-transparent causing local visual noise, most noticeable around high-contrast edges.
- Artifacting and block quantization: visible stair-stepping and micro-block noise create distracting patches, especially in midtone transitions.

**Judge rationale:** This filter convincingly translates the stained-glass idea into a bold decorative style and produces strong, iconic results on colorful, graphic inputs. It is less successful where fine detail or text legibility matters - facial nuance and chart labels are lost to block quantization and inconsistent border rendering. With improved edge consistency and reduced micro-artifacts it would be excellent across photo, comic, and chart domains.

### 24. pop-art-screen - 70.95/100 (Strong)

**What's good**

- Consistent Warhol-inspired motif: flat color zones with a regular Ben-Day dot overlay and bold contouring read clearly across all three variants.
- High visual punch in the comic panel: outlines remain crisp and the halftone pattern boosts the retro comic feel without overwhelming linework.
- Photo variant retains facial features and hair texture through delicate line-work and sparse color, preserving figure-ground separation.
- Chart variant applies halftone fills to bars in a way that preserves the categorical color-coding, helping legend correspondence.

**What's not good**

- Color quantization is uneven: the photo has very desaturated fields (almost white) causing loss of flat color impact expected from Pop Art.
- Dot scale and density are inconsistent between inputs - too sparse in the photo and slightly noisy in the chart, reducing perceived material coherence.
- Thin outlines sometimes break into sketchy strokes (particularly in the photo), which undermines bold, uniform silhouette expected from the intended aesthetic.
- Small text and fine numeric labels in the chart suffer from dot-induced speckle, reducing legibility at typical viewing sizes.

**Judge rationale:** This filter admirably translates a Warhol/Ben-Day concept across disparate inputs, producing a recognizably pop-art effect while mostly honoring underlying structure. It excels on illustrative comic content where the halftone and outlines amplify meaning, but the photo and chart variants reveal inconsistencies in dot scale, color fill strength, and micro-artifact control that limit its professional application without per-input parameter tuning.

### 25. charcoal-on-kraft - 70.05/100 (Strong)

**What's good**

- Consistent warm kraft base tone across all three outputs reinforces the intended paper substrate.
- Charcoal-like directional shading and mark suggestion are convincing on the photo and comic variants, adding expressive, hand-made character.
- Pigment clumping and subtle fibre granularity are well simulated - visible noise and paper speckle read as material texture rather than digital noise.
- Comic panels retain strong edge definition and panel framing, preserving the narrative structure.

**What's not good**

- Photo variant under-abstracts facial detail in deep shadows, flattening midtone modeling and losing some figure-ground separation.
- Chart variant suffers from reduced contrast and washed legend/text - data labels and gridlines are faint and occasionally illegible.
- Cross-input consistency varies: the filter leans heavy on dark blocking in some areas (comic noir panel) but becomes muddy in the bar chart, reducing utility for informational graphics.
- Minor banding and grain aggregation present in flat-tone areas (chart background) distract from a fully convincing tactile finish.

**Judge rationale:** This filter delivers a strong, evocative kraft-and-charcoal look that reads immediately as a handcrafted print across pictorial inputs. It excels at giving portraits and illustrated comics a rich, tactile presence, though it over-commitsto deep blocking in places and reduces legibility on information-dense charts. With a tuning pass to preserve thin text and subtle midtone detail, it would be a highly versatile and exhibition-ready non-photorealistic treatment.

### 26. iron-rust - 68.35/100 (Promising)

**What's good**

- Strong thematic consistency: the warm orange-brown palette and fine speckled pitting read unmistakably as oxidized metal across all three variants.
- Multi-scale corrosion texture: both macro (horizontal grain and streaking) and micro (dense dark speckles) are present, giving believable depth and age.
- NPR expressiveness on comic: the rust treatment enhances mood for noir panels and integrates well with line art, adding period-authentic patina.
- Photoreal portrait retains a convincing metal-tone treatment without completely destroying facial modeling - highlights and hair retain dimensionality.

**What's not good**

- Legibility loss on chart: speckle density and contrast significantly reduce readability of small text and fine gridlines, harming data communication.
- Overly uniform spot pattern: the speckle placement repeats at similar scales and densities across all variants, reducing natural randomness and making artifacts look procedural.
- Artifact halos and contrast clipping: darker speckles sit on top of important dark lines in the comic and on facial features in the photo, creating distracting visual noise.
- Horizontal grain is subtle and inconsistent: intended striations are weak in the chart and uneven in the portrait, so the 'horizontal grain' aspect is not reliably present.

**Judge rationale:** Iron-rust compellingly conveys oxidized metal through color and pitting texture, and it works particularly well as a mood layer for imagery and comics. However, the dense, repeating speckle pattern and insufficient control over small-scale contrast impair functional uses (charts, legible text) and introduce visible artifacts over critical details. With more randomized distribution, stronger control to preserve high-contrast edges and adaptive mask for text/faces, this filter could move from promising to demonstrably strong in mixed outputs.

### 27. noir-rain - 68.05/100 (Strong)

**What's good**

- Clear, consistent motif: vertical rain streaks are applied uniformly across all variants and strongly support the film-noir-with-neon concept.
- High emotional punch in the photo and noir comic panels - dramatic contrast and selective neon rim-lighting create cinematic figure-ground separation.
- Stylized color accents (neon reds/yellows) read well against desaturated backgrounds, adding neon-reflection cues that reinforce the intent.
- Texture feels intentionally analogue: grain and streaking convey wet surfaces and atmosphere, which suits the intended aesthetic.

**What's not good**

- Chart variant loses important data legibility: rain streaks and grain overlay obscure small text and percentage labels, reducing communicative function.
- Comic variant shows inconsistent treatment between panels: the bright, colorful cartoon square competes awkwardly with the dark noir panel rather than blending as a unified series.
- Photo face rendering includes posterization and haloed chromatic edges around highlights that look like processing artifacts rather than deliberate neon glow.
- Artifacts: occasional banding, harsh clipping on highlights, and pixel-level color fringing reduce polish when inspected closely.

**Judge rationale:** Noir-rain captures a compelling, cinematic mood and translates the vertical-rain + neon idea across very different inputs, which is notable. However, the filter sacrifices functional legibility in the chart and sometimes introduces posterization/halo artifacts that feel accidental. Refining highlight handling and reducing rain opacity over small typography would raise this from a strong stylistic effect to an exhibition-ready tool.

### 28. holographic-foil - 65.25/100 (Promising)

**What's good**

- Strong, consistent iridescent rainbow hue shifts that read as a metallic foil across all three variants.
- High visual punch on the photo and comic inputs - the effect creates an arresting, surreal surface that draws attention to form and contours.
- Color placement follows apparent surface gradients (faces, folds, comic linework), which supports the intended foil illusion.

**What's not good**

- Legibility suffers on information-dense content (chart): color noise and micro-patterns obscure numeric labels and reduce clarity.
- On the photo, fine facial detail is both enhanced and disrupted - hair and skin show attractive sheen but also blocky posterization and chroma fringes around edges.
- Comic variant has uneven application: line art remains mostly readable but large flat areas acquire distracting tiled/rectilinear pixelation, breaking the organic metallic illusion.
- Noticeable artifacts: banding, blocky quantization, and aliasing visible in background regions and along high-contrast edges.

**Judge rationale:** This filter convincingly communicates a holographic-foil concept with vivid rainbow shifts and gradient-driven color placement, producing striking, memorable results especially on portrait and illustrative inputs. However, the algorithm struggles with preserving information hierarchy and fine typographic legibility - micro-patterning and quantization artifacts become problematic on charts and in some large flat color regions. With improved artifact control and softer spatial filtering to preserve text and continuous tone, this is a strong candidate for creative use where legibility is secondary.

### 29. solarized-dream - 64.25/100 (Promising)

**What's good**

- Strong, consistent Sabattier-inspired tri-channel shifts produce a recognizably solarized aesthetic across all three variants.
- High visual punch: the psychedelic red/green/blue separations create memorable, dramatic silhouettes and figure-ground contrast in the photo and comic variants.
- Comic variant benefits from heightened chromatic separation that accentuates line-work and poster-like energy.
- Photo retains believable highlight reversal on skin tones, producing an intriguing luminous portrait effect rather than purely destructive posterization.

**What's not good**

- Color balance is aggressive and uneven: per-channel thresholds yield large area color clipping that destroys subtle midtone gradations (especially visible in background areas).
- Chart variant fails functional legibility - text and fine numeric labels are darkened or lost against neon edges, undermining information clarity.
- Artifacts and haloing around high-contrast edges (particularly red/green chroma fringes) distract in the comic and photo images.
- Cross-input consistency suffers: what reads as expressive in the photo/comic becomes obfuscating in data/typographic content.

**Judge rationale:** Solarized-dream successfully translates the Sabattier concept into a vivid, psychedelic family of outputs, delivering strong emotional impact for photographic and illustrative material. However, its hard per-channel thresholds and extreme chroma boosts compromise subtle tonal modeling and renderings that require typographic or numerical legibility. For exhibition use, this filter shines as an expressive visual treatment but should be avoided for charts or any content where precise information must remain readable.

### 30. pointillist-garden - 62.25/100 (Promising)

**What's good**

- Strong adherence to a Seurat-like broken-colour dot vocabulary: discrete pigment-like dots with varied radius across all three variants.
- Pleasant tactile impression - the dots read convincingly as pigment on a white ground and create an engaging painterly surface.
- High visual presence on photographic and comic inputs: the treatment produces a decorative, expressive look that reads at gallery scale.
- Color choices generally respect source hue relationships, preserving warm skin tones and cool shadows in the photo and vivid comic palette.

**What's not good**

- Heavy use of white/very light dots in the photo variant breaks figure-ground clarity and creates distracting speckling over facial features.
- Comic variant shows uneven dot edge framing (thick black dot borders) that flattens internal detail and can obscure linework and type.
- Chart variant fails to preserve small-scale structure and typographic legibility: legend text and axis labels become unreadable.
- Artifact control inconsistent: haloing and clustered white noise appear in darker mid-tones, producing visual clutter rather than controlled broken colour.

**Judge rationale:** Pointillist-garden delivers a convincing painterly dot texture and evocative color mixing on large, pictorial subjects, but the algorithm struggles with small-scale, high-contrast information. Portrait features are often masked by over-dense light speckling and charts/labels collapse into unreadable speckle. For exhibition use, tune dot density and exclude or reduce high-value (white) dot insertion over critical mid-tone detail to improve legibility while retaining the attractive material quality.

## Research Basis Used

- Gestalt perception and whole-form reading: https://en.wikipedia.org/wiki/Gestalt_psychology
- Visual hierarchy and figure-ground emphasis: https://en.wikipedia.org/wiki/Visual_hierarchy
- Color behavior, harmony/contrast traditions: https://en.wikipedia.org/wiki/Color_theory
- Graphical perception (Cleveland & McGill lineage): https://en.wikipedia.org/wiki/Graphical_perception
- Visual variables and information encoding (Bertin lineage): https://en.wikipedia.org/wiki/Map_symbol#Visual_variables
- Perceptual structure and artifact thinking (SSIM/IQA framing): https://en.wikipedia.org/wiki/Structural_similarity and https://en.wikipedia.org/wiki/Image_quality
- Non-photorealistic rendering context: https://en.wikipedia.org/wiki/Non-photorealistic_rendering
