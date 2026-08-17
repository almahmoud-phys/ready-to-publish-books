# Kindle eBook

Verified against official KDP guidance on 2026-08-15. Kindle is reflowable: readers control font, size, line spacing, and often background.

## Structure and navigation

- Provide a working logical table of contents with links; do not use print page numbers in a reflowable eBook TOC.
- Include a title page with the exact title and author.
- Use semantic headings in correct hierarchy. Do not simulate headings with manual font changes alone.
- Test the navigation document, landmarks, language metadata, and reading order.

## Styling

EPUB supports CSS. Story labels and story titles can have separate styles, sizes, spacing, and page-break behavior.

- Keep body typography adaptable; avoid forcing a fixed body font size, line height, color, or page margin.
- Use relative units for headings and spacing where practical.
- Use `break-before: page` with a compatible `page-break-before: always` fallback for new story units.
- Use `break-inside: avoid` / `page-break-inside: avoid` on heading groups, but test across Kindle engines because pagination is device-dependent.
- Do not assume a CSS page break maps to a stable printed page.

## QA

- Validate EPUB syntax and run epubcheck.
- Test in Kindle Previewer at multiple device sizes and font settings.
- Confirm every story label/title pair, TOC label, accented character, em dash, and Spanish punctuation.
- Check that decorative fonts degrade safely and remain readable; embedding/license rules still apply.
