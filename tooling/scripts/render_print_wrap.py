#!/usr/bin/env python3
"""Build the continuous 5x8 KDP paperback wrap and exact front-cover crop.

Geometry is locked to KDP's 82-page, black-and-white, cream-paper template.
The SVG is the editable master: one background spans back, spine, front, and bleed.
"""

from __future__ import annotations

import base64
import html
from pathlib import Path

import fitz


REPO = Path(__file__).resolve().parents[2]
BOOK = REPO / "books" / "spanish-graded-reader-a2"
FINAL = BOOK / "exports" / "cover" / "final"
BACKGROUND = BOOK / "assets" / "full-cover-background-02.jpeg"

SVG = FINAL / "print-wrap.svg"
GUIDES_SVG = FINAL / "print-wrap-guides.svg"
FRONT_SVG = FINAL / "front-cover.svg"
PDF = FINAL / "print-wrap.pdf"
PREVIEW = FINAL / "print-wrap-preview.png"
GUIDES_PREVIEW = FINAL / "print-wrap-guides-preview.png"
WRAP_PNG = FINAL / "print-wrap-300dpi.png"
KDP_PDF = BOOK / "exports" / "kdp" / "print-cover.pdf"
FRONT_PNG = FINAL / "front-cover.png"
FRONT_JPEG = FINAL / "front-cover.jpeg"
FRONT_THUMB = FINAL / "front-cover-100.png"
KDP_FRONT = BOOK / "exports" / "kdp" / "front-cover.jpeg"
DIRECT_FRONT = BOOK / "exports" / "direct" / "front-cover.jpeg"
CANVA_BACK_PDF = FINAL / "back-cover-canva.pdf"
CANVA_BACK_PNG = FINAL / "back-cover-canva-300dpi.png"
CANVA_FRONT_PDF = FINAL / "front-cover-canva.pdf"
CANVA_FRONT_PNG = FINAL / "front-cover-canva-300dpi.png"

# Exact template geometry, in millimetres.
WIDTH_MM = 265.56
HEIGHT_MM = 209.55
BLEED_MM = 3.175
BACK_FOLD_MM = 130.175
FRONT_FOLD_MM = 135.382
TRIM_WIDTH_MM = 127.0
TRIM_HEIGHT_MM = 203.2
TRIM_TOP_MM = 3.175
TRIM_BOTTOM_MM = 206.375


def jpeg_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def cover_content(image_uri: str) -> str:
    """Return the shared artwork used by both the wrap and front-crop SVGs."""
    return f"""
  <defs>
    <filter id="badgeShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="0.8" stdDeviation="1.1" flood-color="#071724" flood-opacity="0.30"/>
    </filter>
  </defs>

  <!-- A single image crosses back, both fold lines, spine, front, and all bleed. -->
  <image x="0" y="0" width="{WIDTH_MM}" height="{HEIGHT_MM}"
         preserveAspectRatio="xMidYMid slice" href="{image_uri}"/>

  <!-- Renderer-safe contrast veils; neither creates a boundary at a fold. -->
  <rect x="0" y="0" width="{BACK_FOLD_MM}" height="{HEIGHT_MM}"
        fill="#071724" fill-opacity="0.22"/>
  <rect x="{FRONT_FOLD_MM}" y="0" width="{WIDTH_MM - FRONT_FOLD_MM:.3f}" height="86"
        fill="#F4EBDD" fill-opacity="0.06"/>

  <!-- Back cover: every readable element is inside the downloaded template's white live area. -->
  <g id="back-copy" font-family="Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif">
    <text x="13" y="20" font-family="Didot, Palatino, Times New Roman, serif"
          font-size="6.2" font-weight="700" fill="#F4EBDD">
      <tspan x="13" dy="0">A letter no one will claim.</tspan>
      <tspan x="13" dy="7.2">A town that will not explain.</tspan>
    </text>
    <line x1="13" y1="40" x2="51" y2="40" stroke="#C9502B" stroke-width="1.1"/>

    <text x="13" y="51" font-size="3.65" fill="#F4EBDD">
      <tspan x="13" dy="0">Ana finds an unclaimed letter at the end of a quiet</tspan>
      <tspan x="13" dy="5.35">shift. Its addressee is a man nobody in Puerto Lento</tspan>
      <tspan x="13" dy="5.35">will discuss. To learn why, she must follow a name, an</tspan>
      <tspan x="13" dy="5.35">empty table, old letters, and a small light on the water.</tspan>
    </text>

    <text x="13" y="82" font-size="3.65" fill="#F4EBDD">
      <tspan x="13" dy="0">Ten linked stories return to the same people and places,</tspan>
      <tspan x="13" dy="5.35">giving adult A2 learners a narrative thread to follow</tspan>
      <tspan x="13" dy="5.35">instead of another disconnected language exercise.</tspan>
    </text>

    <text x="13" y="107" font-family="Snell Roundhand, Apple Chancery, Palatino, serif"
          font-size="5.1" font-weight="700" fill="#E7B38F">Open the letter. Follow Ana into the night.</text>
    <text x="13" y="116" font-size="3.2" font-weight="700" letter-spacing="0.7"
          fill="#F4EBDD">NINA MARLO</text>

    <text x="13" y="138.7" font-size="2.9" font-weight="700" letter-spacing="0.35"
          fill="#E7B38F">WHAT'S INSIDE</text>
    <g font-size="3.35" font-weight="650" fill="#F4EBDD">
      <circle cx="14.5" cy="147.4" r="1.45" fill="#2D9079"/>
      <text x="19" y="148.5">10 linked A2 stories</text>
      <circle cx="14.5" cy="156.7" r="1.45" fill="#2D9079"/>
      <text x="19" y="157.8">Complete English translations</text>
      <circle cx="14.5" cy="166" r="1.45" fill="#2D9079"/>
      <text x="19" y="167.1">Questions collected at the back</text>
    </g>
  </g>

  <!-- Spine: intentionally text-free. The scene itself continues across it. -->

  <!-- Front cover. Coordinates are measured from the official x=135.382 mm front fold. -->
  <g id="front-copy" font-family="Avenir Next, Avenir, Helvetica Neue, Arial, sans-serif">
    <text x="144.9" y="27.0" font-size="17.6" font-weight="800" letter-spacing="-0.5"
          fill="#C9502B">SPANISH</text>
    <text x="145.4" y="36.35" font-size="5.4" font-weight="700" letter-spacing="0.4"
          fill="#173753">GRADED READER FOR ADULTS</text>
    <rect x="238.55" y="11.43" width="14.92" height="10.0" rx="0.8"
          fill="#2D9079" filter="url(#badgeShadow)"/>
    <text x="241.0" y="18.55" font-size="6.5" font-weight="800" fill="#FFFFFF">A</text>
    <text x="247.1" y="18.55" font-size="6.5" font-weight="800" fill="#FFFFFF">2</text>
    <line x1="145.4" y1="42.2" x2="252.4" y2="42.2" stroke="#173753" stroke-width="0.72"/>

    <g id="book-title" fill="#173753">
      <text x="145.4" y="56.5" font-family="Snell Roundhand, Apple Chancery, Palatino, serif"
            font-size="11.9" font-weight="700">The Letter at</text>
      <text x="145.4" y="71.6" font-family="Didot, Palatino, Times New Roman, serif"
            font-size="12.1" font-weight="700" letter-spacing="0.35">PUERTO LENTO</text>
    </g>

    <text x="145.4" y="88.8" font-size="3.4" font-weight="700" letter-spacing="0.12"
          fill="#173753">TEN LINKED SPANISH STORIES</text>
    <text x="145.4" y="93.75" font-size="3.4" font-weight="700" letter-spacing="0.12"
          fill="#173753">A QUIET COASTAL MYSTERY</text>
    <line x1="145.4" y1="99.1" x2="197.3" y2="99.1" stroke="#C9502B" stroke-width="0.64"/>
    <text x="145.4" y="104.65" font-size="2.45" font-weight="700" letter-spacing="0.27"
          fill="#8E3C25">LATIN-AMERICAN SPANISH CONVENTION</text>
    <text x="145.4" y="116.1" font-size="4.13" font-weight="600" letter-spacing="0.63"
          fill="#173753">NINA MARLO</text>
  </g>

"""


def guide_content() -> str:
    """Visible overlay used only in the separate, explicitly review-only guide SVG."""
    return """
  <g id="kdp-guides" fill="none" vector-effect="non-scaling-stroke">
    <rect id="back-trim" x="3.175" y="3.175" width="127" height="203.2"
          stroke="#111" stroke-width="0.25"/>
    <rect id="front-trim" x="135.382" y="3.175" width="127" height="203.2"
          stroke="#111" stroke-width="0.25"/>
    <rect id="back-live-area" x="6.35" y="6.35" width="120.65" height="196.85"
          stroke="#00A870" stroke-width="0.35"/>
    <rect id="front-live-area" x="138.557" y="6.35" width="120.65" height="196.85"
          stroke="#00A870" stroke-width="0.35"/>
    <rect id="spine" x="130.175" y="3.175" width="5.207" height="203.2"
          stroke="#0066FF" stroke-width="0.25"/>
    <rect id="barcode-zone" x="73.025" y="169.545" width="50.8" height="30.48"
          stroke="#FFD400" stroke-width="0.35"/>
  </g>
"""


def svg_document(content: str, *, width: str, height: str, view_box: str,
                 title: str, description: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     width="{width}" height="{height}" viewBox="{view_box}"
     role="img" aria-labelledby="cover-title cover-desc">
  <title id="cover-title">{html.escape(title)}</title>
  <desc id="cover-desc">{html.escape(description)}</desc>{content}
</svg>
"""


def save_pdf_from_svg(svg_path: Path, pdf_path: Path) -> None:
    source = fitz.open(svg_path)
    converted = fitz.open("pdf", source.convert_to_pdf())
    converted.set_metadata({
        "title": "The Letter at Puerto Lento — paperback cover",
        "author": "Nina Marlo",
        "subject": "5x8 in, 82 production pages, cream paper",
        "creator": "ready-to-publish-books cover pipeline",
    })
    converted.save(pdf_path, garbage=4, deflate=True, clean=True)
    converted.close()
    source.close()


def crop_pdf(source: fitz.Document, destination: Path, clip: fitz.Rect,
             title: str, subject: str) -> None:
    out = fitz.open()
    page = out.new_page(width=clip.width, height=clip.height)
    page.show_pdf_page(page.rect, source, 0, clip=clip)
    out.set_metadata({
        "title": title,
        "author": "Nina Marlo",
        "subject": subject,
        "creator": "ready-to-publish-books cover pipeline",
    })
    out.save(destination, garbage=4, deflate=True, clean=True)
    out.close()


def render_png(pdf_path: Path, png_path: Path, width_px: int) -> fitz.Pixmap:
    doc = fitz.open(pdf_path)
    scale = width_px / doc[0].rect.width
    pix = doc[0].get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    pix.save(png_path)
    doc.close()
    return pix


def main() -> int:
    if not BACKGROUND.exists():
        raise SystemExit(f"missing cover image: {BACKGROUND}")

    FINAL.mkdir(parents=True, exist_ok=True)
    image_uri = jpeg_data_uri(BACKGROUND)
    content = cover_content(image_uri)
    SVG.write_text(svg_document(
        content,
        width=f"{WIDTH_MM}mm",
        height=f"{HEIGHT_MM}mm",
        view_box=f"0 0 {WIDTH_MM} {HEIGHT_MM}",
        title="The Letter at Puerto Lento — 5 by 8 inch paperback wrap",
        description=("One continuous harbor scene across the back, text-free spine, and "
                     "front cover for an 82-page cream-paper paperback."),
    ), encoding="utf-8")
    GUIDES_SVG.write_text(svg_document(
        content + guide_content(),
        width=f"{WIDTH_MM}mm",
        height=f"{HEIGHT_MM}mm",
        view_box=f"0 0 {WIDTH_MM} {HEIGHT_MM}",
        title="The Letter at Puerto Lento — KDP alignment review",
        description=("Review-only copy of the continuous wrap with trim, white live-area, "
                     "spine, and barcode guides. Never upload or print this file."),
    ), encoding="utf-8")
    FRONT_SVG.write_text(svg_document(
        content,
        width="1600",
        height="2560",
        view_box=f"{FRONT_FOLD_MM} {TRIM_TOP_MM} {TRIM_WIDTH_MM} {TRIM_HEIGHT_MM}",
        title="The Letter at Puerto Lento — front cover",
        description="Exact front-trim crop of the approved continuous paperback wrap.",
    ), encoding="utf-8")

    save_pdf_from_svg(SVG, PDF)
    KDP_PDF.parent.mkdir(parents=True, exist_ok=True)
    KDP_PDF.write_bytes(PDF.read_bytes())

    wrap = fitz.open(PDF)
    back_clip = fitz.Rect(0, 0, BACK_FOLD_MM * 72 / 25.4, HEIGHT_MM * 72 / 25.4)
    front_panel_clip = fitz.Rect(
        FRONT_FOLD_MM * 72 / 25.4, 0, WIDTH_MM * 72 / 25.4, HEIGHT_MM * 72 / 25.4
    )
    front_trim_clip = fitz.Rect(
        FRONT_FOLD_MM * 72 / 25.4,
        TRIM_TOP_MM * 72 / 25.4,
        (FRONT_FOLD_MM + TRIM_WIDTH_MM) * 72 / 25.4,
        TRIM_BOTTOM_MM * 72 / 25.4,
    )
    crop_pdf(wrap, CANVA_BACK_PDF, back_clip,
             "The Letter at Puerto Lento — Canva-ready back cover",
             "Back panel including bleed, 130.175 x 209.55 mm")
    crop_pdf(wrap, CANVA_FRONT_PDF, front_panel_clip,
             "The Letter at Puerto Lento — Canva-ready front cover",
             "Front panel including bleed, 130.178 x 209.55 mm")
    front_trim_pdf = FINAL / ".front-trim.tmp.pdf"
    crop_pdf(wrap, front_trim_pdf, front_trim_clip,
             "The Letter at Puerto Lento — Kindle front cover",
             "Exact 5 x 8 inch front-trim crop of the paperback master")
    wrap.close()

    preview = render_png(PDF, PREVIEW, 1600)
    guides_pdf = FINAL / ".guides.tmp.pdf"
    save_pdf_from_svg(GUIDES_SVG, guides_pdf)
    render_png(guides_pdf, GUIDES_PREVIEW, 1600)
    guides_pdf.unlink()
    wrap_300 = render_png(PDF, WRAP_PNG, round(WIDTH_MM / 25.4 * 300))
    back_pix = render_png(CANVA_BACK_PDF, CANVA_BACK_PNG,
                          round(BACK_FOLD_MM / 25.4 * 300))
    front_panel_pix = render_png(CANVA_FRONT_PDF, CANVA_FRONT_PNG,
                                 round((WIDTH_MM - FRONT_FOLD_MM) / 25.4 * 300))
    front_pix = render_png(front_trim_pdf, FRONT_PNG, 1600)
    front_doc = fitz.open(front_trim_pdf)
    scale = 1600 / front_doc[0].rect.width
    jpeg_pix = front_doc[0].get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    jpeg_pix.save(FRONT_JPEG, jpg_quality=94)
    front_doc.close()
    thumb_doc = fitz.open(front_trim_pdf)
    thumb_scale = 100 / thumb_doc[0].rect.width
    thumb_pix = thumb_doc[0].get_pixmap(matrix=fitz.Matrix(thumb_scale, thumb_scale), alpha=False)
    thumb_pix.save(FRONT_THUMB)
    thumb_doc.close()
    front_trim_pdf.unlink()

    for target in (KDP_FRONT, DIRECT_FRONT):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(FRONT_JPEG.read_bytes())

    print(
        f"OK: {SVG.relative_to(REPO)} and {PDF.relative_to(REPO)} "
        f"({WIDTH_MM} x {HEIGHT_MM} mm); preview {preview.width}x{preview.height}; "
        f"300dpi wrap {wrap_300.width}x{wrap_300.height}; "
        f"front {front_pix.width}x{front_pix.height}; "
        f"panels {back_pix.width}x{back_pix.height} / "
        f"{front_panel_pix.width}x{front_panel_pix.height}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
