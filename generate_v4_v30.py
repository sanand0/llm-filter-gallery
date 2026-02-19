#!/usr/bin/env python3
"""
Master generator for image filter versions v4-v30.
Run from the project root: python3 generate_v4_v30.py
"""

import os
import sys
import subprocess
import tempfile
import textwrap
import stat
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageDraw
from scipy.ndimage import gaussian_filter, uniform_filter

BASE = Path(__file__).parent
INPUTS = {
    'chart': BASE / 'inputs/chart.avif',
    'comic': BASE / 'inputs/comic.avif',
    'photo': BASE / 'inputs/photo.avif',
}


def load_avif(path: Path) -> Image.Image:
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        tmp = f.name
    subprocess.run(['ffmpeg', '-y', '-i', str(path), tmp],
                   capture_output=True, check=True)
    img = Image.open(tmp).convert('RGB')
    os.unlink(tmp)
    return img


def save_webp(img: Image.Image, path: Path):
    img.save(str(path), 'WEBP', quality=75, method=6)


# =============================================================================
# FILTER IMPLEMENTATIONS  (each takes PIL RGB Image → PIL RGB Image)
# =============================================================================

def apply_v4(img):
    """Risograph Reverie – 2-colour halftone on cream, channels misregistered."""
    w, h = img.size
    rng = np.random.default_rng(42)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0
    gray_blur = gaussian_filter(gray, sigma=1.5)

    def halftone(luma, angle_deg, dot=9):
        import math
        a = math.radians(angle_deg)
        ca, sa = math.cos(a), math.sin(a)
        yy, xx = np.mgrid[0:h, 0:w]
        rx = xx * ca + yy * sa
        ry = -xx * sa + yy * ca
        gx = (rx % dot) - dot / 2
        gy = (ry % dot) - dot / 2
        dist = np.sqrt(gx ** 2 + gy ** 2)
        radius = gaussian_filter(luma, 1) * dot * 0.68
        return (dist < radius).astype(np.float32)

    # Channel 1: coral red at 15°
    ht1 = halftone(gray_blur, 15)
    # Channel 2: teal at 75°  (slight x/y mis-register +4 px)
    ht2_raw = halftone(gray_blur, 75)
    ht2 = np.roll(np.roll(ht2_raw, 4, axis=1), 3, axis=0)

    # Cream paper base
    paper = np.ones((h, w, 3), dtype=np.float32) * [0.96, 0.93, 0.87]
    paper += rng.normal(0, 0.010, (h, w, 3))

    # Coral
    coral = np.array([0.88, 0.22, 0.18])
    # Teal
    teal  = np.array([0.06, 0.56, 0.62])

    out = paper.copy()
    for c in range(3):
        out[:, :, c] = np.where(ht1 > 0.5, paper[:, :, c] * 0.25 + coral[c] * 0.75, out[:, :, c])
    for c in range(3):
        out[:, :, c] = np.where(ht2 > 0.5, out[:, :, c] * 0.40 + teal[c] * 0.60, out[:, :, c])

    out = np.clip(out, 0, 1)
    return Image.fromarray((out * 255).astype(np.uint8))


def apply_v5(img):
    """Silver Daguerreotype – antique silver-plate portrait."""
    w, h = img.size
    rng = np.random.default_rng(7)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # S-curve: compress shadows, blow highlights
    def s_curve(x):
        return np.where(x < 0.5,
                        2 * x * x,
                        1 - 2 * (1 - x) ** 2)

    luma = s_curve(gray)

    # Fine metallic grain (not gaussian – bimodal clumps)
    grain = rng.normal(0, 0.018, (h, w))
    grain += rng.exponential(0.008, (h, w)) * rng.choice([-1, 1], (h, w))
    luma = np.clip(luma + grain, 0, 1)

    # Silver tint: warm in shadows, cool-neutral in highlights
    r = luma * 0.92 + 0.04
    g = luma * 0.94 + 0.02
    b = luma * 0.98

    # Oval vignette
    yy, xx = np.mgrid[0:h, 0:w]
    cx, cy = w / 2, h / 2
    ell = ((xx - cx) / (cx * 0.82)) ** 2 + ((yy - cy) / (cy * 0.87)) ** 2
    vig = np.clip(1.0 - (ell - 0.5) * 2.0, 0.0, 1.0)

    rgb = np.stack([r * vig, g * vig, b * vig], axis=2)

    # Subtle highlight bloom
    bright_mask = gaussian_filter((luma > 0.80).astype(float), sigma=6) * 0.12
    rgb[:, :, 0] = np.clip(rgb[:, :, 0] + bright_mask, 0, 1)
    rgb[:, :, 1] = np.clip(rgb[:, :, 1] + bright_mask, 0, 1)
    rgb[:, :, 2] = np.clip(rgb[:, :, 2] + bright_mask * 1.1, 0, 1)

    return Image.fromarray((np.clip(rgb, 0, 1) * 255).astype(np.uint8))


def apply_v6(img):
    """Synthwave Horizon – 80s vaporwave with perspective grid & neon glow."""
    w, h = img.size
    rng = np.random.default_rng(13)
    arr = np.array(img, dtype=np.float32) / 255.0
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Purple-to-pink-to-blue gradient colormap
    def synthwave_lut(t):
        # t in [0,1] → (r,g,b)
        stops = [(0.0,  [0.05, 0.00, 0.22]),
                 (0.30, [0.48, 0.00, 0.55]),
                 (0.55, [0.98, 0.10, 0.55]),
                 (0.75, [0.99, 0.60, 0.10]),
                 (1.0,  [0.10, 0.85, 0.98])]
        ts = [s[0] for s in stops]
        rs = [s[1][0] for s in stops]
        gs = [s[1][1] for s in stops]
        bs = [s[1][2] for s in stops]
        return (np.interp(t, ts, rs),
                np.interp(t, ts, gs),
                np.interp(t, ts, bs))

    r, g, b = synthwave_lut(gray)
    out = np.stack([r, g, b], axis=2)

    # Perspective floor grid overlay (bottom third)
    grid = np.zeros((h, w), dtype=np.float32)
    horizon = int(h * 0.60)
    for row in range(horizon, h):
        progress = (row - horizon) / max(h - horizon, 1)
        # Horizontal line every ~20 perspective-foreshortened units
        if int(progress * 120) % 10 == 0:
            grid[row, :] = 0.55
    # Vertical perspective lines converging to center-top
    cx = w // 2
    for vx in range(-w // 2, w // 2, 32):
        for row in range(horizon, h):
            progress = (row - horizon) / max(h - horizon, 1)
            x = int(cx + vx * progress)
            if 0 <= x < w:
                grid[row, x] = 0.55
    grid_blur = gaussian_filter(grid, sigma=0.8)
    for c in range(3):
        out[:, :, c] = np.clip(out[:, :, c] + grid_blur * [0.90, 0.10, 0.90][c], 0, 1)

    # CRT scanlines
    scanlines = np.ones((h, 1))
    scanlines[::3] = 0.75
    out *= scanlines[:, :, np.newaxis]

    # Chromatic aberration
    shift = 4
    out_r = np.roll(out[:, :, 0], shift, axis=1)
    out_b = np.roll(out[:, :, 2], -shift, axis=1)
    out[:, :, 0] = out_r
    out[:, :, 2] = out_b

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v7(img):
    """Impasto Storm – thick oil-paint brushstroke texture."""
    w, h = img.size
    rng = np.random.default_rng(99)
    arr = np.array(img, dtype=np.float32) / 255.0

    # Boost saturation and warmth first
    pil = ImageEnhance.Color(img).enhance(2.0)
    pil = ImageEnhance.Contrast(pil).enhance(1.4)
    arr = np.array(pil, dtype=np.float32) / 255.0

    # Multiple box-filter passes to create paint-smear regions
    smear = arr.copy()
    for _ in range(6):
        smear = uniform_filter(smear, size=[5, 5, 1])
    # Blend original detail back
    mixed = arr * 0.35 + smear * 0.65

    # Generate brushstroke emboss texture
    # Random directional noise
    noise = rng.normal(0, 1.0, (h, w))
    noise_blur_h = gaussian_filter(noise, sigma=[2, 0.3])
    noise_blur_v = gaussian_filter(noise, sigma=[0.3, 2])
    bx = gaussian_filter(noise_blur_h, sigma=1)
    by = gaussian_filter(noise_blur_v, sigma=1)
    # Emboss from gradient
    emboss = bx - by
    emboss = (emboss - emboss.min()) / (emboss.max() - emboss.min() + 1e-8)
    emboss = emboss * 2 - 1  # -1..1

    # Apply emboss as texture: lighten where light hits, darken in shadows
    texture = emboss * 0.18
    for c in range(3):
        mixed[:, :, c] = np.clip(mixed[:, :, c] + texture, 0, 1)

    # Final saturation pop
    out = Image.fromarray((mixed * 255).astype(np.uint8))
    out = ImageEnhance.Color(out).enhance(1.5)
    return out


def apply_v8(img):
    """Graphite Study – pencil sketch with crosshatch on cream paper."""
    w, h = img.size
    rng = np.random.default_rng(21)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Edge map (inverted for dark lines on light background)
    pil_gray = img.convert('L')
    sharp = pil_gray.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=2))
    edges = sharp.filter(ImageFilter.FIND_EDGES)
    edge_arr = np.array(edges, dtype=np.float32) / 255.0
    edge_arr = np.clip(edge_arr * 2.5, 0, 1)

    # Crosshatch in shadow regions (luma < 0.4)
    shadow_mask = (gray < 0.40).astype(float)
    shadow_mask = gaussian_filter(shadow_mask, sigma=1)

    # Hatch lines at 45° and 135°
    yy, xx = np.mgrid[0:h, 0:w]
    hatch1 = ((xx + yy) % 8 < 1.2).astype(float) * shadow_mask
    hatch2 = ((xx - yy) % 8 < 1.2).astype(float) * shadow_mask * (gray < 0.28).astype(float)
    hatch = np.clip(hatch1 + hatch2, 0, 1)

    # Cream paper
    paper = np.ones((h, w, 3), dtype=np.float32) * [0.96, 0.94, 0.89]
    paper += rng.normal(0, 0.008, (h, w, 3))

    # Combine: paper - edges (dark) - hatch (dark)
    marks = np.clip(edge_arr + hatch * 0.65, 0, 1)
    for c in range(3):
        paper[:, :, c] = np.clip(paper[:, :, c] - marks * [0.85, 0.82, 0.75][c], 0, 1)

    return Image.fromarray((np.clip(paper, 0, 1) * 255).astype(np.uint8))


def apply_v9(img):
    """Watercolor Bloom – wet-on-wet pigment bleeds on textured paper."""
    w, h = img.size
    rng = np.random.default_rng(55)
    arr = np.array(img, dtype=np.float32) / 255.0

    # Bleach out (watercolors are light and transparent)
    arr = arr * 0.75 + 0.18

    # Wet spread: aggressive blur to simulate water spreading
    wet = gaussian_filter(arr, sigma=[6, 6, 0])
    arr = arr * 0.45 + wet * 0.55

    # Edge-darkening (dried paint concentrates at edges of wet areas)
    gray = np.mean(arr, axis=2)
    gray_blur = gaussian_filter(gray, sigma=4)
    edge_dark = np.clip(np.abs(gray - gray_blur) * 4, 0, 1)
    for c in range(3):
        arr[:, :, c] = np.clip(arr[:, :, c] - edge_dark * 0.25, 0, 1)

    # Paper texture
    paper_noise = rng.normal(0, 0.025, (h, w))
    paper_noise = gaussian_filter(paper_noise, sigma=1.2)
    for c in range(3):
        arr[:, :, c] = np.clip(arr[:, :, c] + paper_noise * 0.5, 0, 1)

    # Granulation (pigment settling in paper valleys)
    gran = rng.normal(0, 0.020, (h, w, 3))
    dark_mask = (1 - gray)[:, :, np.newaxis] ** 1.5
    arr = np.clip(arr + gran * dark_mask, 0, 1)

    # Final desaturate slightly (watercolors are never fully saturated)
    out = Image.fromarray((arr * 255).astype(np.uint8))
    out = ImageEnhance.Color(out).enhance(0.80)
    return out


def apply_v10(img):
    """Cross-Stitch Canvas – embroidery on linen with X-stitch marks."""
    w, h = img.size
    STITCH = 9  # pixels per stitch cell

    # Downsample to stitch resolution
    sw, sh = w // STITCH, h // STITCH
    small = img.resize((sw, sh), Image.LANCZOS)
    colors = np.array(small, dtype=np.float32) / 255.0

    # Linen background
    out = np.ones((h, w, 3), dtype=np.float32) * [0.88, 0.84, 0.76]
    rng = np.random.default_rng(33)

    # Add linen weave texture
    yy, xx = np.mgrid[0:h, 0:w]
    weave = (np.sin(xx * np.pi / 2) * 0.035 +
             np.sin(yy * np.pi / 2) * 0.035)
    for c in range(3):
        out[:, :, c] += weave

    # Draw X stitches
    for sy in range(sh):
        for sx in range(sw):
            col = colors[sy, sx]
            py = sy * STITCH
            px = sx * STITCH
            s = STITCH - 1
            # Draw two diagonal lines of the X
            for i in range(s + 1):
                x1, y1 = px + i, py + i
                x2, y2 = px + s - i, py + i
                if 0 <= y1 < h and 0 <= x1 < w:
                    out[y1, x1] = col * 0.82
                if 0 <= y2 < h and 0 <= x2 < w:
                    out[y2, x2] = col * 0.82

    out = np.clip(out + rng.normal(0, 0.012, (h, w, 3)), 0, 1)
    return Image.fromarray((out * 255).astype(np.uint8))


def apply_v11(img):
    """Cathedral Glass – stained glass with lead came and backlit glow."""
    w, h = img.size
    arr = np.array(img, dtype=np.float32) / 255.0

    # Segment into stained glass regions using heavy blur + quantized grid
    CELL = 48
    sw, sh = w // CELL + 1, h // CELL + 1
    small = img.resize((sw, sh), Image.NEAREST)
    # Upsample back to create flat color regions
    flat = small.resize((w, h), Image.NEAREST)
    flat_arr = np.array(flat, dtype=np.float32) / 255.0

    # Supersaturate the flat colors
    flat_pil = Image.fromarray((flat_arr * 255).astype(np.uint8))
    flat_pil = ImageEnhance.Color(flat_pil).enhance(3.5)
    flat_arr = np.array(flat_pil, dtype=np.float32) / 255.0

    # Lead came: find edges between cells and draw dark borders
    gray_flat = np.mean(flat_arr, axis=2)
    # Detect transitions
    dx = np.abs(np.diff(gray_flat, axis=1, prepend=gray_flat[:, :1]))
    dy = np.abs(np.diff(gray_flat, axis=0, prepend=gray_flat[:1, :]))
    edges = np.clip((dx + dy) * 8, 0, 1)
    edges = gaussian_filter(edges, sigma=1.0)
    lead = (edges > 0.15).astype(float)
    lead_thick = gaussian_filter(lead, sigma=1.2)

    # Backlit glow (brighten slightly overall, strong in mid-tones)
    glow = gaussian_filter(flat_arr, sigma=3) * 0.25
    lit = np.clip(flat_arr + glow, 0, 1)

    # Apply lead came (near black)
    for c in range(3):
        lit[:, :, c] = lit[:, :, c] * (1 - lead_thick * 0.92)

    return Image.fromarray((np.clip(lit, 0, 1) * 255).astype(np.uint8))


def apply_v12(img):
    """Signal Corrupted – digital glitch with scan displacement & RGB bleed."""
    w, h = img.size
    rng = np.random.default_rng(666)
    arr = np.array(img, dtype=np.float32) / 255.0

    # RGB channel displacement
    shift_r = rng.integers(3, 9)
    shift_b = rng.integers(3, 9)
    arr[:, :, 0] = np.roll(arr[:, :, 0],  shift_r, axis=1)
    arr[:, :, 2] = np.roll(arr[:, :, 2], -shift_b, axis=1)

    # Horizontal scan-line displacement (random row shifts)
    n_glitch_rows = rng.integers(30, 70)
    glitch_rows = rng.integers(0, h, n_glitch_rows)
    for row in glitch_rows:
        dx = rng.integers(-40, 40)
        arr[row] = np.roll(arr[row], dx, axis=0)

    # Block corruption: random rectangles with wrong colors
    for _ in range(12):
        bh = rng.integers(4, 20)
        bw = rng.integers(20, 100)
        by = rng.integers(0, h - bh)
        bx = rng.integers(0, w - bw)
        color = rng.random(3)
        alpha = rng.uniform(0.3, 0.7)
        arr[by:by+bh, bx:bx+bw] = arr[by:by+bh, bx:bx+bw] * (1-alpha) + color * alpha

    # Scan-line dropout (random dark lines)
    dropout = rng.choice([0, 1], h, p=[0.04, 0.96]).astype(float)
    arr *= dropout[:, np.newaxis, np.newaxis]

    # Neon color noise overlay
    noise = rng.normal(0, 0.04, (h, w, 3))
    arr = np.clip(arr + noise, 0, 1)

    return Image.fromarray((arr * 255).astype(np.uint8))


def apply_v13(img):
    """Verdigris Antiquity – oxidized copper patina with metallic texture."""
    w, h = img.size
    rng = np.random.default_rng(88)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Patina colormap: dark brown → rust → olive → teal → pale blue-green
    stops_t = [0.0,  0.20, 0.40, 0.62, 0.82, 1.0]
    stops_r  = [0.10, 0.30, 0.45, 0.22, 0.32, 0.72]
    stops_g  = [0.07, 0.15, 0.28, 0.42, 0.58, 0.78]
    stops_b  = [0.04, 0.08, 0.10, 0.30, 0.50, 0.70]
    r = np.interp(gray, stops_t, stops_r)
    g = np.interp(gray, stops_t, stops_g)
    b = np.interp(gray, stops_t, stops_b)

    # Multi-scale oxidation texture
    tx1 = rng.normal(0, 1, (h, w))
    tx2 = rng.normal(0, 1, (h // 2, w // 2))
    from PIL import Image as PilImg
    tx2_up = np.array(PilImg.fromarray(tx2).resize((w, h), PilImg.BILINEAR))
    texture = gaussian_filter(tx1, 2) * 0.6 + gaussian_filter(tx2_up, 4) * 0.4
    texture = (texture - texture.min()) / (texture.max() - texture.min()) - 0.5

    # Raised areas lighter, recessed darker
    bump = texture * 0.12
    r = np.clip(r + bump, 0, 1)
    g = np.clip(g + bump * 1.1, 0, 1)
    b = np.clip(b + bump * 0.8, 0, 1)

    # Metallic highlight on bright areas
    highlight = (gray > 0.75).astype(float)
    highlight = gaussian_filter(highlight, sigma=3) * 0.25
    r = np.clip(r + highlight * 0.6, 0, 1)
    g = np.clip(g + highlight * 0.7, 0, 1)
    b = np.clip(b + highlight * 0.5, 0, 1)

    return Image.fromarray((np.stack([r, g, b], axis=2) * 255).astype(np.uint8))


def apply_v14(img):
    """Infrared Reverie – IR film with glowing whites and inverted foliage."""
    w, h = img.size
    arr = np.array(img, dtype=np.float32) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

    # IR effect: bright channel is boosted red; blue/green go dark
    # Simulate "wood effect": areas with high green relative to red → become bright white
    wood = np.clip((g - r * 0.5) * 2.0, 0, 1)  # high green = white in IR
    ir_luma = r * 0.6 + wood * 0.4
    ir_luma = np.clip(ir_luma * 1.3, 0, 1)

    # Sky/blue areas go very dark
    sky = np.clip((b - r) * 1.5, 0, 1)
    ir_luma = np.clip(ir_luma - sky * 0.5, 0, 1)

    # Highlight bloom (halation) on bright areas
    bloom = gaussian_filter((ir_luma > 0.75).astype(float), sigma=12) * 0.45
    ir_luma = np.clip(ir_luma + bloom, 0, 1)

    # Tone as warm-silver (slight cream tint)
    rout = ir_luma * 1.02
    gout = ir_luma * 0.99
    bout = ir_luma * 0.94

    # Add IR film grain (clumpy)
    rng = np.random.default_rng(14)
    grain = rng.normal(0, 0.018, (h, w))
    grain = gaussian_filter(grain, sigma=0.6)
    rout = np.clip(rout + grain, 0, 1)
    gout = np.clip(gout + grain, 0, 1)
    bout = np.clip(bout + grain, 0, 1)

    return Image.fromarray((np.stack([rout, gout, bout], axis=2) * 255).astype(np.uint8))


def apply_v15(img):
    """Linocut Bold – stark relief-print in black ink on off-white paper."""
    w, h = img.size
    rng = np.random.default_rng(15)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Boost contrast before thresholding
    pil_g = ImageEnhance.Contrast(img.convert('L')).enhance(2.0)
    gray_c = np.array(pil_g, dtype=np.float32) / 255.0

    # Threshold
    binary = (gray_c < 0.52).astype(np.float32)

    # Morphological cleanup: small isolated dots removed
    from skimage import morphology as morph
    binary_bool = binary.astype(bool)
    binary_bool = morph.remove_small_objects(binary_bool, min_size=40)
    binary_bool = morph.remove_small_holes(binary_bool, area_threshold=40)
    binary = binary_bool.astype(float)

    # Rough edge effect: erode/dilate with slight irregularity
    noise_edge = rng.normal(0, 0.5, (h, w))
    binary_noisy = np.clip(binary + noise_edge * 0.08, 0, 1)

    # Off-white paper
    paper_r = 0.95 + rng.normal(0, 0.012, (h, w))
    paper_g = 0.93 + rng.normal(0, 0.012, (h, w))
    paper_b = 0.87 + rng.normal(0, 0.012, (h, w))

    ink = np.array([0.08, 0.07, 0.06])

    out = np.stack([
        paper_r * (1 - binary_noisy) + ink[0] * binary_noisy,
        paper_g * (1 - binary_noisy) + ink[1] * binary_noisy,
        paper_b * (1 - binary_noisy) + ink[2] * binary_noisy,
    ], axis=2)

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v16(img):
    """Brutalist Duotone – exactly 2 harsh colours, flat and uncompromising."""
    w, h = img.size
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Hard threshold (no anti-aliasing)
    binary = (gray > 0.48).astype(float)

    # Colour pair: acid yellow + deep charcoal
    col_dark  = np.array([0.08, 0.08, 0.09])
    col_light = np.array([0.98, 0.95, 0.02])

    out = np.zeros((h, w, 3), dtype=np.float32)
    for c in range(3):
        out[:, :, c] = binary * col_light[c] + (1 - binary) * col_dark[c]

    # Very slight halftone noise in the light areas to avoid total flatness
    rng = np.random.default_rng(16)
    dot_noise = (rng.random((h, w)) < gray * 0.15).astype(float)
    for c in range(3):
        out[:, :, c] = np.clip(out[:, :, c] - dot_noise * col_light[c] * 0.3 * binary, 0, 1)

    return Image.fromarray((out * 255).astype(np.uint8))


def apply_v17(img):
    """CMYK Halftone Separation – four-colour dot screens, slightly misregistered."""
    w, h = img.size
    arr = np.array(img, dtype=np.float32) / 255.0
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

    # RGB → CMY → K
    C = 1 - r
    M = 1 - g
    Y = 1 - b
    K = np.minimum(np.minimum(C, M), Y)
    C = np.clip((C - K) / (1 - K + 1e-9), 0, 1)
    M = np.clip((M - K) / (1 - K + 1e-9), 0, 1)
    Y = np.clip((Y - K) / (1 - K + 1e-9), 0, 1)

    import math
    def halftone_ch(ch, angle_deg, dot=8, shift=(0, 0)):
        a = math.radians(angle_deg)
        ca, sa = math.cos(a), math.sin(a)
        yy, xx = np.mgrid[0:h, 0:w]
        rx = (xx + shift[0]) * ca + (yy + shift[1]) * sa
        ry = -(xx + shift[0]) * sa + (yy + shift[1]) * ca
        gx = (rx % dot) - dot / 2
        gy = (ry % dot) - dot / 2
        dist = np.sqrt(gx ** 2 + gy ** 2)
        radius = gaussian_filter(ch, 1) * dot * 0.62
        return (dist < radius).astype(np.float32)

    Cscreen = halftone_ch(C, 15)
    Mscreen = halftone_ch(M, 75, shift=(3, 2))
    Yscreen = halftone_ch(Y,  0, shift=(1, 4))
    Kscreen = halftone_ch(K, 45, shift=(5, 1))

    # White paper background
    out_r = np.ones((h, w))
    out_g = np.ones((h, w))
    out_b = np.ones((h, w))

    # Subtract ink layers
    out_r = out_r - Cscreen * 0.90 - Kscreen * 0.95
    out_g = out_g - Mscreen * 0.88 - Kscreen * 0.95
    out_b = out_b - Yscreen * 0.88 - Kscreen * 0.95

    return Image.fromarray((np.clip(np.stack([out_r, out_g, out_b], axis=2), 0, 1) * 255).astype(np.uint8))


def apply_v18(img):
    """Terminal Matrix – ASCII character-grid rendering in phosphor green."""
    w, h = img.size
    CSIZE = 8  # character cell size in pixels

    cw, ch = w // CSIZE, h // CSIZE
    small = img.resize((cw, ch), Image.LANCZOS).convert('L')
    luma = np.array(small, dtype=np.float32) / 255.0

    # Black background
    out = np.zeros((h, w, 3), dtype=np.float32)

    # Phosphor green palette
    def get_green(intensity):
        return np.array([intensity * 0.05, intensity * 1.0, intensity * 0.25])

    # ASCII density chars (from darkest to brightest): . : ; i l ! I ; = + x X $ & #
    char_patterns = [
        # Each pattern: 8x8 binary grid (True = lit pixel)
        # Approximations using math
    ]

    yy, xx = np.mgrid[0:CSIZE, 0:CSIZE]
    # Generate pixel patterns for ~16 brightness levels
    patterns = {}
    for level in range(16):
        t = level / 15.0
        density = t
        # Different "character" shapes based on density
        if level == 0:
            pat = np.zeros((CSIZE, CSIZE), bool)
        elif level < 3:
            # Dot: just center pixel
            pat = np.zeros((CSIZE, CSIZE), bool)
            pat[CSIZE//2, CSIZE//2] = True
            pat[CSIZE//2-1, CSIZE//2] = True
        elif level < 6:
            # Colon/period: vertical dots
            pat = np.zeros((CSIZE, CSIZE), bool)
            pat[2, CSIZE//2-1:CSIZE//2+1] = True
            pat[5, CSIZE//2-1:CSIZE//2+1] = True
        elif level < 9:
            # Plus / cross
            pat = np.zeros((CSIZE, CSIZE), bool)
            pat[CSIZE//2, :] = True
            pat[:, CSIZE//2] = True
        elif level < 12:
            # X marks
            pat = np.zeros((CSIZE, CSIZE), bool)
            for i in range(CSIZE):
                pat[i, i] = True
                pat[i, CSIZE-1-i] = True
        elif level < 14:
            # Hash dense
            pat = np.zeros((CSIZE, CSIZE), bool)
            pat[1::3, :] = True
            pat[:, 1::3] = True
        else:
            # Full block
            pat = np.ones((CSIZE, CSIZE), bool)
        patterns[level] = pat

    for cy_i in range(ch):
        for cx_i in range(cw):
            val = luma[cy_i, cx_i]
            level = min(int(val * 15), 15)
            pat = patterns[level]
            py = cy_i * CSIZE
            px = cx_i * CSIZE
            # Phosphor glow on lit pixels
            glow = gaussian_filter(pat.astype(float), sigma=0.8) * val
            out[py:py+CSIZE, px:px+CSIZE, 0] = glow * 0.05
            out[py:py+CSIZE, px:px+CSIZE, 1] = glow * 1.00
            out[py:py+CSIZE, px:px+CSIZE, 2] = glow * 0.28

    # CRT scanline overlay
    out[::2] *= 0.80
    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v19(img):
    """Byzantine Mosaic – chunky tesserae tiles with gold grout."""
    w, h = img.size
    TILE = 14  # tile size in pixels
    GAP  = 2   # grout gap

    tw, th = w // TILE, h // TILE
    small = img.resize((tw, th), Image.LANCZOS)
    colors = np.array(small, dtype=np.float32) / 255.0

    # Gold grout background
    out = np.ones((h, w, 3), dtype=np.float32) * [0.62, 0.50, 0.15]

    rng = np.random.default_rng(19)

    for ty in range(th):
        for tx in range(tw):
            col = colors[ty, tx].copy()
            # Slight random brightness variation per tile (mosaic irregularity)
            brightness = 1.0 + rng.uniform(-0.12, 0.12)
            col = np.clip(col * brightness, 0, 1)

            py = ty * TILE + GAP
            px = tx * TILE + GAP
            ey = min(py + TILE - GAP * 2, h)
            ex = min(px + TILE - GAP * 2, w)

            if py < h and px < w:
                out[py:ey, px:ex] = col
                # Slight edge shading on each tile (bevel)
                if ey > py and ex > px:
                    out[py, px:ex] = np.clip(col * 1.25, 0, 1)   # top edge lighter
                    out[py:ey, px] = np.clip(col * 1.20, 0, 1)   # left edge lighter
                    out[min(ey-1, h-1), px:ex] = col * 0.65      # bottom darker
                    out[py:ey, min(ex-1, w-1)] = col * 0.70      # right darker

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v20(img):
    """Prussian Cyanotype – contact-print in iron-blue on rough paper."""
    w, h = img.size
    rng = np.random.default_rng(20)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Boost contrast (contact prints are high-contrast)
    gray = np.clip((gray - 0.3) * 1.6 + 0.3, 0, 1)

    # Prussian blue LUT: deep blue → pale sky
    r = np.interp(gray, [0, 0.25, 0.65, 1.0], [0.00, 0.02, 0.22, 0.82])
    g = np.interp(gray, [0, 0.25, 0.65, 1.0], [0.04, 0.12, 0.48, 0.88])
    b = np.interp(gray, [0, 0.25, 0.65, 1.0], [0.18, 0.38, 0.78, 0.96])

    # Rough watercolour paper texture
    tx = rng.normal(0, 1, (h, w))
    tx = gaussian_filter(tx, sigma=2.5) * 0.5 + rng.normal(0, 0.5, (h, w)) * 0.5
    tx = (tx - tx.min()) / (tx.max() - tx.min()) * 0.06 - 0.03
    r = np.clip(r + tx, 0, 1)
    g = np.clip(g + tx, 0, 1)
    b = np.clip(b + tx * 0.5, 0, 1)

    # Slight vignette
    yy, xx = np.mgrid[0:h, 0:w]
    vig = np.clip(1.0 - ((xx / w - 0.5)**2 + (yy / h - 0.5)**2) * 0.8, 0.6, 1.0)
    r *= vig; g *= vig; b *= vig

    return Image.fromarray((np.clip(np.stack([r, g, b], axis=2), 0, 1) * 255).astype(np.uint8))


def apply_v21(img):
    """Holographic Foil – iridescent rainbow shift driven by surface gradient."""
    w, h = img.size
    arr = np.array(img, dtype=np.float32) / 255.0
    gray = np.mean(arr, axis=2)

    # Gradient magnitude drives hue rotation amount
    gy = np.gradient(gray, axis=0)
    gx = np.gradient(gray, axis=1)
    grad_mag = np.sqrt(gx**2 + gy**2)
    grad_mag = np.clip(grad_mag * 8, 0, 1)

    # Gradient direction drives hue shift direction
    grad_dir = np.arctan2(gy, gx)  # -π to π

    # Smooth base luminance for the foil
    luma = gaussian_filter(gray, sigma=2)

    # Convert image to HSV-like for hue rotation
    from PIL import Image as PilImg
    hsv_img = img.convert('HSV')
    hsv = np.array(hsv_img, dtype=np.float32)

    # Rainbow: hue shifts based on gradient direction + luminance position
    hue_shift = (grad_dir / (2 * np.pi) * 255 +
                 luma * 80 +
                 grad_mag * 60)
    hsv[:, :, 0] = (hsv[:, :, 0] + hue_shift) % 256
    # Boost saturation where gradient is high
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * (1 + grad_mag * 2.5), 0, 255)
    # Boost value slightly
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.15, 0, 255)

    result = PilImg.fromarray(hsv.astype(np.uint8), 'HSV').convert('RGB')
    # Blend with a metallic sheen
    result_arr = np.array(result, dtype=np.float32) / 255.0
    # Metallic: add white highlight where gradient is very high
    white_mask = gaussian_filter(grad_mag, sigma=1) * 0.35
    result_arr = np.clip(result_arr + white_mask[:, :, np.newaxis], 0, 1)
    return Image.fromarray((result_arr * 255).astype(np.uint8))


def apply_v22(img):
    """Copper Plate Etching – variable-density crosshatch on cream paper."""
    w, h = img.size
    rng = np.random.default_rng(22)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0
    # Invert: dark original = more hatching
    density = 1 - gray

    out = np.ones((h, w), dtype=np.float32)  # white paper

    # Fine hatching at 30°: line spacing varies with density
    # Use continuous wave approach: sin wave with frequency ~ density
    yy, xx = np.mgrid[0:h, 0:w].astype(float)

    # Direction 1: 30° lines
    proj1 = xx * np.cos(np.radians(30)) + yy * np.sin(np.radians(30))
    # Direction 2: 120° lines (crosshatch)
    proj2 = xx * np.cos(np.radians(120)) + yy * np.sin(np.radians(120))

    for proj, weight in [(proj1, 1.0), (proj2, 0.7)]:
        # Line spacing: dark areas have tight spacing (4px), light areas sparse (20px)
        spacing = np.clip(20 - density * 16, 4, 20)
        # Each pixel: how far from nearest hatch line?
        pos_in_cell = proj % spacing
        # Normalize to 0..1 within cell
        norm_pos = pos_in_cell / spacing
        # Line width ~1.2 pixels
        line_mask = (norm_pos < 1.2 / spacing) | (norm_pos > 1 - 0.6 / spacing)
        # Only draw where density is high enough
        draw_mask = (density > 0.15 * weight).astype(float)
        # Fade line darkness with density
        line_darkness = line_mask.astype(float) * density * 0.8 * weight
        out -= line_darkness * draw_mask

    out = np.clip(out, 0, 1)

    # Warm sepia tint (cream paper + brown ink)
    r = np.clip(out * 0.96 + 0.02, 0, 1)
    g = np.clip(out * 0.90, 0, 1)
    b = np.clip(out * 0.78, 0, 1)

    # Paper grain
    grain = rng.normal(0, 0.010, (h, w))
    r = np.clip(r + grain, 0, 1)
    g = np.clip(g + grain * 0.9, 0, 1)
    b = np.clip(b + grain * 0.8, 0, 1)

    return Image.fromarray((np.stack([r, g, b], axis=2) * 255).astype(np.uint8))


def apply_v23(img):
    """Solarized Dream – Sabattier effect with psychedelic colour inversion."""
    w, h = img.size
    arr = np.array(img, dtype=np.float32) / 255.0

    # Boost saturation first for more vivid solarization
    pil = ImageEnhance.Color(img).enhance(2.0)
    arr = np.array(pil, dtype=np.float32) / 255.0

    # Apply Sabattier (solarization) at different thresholds per channel
    thresholds = [0.55, 0.45, 0.50]
    out = arr.copy()
    for c, thresh in enumerate(thresholds):
        ch = arr[:, :, c]
        out[:, :, c] = np.where(ch > thresh, 1.0 - ch, ch)

    # Smooth the inversion boundary
    out = gaussian_filter(out, sigma=[0.8, 0.8, 0])

    # Psychedelic hue boost: exaggerate colour differences
    pil_out = Image.fromarray((out * 255).astype(np.uint8))
    pil_out = ImageEnhance.Color(pil_out).enhance(2.5)
    pil_out = ImageEnhance.Contrast(pil_out).enhance(1.3)
    out = np.array(pil_out, dtype=np.float32) / 255.0

    # Add slight Gaussian blur for dreamy quality
    out = gaussian_filter(out, sigma=[1.5, 1.5, 0])

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v24(img):
    """Charcoal on Kraft – raw charcoal marks on warm brown paper."""
    w, h = img.size
    rng = np.random.default_rng(24)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0
    arr = np.array(img, dtype=np.float32) / 255.0

    # Kraft paper base: warm brown
    kr = 0.58 + rng.normal(0, 0.025, (h, w))
    kg = 0.44 + rng.normal(0, 0.025, (h, w))
    kb = 0.28 + rng.normal(0, 0.020, (h, w))

    # Charcoal marks: based on dark areas of the image
    # Directional smear (simulate charcoal stick direction)
    dark_mask = 1.0 - gray  # brighter = more charcoal

    # Smear horizontally and at slight angle
    smear_h = gaussian_filter(dark_mask, sigma=[0.5, 3.0])
    smear_d = gaussian_filter(dark_mask, sigma=[1.5, 1.5])
    charcoal = smear_h * 0.6 + smear_d * 0.4
    charcoal = np.clip(charcoal * 1.4, 0, 1)

    # Random pigment clumps (charcoal is lumpy)
    clumps = (rng.random((h, w)) < dark_mask * 0.30).astype(float)
    clumps = gaussian_filter(clumps, sigma=1.0) * 0.35
    charcoal = np.clip(charcoal + clumps, 0, 1)

    # Charcoal colour: near black with slight blue-grey
    ck_r, ck_g, ck_b = 0.12, 0.13, 0.16

    # Kraft paper picks up charcoal colour slightly (warm undertone)
    out_r = kr * (1 - charcoal * 0.90) + ck_r * charcoal
    out_g = kg * (1 - charcoal * 0.92) + ck_g * charcoal
    out_b = kb * (1 - charcoal * 0.88) + ck_b * charcoal

    # Paper fibres
    fibres = rng.normal(0, 0.5, (h, w))
    fibres = gaussian_filter(fibres, sigma=[0.3, 3]) * 0.018
    out_r = np.clip(out_r + fibres, 0, 1)
    out_g = np.clip(out_g + fibres * 0.9, 0, 1)
    out_b = np.clip(out_b + fibres * 0.7, 0, 1)

    return Image.fromarray((np.stack([out_r, out_g, out_b], axis=2) * 255).astype(np.uint8))


def apply_v25(img):
    """Pop Art Screen – Warhol flat colours with Ben-Day dots."""
    w, h = img.size
    rng = np.random.default_rng(25)

    # Quantize to 5 bold colours
    small = img.resize((w // 4, h // 4), Image.LANCZOS)
    quantized = small.quantize(colors=5, method=Image.Quantize.FASTOCTREE)
    quantized = quantized.convert('RGB').resize((w, h), Image.NEAREST)
    qarr = np.array(quantized, dtype=np.float32) / 255.0

    # Remap each cluster to a bold pop-art colour
    bold_colors = [
        [0.98, 0.06, 0.45],  # hot pink
        [0.06, 0.38, 0.88],  # electric blue
        [0.99, 0.88, 0.02],  # acid yellow
        [0.02, 0.75, 0.40],  # vivid green
        [0.95, 0.30, 0.08],  # orange-red
    ]

    # Posterize into flat regions
    pil_q = ImageEnhance.Color(quantized).enhance(3.0)
    pil_q = ImageEnhance.Contrast(pil_q).enhance(2.0)
    arr = np.array(pil_q, dtype=np.float32) / 255.0

    # Ben-Day dots (regular dot grid at ~45°)
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    dot_size = 7
    a = np.radians(45)
    rx = xx * np.cos(a) + yy * np.sin(a)
    ry = -xx * np.sin(a) + yy * np.cos(a)
    gx_d = (rx % dot_size) - dot_size / 2
    gy_d = (ry % dot_size) - dot_size / 2
    dist_d = np.sqrt(gx_d**2 + gy_d**2)
    # Dots proportional to luminance
    luma = np.mean(arr, axis=2)
    dot_radius = luma * dot_size * 0.52
    dot_mask = (dist_d < dot_radius).astype(float)

    # White paper base
    out = np.ones((h, w, 3))
    # Fill dots with the image colour
    for c in range(3):
        out[:, :, c] = 1.0 - dot_mask * (1.0 - arr[:, :, c])

    # Black outlines
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0
    pil_g = img.convert('L').filter(ImageFilter.FIND_EDGES)
    edges = np.array(pil_g, dtype=np.float32) / 255.0
    edges = np.clip(edges * 3, 0, 1)
    edge_thresh = (edges > 0.25).astype(float)
    edge_thick = gaussian_filter(edge_thresh, sigma=0.8)
    for c in range(3):
        out[:, :, c] = np.clip(out[:, :, c] - edge_thick * 0.85, 0, 1)

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


def apply_v26(img):
    """Arctic Crystal – frost ice patterns on cold blue-white palette."""
    w, h = img.size
    rng = np.random.default_rng(26)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Cold blue-white base palette
    r_base = np.interp(gray, [0, 0.3, 0.7, 1.0], [0.05, 0.20, 0.62, 0.92])
    g_base = np.interp(gray, [0, 0.3, 0.7, 1.0], [0.10, 0.35, 0.78, 0.96])
    b_base = np.interp(gray, [0, 0.3, 0.7, 1.0], [0.28, 0.60, 0.92, 1.00])

    # Crystal frost pattern: Voronoi-like using distance to random seeds
    n_seeds = 180
    sx = rng.integers(0, w, n_seeds).astype(float)
    sy = rng.integers(0, h, n_seeds).astype(float)

    yy, xx = np.mgrid[0:h, 0:w].astype(float)

    # For each pixel, distance to nearest 2 seeds
    dist_grid = np.full((h, w), np.inf)
    dist2_grid = np.full((h, w), np.inf)
    for i in range(n_seeds):
        d = np.sqrt((xx - sx[i])**2 + (yy - sy[i])**2)
        mask = d < dist_grid
        dist2_grid = np.where(mask, dist_grid, np.minimum(dist2_grid, d))
        dist_grid = np.where(mask, d, dist_grid)

    # Crystal edge = boundary between cells (small dist2 - dist1)
    edge_width = dist2_grid - dist_grid
    crystal_edge = np.clip(1 - edge_width / 6, 0, 1) ** 2

    # Sparkle at crystal vertices (where edge_width is very small)
    sparkle = (edge_width < 2).astype(float) * 0.6

    # Overlay frost on image
    frost_intensity = crystal_edge * 0.55 + sparkle
    r = np.clip(r_base * (1 - frost_intensity * 0.4) + frost_intensity * 0.88, 0, 1)
    g = np.clip(g_base * (1 - frost_intensity * 0.3) + frost_intensity * 0.94, 0, 1)
    b = np.clip(b_base * (1 - frost_intensity * 0.1) + frost_intensity * 1.00, 0, 1)

    # Ice grain
    grain = rng.normal(0, 0.012, (h, w))
    r = np.clip(r + grain, 0, 1)
    g = np.clip(g + grain, 0, 1)
    b = np.clip(b + grain * 0.5, 0, 1)

    return Image.fromarray((np.stack([r, g, b], axis=2) * 255).astype(np.uint8))


def apply_v27(img):
    """Noir Rain – film noir darkness with neon street-light reflections."""
    w, h = img.size
    rng = np.random.default_rng(27)
    arr = np.array(img, dtype=np.float32) / 255.0

    # Desaturate heavily and darken (noir)
    gray = np.mean(arr, axis=2, keepdims=True)
    noir = arr * 0.15 + gray * 0.85
    # Darken overall – noir lives in shadow
    noir = np.clip(noir * 0.6, 0, 1)
    # High contrast S-curve
    noir = np.where(noir < 0.4, noir * 0.5, 1 - (1 - noir)**1.5 * 0.7)

    # Film grain
    grain = rng.normal(0, 0.025, (h, w, 3))
    noir = np.clip(noir + grain, 0, 1)

    # Rain streaks (vertical with slight diagonal drift)
    rain_layer = np.zeros((h, w, 3), dtype=np.float32)
    n_drops = rng.integers(300, 600)
    for _ in range(n_drops):
        x = rng.integers(0, w)
        y_start = rng.integers(0, h // 2)
        length = rng.integers(15, 60)
        brightness = rng.uniform(0.3, 0.9)
        drift = rng.integers(-2, 3)
        for l in range(length):
            yy = y_start + l
            xx = x + int(l * drift / max(length, 1))
            if 0 <= yy < h and 0 <= xx < w:
                alpha = brightness * (1 - l / length) ** 0.5
                rain_layer[yy, xx] = np.clip([alpha] * 3, 0, 1)
    rain_layer = gaussian_filter(rain_layer, sigma=[0.4, 0.2, 0])

    # Neon reflections: coloured patches (pink, teal, amber, blue)
    neon_colors = [
        ([0.98, 0.05, 0.55], rng.integers(20, w-20), rng.integers(h//2, h-20)),
        ([0.05, 0.90, 0.88], rng.integers(20, w-20), rng.integers(h//2, h-20)),
        ([0.98, 0.65, 0.05], rng.integers(20, w-20), rng.integers(h//2, h-20)),
        ([0.15, 0.35, 0.95], rng.integers(20, w-20), rng.integers(h//2, h-20)),
    ]
    neon_layer = np.zeros((h, w, 3), dtype=np.float32)
    for col, nx, ny in neon_colors:
        blob = np.zeros((h, w))
        blob[ny, nx] = 1.0
        blob = gaussian_filter(blob, sigma=rng.uniform(20, 45)) * rng.uniform(0.4, 0.9)
        for c in range(3):
            neon_layer[:, :, c] += blob * col[c]
    neon_layer = np.clip(neon_layer, 0, 0.6)

    out = np.clip(noir + rain_layer * 0.7 + neon_layer * 0.55, 0, 1)
    return Image.fromarray((out * 255).astype(np.uint8))


def apply_v28(img):
    """Iron & Rust – oxidized metal with corrosion texture and decay."""
    w, h = img.size
    rng = np.random.default_rng(28)
    gray = np.array(img.convert('L'), dtype=np.float32) / 255.0

    # Rust colormap: near-black → dark rust → burnt orange → ochre → cream
    stops_t = [0.0,  0.18, 0.38, 0.58, 0.78, 1.0]
    stops_r  = [0.08, 0.32, 0.62, 0.78, 0.88, 0.94]
    stops_g  = [0.05, 0.12, 0.22, 0.38, 0.58, 0.78]
    stops_b  = [0.03, 0.05, 0.06, 0.10, 0.24, 0.52]

    r = np.interp(gray, stops_t, stops_r)
    g = np.interp(gray, stops_t, stops_g)
    b = np.interp(gray, stops_t, stops_b)

    # Multi-scale corrosion noise
    def corrosion_noise(scale, sigma):
        n = rng.normal(0, 1, (h // scale + 1, w // scale + 1))
        n_up = np.array(Image.fromarray(n).resize((w, h), Image.BILINEAR))
        return gaussian_filter(n_up, sigma=sigma)

    c1 = corrosion_noise(1, 2)
    c2 = corrosion_noise(4, 6)
    c3 = corrosion_noise(16, 12)
    corr = c1 * 0.4 + c2 * 0.35 + c3 * 0.25
    corr = (corr - corr.min()) / (corr.max() - corr.min()) - 0.5
    corr *= 0.22

    r = np.clip(r + corr * 1.2, 0, 1)
    g = np.clip(g + corr * 0.6, 0, 1)
    b = np.clip(b + corr * 0.2, 0, 1)

    # Pitting: random dark spots (oxidation holes)
    pits = (rng.random((h, w)) < 0.004).astype(float)
    pits = gaussian_filter(pits, sigma=2) * 8
    pits = np.clip(pits, 0, 0.85)
    r = np.clip(r - pits * 0.7, 0, 1)
    g = np.clip(g - pits * 0.5, 0, 1)
    b = np.clip(b - pits * 0.3, 0, 1)

    # Metal grain (fine horizontal striations)
    stripe = rng.normal(0, 0.5, (h, w))
    stripe = gaussian_filter(stripe, sigma=[0.5, 3]) * 0.030
    r = np.clip(r + stripe, 0, 1)
    g = np.clip(g + stripe * 0.7, 0, 1)
    b = np.clip(b + stripe * 0.3, 0, 1)

    return Image.fromarray((np.stack([r, g, b], axis=2) * 255).astype(np.uint8))


def apply_v29(img):
    """Pointillist Garden – Seurat-style broken-colour dot painting."""
    w, h = img.size
    rng = np.random.default_rng(29)
    arr = np.array(img, dtype=np.float32) / 255.0
    luma = np.mean(arr, axis=2)

    DOT_RADIUS_MAX = 5
    n_dots = w * h // (DOT_RADIUS_MAX ** 2)

    ys = rng.integers(0, h, n_dots)
    xs = rng.integers(0, w, n_dots)

    # Sort dark dots first (light dots on top)
    dot_luma = luma[ys, xs]
    sort_idx = np.argsort(dot_luma)[::-1]
    ys, xs = ys[sort_idx], xs[sort_idx]

    # Pre-batch random neighbourhood offsets
    dy_off = rng.integers(-2, 3, n_dots)
    dx_off = rng.integers(-2, 3, n_dots)
    sample_ys = np.clip(ys + dy_off, 0, h - 1)
    sample_xs = np.clip(xs + dx_off, 0, w - 1)

    # Use PIL ImageDraw for fast dot rendering
    canvas = Image.new('RGB', (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)

    for i in range(n_dots):
        y0, x0 = int(ys[i]), int(xs[i])
        col = arr[sample_ys[i], sample_xs[i]].copy()
        col = np.clip((col - 0.5) * 1.4 + 0.5, 0, 1)
        col_int = (int(col[0]*255), int(col[1]*255), int(col[2]*255))
        dot_l = luma[y0, x0]
        radius = int(DOT_RADIUS_MAX * (0.5 + (1 - dot_l) * 0.5))
        r = max(radius, 1)
        draw.ellipse([x0 - r, y0 - r, x0 + r, y0 + r], fill=col_int)

    return canvas


def apply_v30(img):
    """Origami Fold – angular faceted paper geometry with crease shadows."""
    w, h = img.size
    rng = np.random.default_rng(30)
    arr = np.array(img, dtype=np.float32) / 255.0

    # Generate triangular facets using random Delaunay-like triangulation
    # Simplified: use a grid of triangles with jittered vertices
    GRID = 20  # grid cells
    gw = w // GRID
    gh = h // GRID

    # Jittered grid points
    pts_x = np.zeros((GRID + 1, GRID + 1))
    pts_y = np.zeros((GRID + 1, GRID + 1))
    for gy in range(GRID + 1):
        for gx in range(GRID + 1):
            pts_x[gy, gx] = gx * gw + rng.integers(-gw // 4, gw // 4 + 1)
            pts_y[gy, gx] = gy * gh + rng.integers(-gh // 4, gh // 4 + 1)
    pts_x = np.clip(pts_x, 0, w - 1)
    pts_y = np.clip(pts_y, 0, h - 1)

    # Paper base: flat white-cream
    out = np.ones((h, w, 3), dtype=np.float32) * [0.97, 0.96, 0.93]

    # For each grid quad, split into 2 triangles
    # Fill each triangle with the average colour from the original image + fold shading
    def fill_triangle(p0, p1, p2, color, fold_bright):
        """Rasterize a triangle."""
        xs = [p0[0], p1[0], p2[0]]
        ys = [p0[1], p1[1], p2[1]]
        min_x = max(int(min(xs)) - 1, 0)
        max_x = min(int(max(xs)) + 2, w)
        min_y = max(int(min(ys)) - 1, 0)
        max_y = min(int(max(ys)) + 2, h)

        # Barycentric coordinates
        yy_r, xx_r = np.mgrid[min_y:max_y, min_x:max_x].astype(float)
        v0 = (p1[0] - p0[0], p1[1] - p0[1])
        v1 = (p2[0] - p0[0], p2[1] - p0[1])
        v2_x = xx_r - p0[0]
        v2_y = yy_r - p0[1]
        dot00 = v0[0]*v0[0] + v0[1]*v0[1]
        dot01 = v0[0]*v1[0] + v0[1]*v1[1]
        dot11 = v1[0]*v1[0] + v1[1]*v1[1]
        dot02 = v0[0]*v2_x + v0[1]*v2_y
        dot12 = v1[0]*v2_x + v1[1]*v2_y
        inv = 1.0 / (dot00 * dot11 - dot01 * dot01 + 1e-10)
        u = (dot11 * dot02 - dot01 * dot12) * inv
        v = (dot00 * dot12 - dot01 * dot02) * inv
        inside = (u >= 0) & (v >= 0) & (u + v <= 1)

        shaded = np.clip(color * fold_bright, 0, 1)
        out[min_y:max_y, min_x:max_x][inside] = shaded

    for gy in range(GRID):
        for gx in range(GRID):
            # 4 corners of the grid cell
            tl = (pts_x[gy,   gx],   pts_y[gy,   gx])
            tr = (pts_x[gy,   gx+1], pts_y[gy,   gx+1])
            bl = (pts_x[gy+1, gx],   pts_y[gy+1, gx])
            br = (pts_x[gy+1, gx+1], pts_y[gy+1, gx+1])

            # Sample average colour from original image for this cell
            sy = int(np.clip((gy + 0.5) * gh, 0, h-1))
            sx = int(np.clip((gx + 0.5) * gw, 0, w-1))
            base_col = arr[sy, sx].copy()

            # Fold shading: random light direction creates angular facets
            bright1 = rng.uniform(0.72, 1.15)
            bright2 = rng.uniform(0.72, 1.15)

            # Triangle 1: top-left, top-right, bottom-left
            fill_triangle(tl, tr, bl, base_col, bright1)
            # Triangle 2: top-right, bottom-right, bottom-left
            fill_triangle(tr, br, bl, base_col, bright2)

    # Crease shadow lines: draw thin dark lines along the grid edges
    for gy in range(GRID + 1):
        for gx in range(GRID):
            x0 = int(pts_x[gy, gx])
            y0 = int(pts_y[gy, gx])
            x1 = int(pts_x[gy, gx+1])
            y1 = int(pts_y[gy, gx+1])
            # Draw a thin dark line between adjacent grid points
            steps = max(abs(x1-x0), abs(y1-y0)) + 1
            for t_i in range(steps):
                t = t_i / max(steps - 1, 1)
                px = int(x0 + (x1 - x0) * t)
                py = int(y0 + (y1 - y0) * t)
                if 0 <= py < h and 0 <= px < w:
                    out[py, px] *= 0.68
    for gx in range(GRID + 1):
        for gy in range(GRID):
            x0 = int(pts_x[gy, gx])
            y0 = int(pts_y[gy, gx])
            x1 = int(pts_x[gy+1, gx])
            y1 = int(pts_y[gy+1, gx])
            steps = max(abs(x1-x0), abs(y1-y0)) + 1
            for t_i in range(steps):
                t = t_i / max(steps - 1, 1)
                px = int(x0 + (x1 - x0) * t)
                py = int(y0 + (y1 - y0) * t)
                if 0 <= py < h and 0 <= px < w:
                    out[py, px] *= 0.68

    # Smooth crease lines slightly and add paper texture
    out = gaussian_filter(out, sigma=[0.4, 0.4, 0])
    rng2 = np.random.default_rng(301)
    out += rng2.normal(0, 0.008, (h, w, 3))

    return Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8))


# =============================================================================
# METADATA: name, short description
# =============================================================================

FILTER_META = {
    4:  ("Risograph Reverie",      "Two-colour halftone risograph print with misregistered coral + teal channels on cream paper"),
    5:  ("Silver Daguerreotype",   "Antique silver-plate photograph with S-curve toning, metallic grain, and oval vignette"),
    6:  ("Synthwave Horizon",      "1980s vaporwave with purple-to-pink gradient, perspective floor grid, scanlines, and chromatic aberration"),
    7:  ("Impasto Storm",          "Thick oil-paint brushstroke texture with palette-knife smears and rich saturated colour"),
    8:  ("Graphite Study",         "Pencil sketch with variable crosshatching on textured cream paper"),
    9:  ("Watercolor Bloom",       "Wet-on-wet watercolour with pigment bleeds, dried-edge darkening, and paper granulation"),
    10: ("Cross-Stitch Canvas",    "Hand embroidery X-stitch pattern on linen background with woven fabric texture"),
    11: ("Cathedral Glass",        "Stained glass with bold flat colour regions, dark lead came borders, and backlit glow"),
    12: ("Signal Corrupted",       "Digital glitch with scan-line displacement, RGB bleed, block corruption, and neon noise"),
    13: ("Verdigris Antiquity",    "Oxidized copper patina with multi-scale corrosion texture and metallic highlight"),
    14: ("Infrared Reverie",       "Infrared film photography with glowing whites, darkened blues, and highlight halation bloom"),
    15: ("Linocut Bold",           "Stark linocut relief print in black ink on off-white paper, morphologically cleaned"),
    16: ("Brutalist Duotone",      "Hard two-colour duotone in acid yellow and charcoal – flat, uncompromising, Bauhaus"),
    17: ("CMYK Separation",        "Four-colour halftone dot screens (C/M/Y/K) at different angles with slight misregistration"),
    18: ("Terminal Matrix",        "ASCII character-cell rendering in phosphor green on black CRT terminal"),
    19: ("Byzantine Mosaic",       "Chunky tesserae tiles with gold grout lines and random brightness variation"),
    20: ("Prussian Cyanotype",     "Iron-salt cyanotype contact print in prussian blue on rough watercolour paper"),
    21: ("Holographic Foil",       "Iridescent rainbow hue shifts driven by surface gradient – metallic foil effect"),
    22: ("Copper Plate Etching",   "Variable-density crosshatch engraving lines on warm cream paper – fine intaglio print"),
    23: ("Solarized Dream",        "Sabattier solarization with per-channel thresholds and psychedelic colour boost"),
    24: ("Charcoal on Kraft",      "Directional charcoal marks on warm brown kraft paper with pigment clumps and fibre texture"),
    25: ("Pop Art Screen",         "Warhol-style flat colour quantization with Ben-Day dot overlay and bold black outlines"),
    26: ("Arctic Crystal",         "Voronoi frost/crystal pattern on cold blue-white palette with specular sparkle"),
    27: ("Noir Rain",              "Film noir darkness with vertical rain streaks and neon street-light colour reflections"),
    28: ("Iron & Rust",            "Oxidized metal with multi-scale corrosion texture, pitting decay, and horizontal grain striations"),
    29: ("Pointillist Garden",     "Seurat broken-colour dot painting with pure pigment dots of varying radius on white canvas"),
    30: ("Origami Fold",           "Jittered triangular facets with angular fold shading and crease shadow lines on cream paper"),
}


def make_readme(v, input_name, name, description):
    return f"""# Filter v{v}: {name}

## The Aesthetic

{description}.

## Input

Applied to `inputs/{input_name}.avif`.

## Technique

See `filter.sh` for the full multi-step recipe.

## Tools Used

- `ffmpeg` — AVIF decode
- Python 3 / Pillow / NumPy / SciPy / scikit-image
- Output: WebP (quality 75, method 6)
"""


def make_filter_sh(v, input_name, name):
    default_input = f"inputs/{input_name}.avif"
    return f"""#!/usr/bin/env bash
# Filter v{v}: {name}
# Apply with: bash filter.sh [input.avif]
set -e

INPUT="${{1:-{default_input}}}"
OUTPUT="$(dirname "$0")/output.webp"
TMP=$(mktemp /tmp/filter_v{v}_XXXXXX.png)

ffmpeg -y -i "$INPUT" "$TMP" 2>/dev/null

python3 - "$TMP" "$OUTPUT" <<'PYEOF'
import sys, os, math
import numpy as np
from PIL import Image, ImageFilter, ImageOps, ImageEnhance, ImageDraw
from scipy.ndimage import gaussian_filter, uniform_filter

src, dst = sys.argv[1], sys.argv[2]
img = Image.open(src).convert('RGB')

# ---- Filter v{v}: {name} ----
# Run: python3 generate_v4_v30.py  to regenerate all outputs.
# This script is auto-generated. For the full implementation see generate_v4_v30.py

import subprocess, importlib.util, tempfile, pathlib
gen = pathlib.Path(__file__).parent.parent.parent / 'generate_v4_v30.py'
spec = importlib.util.spec_from_file_location('gen', gen)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
result = mod.APPLY_FNS[{v}](img)
result.save(dst, 'WEBP', quality=75, method=6)
print(f'Saved: {{dst}}')
PYEOF

rm -f "$TMP"
echo "Done: $OUTPUT"
"""


# =============================================================================
# MAIN
# =============================================================================

APPLY_FNS = {
    4: apply_v4,   5: apply_v5,   6: apply_v6,   7: apply_v7,
    8: apply_v8,   9: apply_v9,  10: apply_v10,  11: apply_v11,
    12: apply_v12, 13: apply_v13, 14: apply_v14,  15: apply_v15,
    16: apply_v16, 17: apply_v17, 18: apply_v18,  19: apply_v19,
    20: apply_v20, 21: apply_v21, 22: apply_v22,  23: apply_v23,
    24: apply_v24, 25: apply_v25, 26: apply_v26,  27: apply_v27,
    28: apply_v28, 29: apply_v29, 30: apply_v30,
}


def main():
    versions = sorted(APPLY_FNS.keys())
    inputs_list = list(INPUTS.items())
    total = len(versions) * len(inputs_list)
    done = 0

    for v in versions:
        name, description = FILTER_META[v]
        fn = APPLY_FNS[v]
        print(f"\n=== v{v}: {name} ===")

        for iname, ipath in inputs_list:
            outdir = BASE / f'output/{iname}-claude-code-v{v}'
            outdir.mkdir(parents=True, exist_ok=True)

            print(f"  {iname}...", end=' ', flush=True)
            img = load_avif(ipath)
            result = fn(img)
            save_webp(result, outdir / 'output.webp')

            # Write README.md
            readme = make_readme(v, iname, name, description)
            (outdir / 'README.md').write_text(readme)

            # Write filter.sh
            sh = make_filter_sh(v, iname, name)
            sh_path = outdir / 'filter.sh'
            sh_path.write_text(sh)
            sh_path.chmod(sh_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP)

            done += 1
            print(f"done ({done}/{total})")

    print(f"\nAll {total} outputs generated.")


if __name__ == '__main__':
    main()
