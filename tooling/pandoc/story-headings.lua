-- Render `Story N — Title` / `Historia N — Título` as a designed two-level
-- opening in PDF and EPUB while preserving the complete conventional title in the TOC.
local top_command = "section"

local function latex(text)
  local parsed = pandoc.read(text, "markdown")
  local rendered = pandoc.write(parsed, "latex")
  return rendered:gsub("%s+$", "")
end

local function story_header(header)
  if not header.classes:includes("story-opening") then
    return nil
  end

  local full = pandoc.utils.stringify(header.content)
  local label, title = full:match("^(Historia %d+)%s+—%s+(.+)$")
  if not label then
    label, title = full:match("^(Story %d+)%s+—%s+(.+)$")
  end
  if not label then
    return nil
  end

  if FORMAT:match("html") or FORMAT:match("epub") then
    header.content = {
      pandoc.Span({ pandoc.Str(label) }, pandoc.Attr("", { "story-label" })),
      pandoc.Space(),
      pandoc.Span(pandoc.read(title, "markdown").blocks[1].content,
        pandoc.Attr("", { "story-title" }))
    }
    return header
  end

  if not FORMAT:match("latex") then
    return nil
  end

  local command
  if top_command == "chapter" then
    command = header.level == 1 and "chapter" or "section"
  else
    command = header.level == 1 and "section" or "subsection"
  end

  local identifier = header.identifier ~= "" and ("\\label{" .. header.identifier .. "}") or ""
  -- \chapter* already clears the page. Placing \phantomsection before it creates
  -- a header-only blank page, so only section-level openings need an explicit break.
  local opening = command == "chapter" and "" or "\\clearpage\n\\phantomsection\n"
  local tex = string.format(
    "%s\\%s*{\\StoryHeading{%s}{%s}}%s\n\\addcontentsline{toc}{%s}{%s}\n\\markboth{%s}{%s}",
    opening, command, latex(label), latex(title), identifier, command, latex(full), latex(full), latex(full)
  )
  return pandoc.RawBlock("latex", tex)
end

-- Metadata filters run after block filters in Pandoc. Walking the document here
-- ensures story-heading-top is known before any heading is converted.
function Pandoc(doc)
  if doc.meta["story-heading-top"] then
    top_command = pandoc.utils.stringify(doc.meta["story-heading-top"])
  end
  return doc:walk({ Header = story_header })
end
