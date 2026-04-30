---
name: academic-html-ppt
description: Generate academic-style interactive self-contained HTML slide decks for university teaching, research talks, graduate seminars, conference lectures, and browser-based PPT/web PPT requests. Use when the user asks for an academic PPT, interactive HTML presentation, offline webpage slides, 16:9 lecture deck, or a deck with keyboard navigation, overview mode, fullscreen, font-size controls, progress bar, and print/export-friendly CSS.
---

# Academic HTML PPT

## Output Contract

Create exactly one complete offline `.html` slide deck unless the user explicitly asks for additional artifacts.

- Name the file `academic_ppt_<short_topic>.html` using lowercase ASCII slug text.
- Embed all CSS and JavaScript in the file.
- Do not use external CDNs, remote fonts, tracking, or network dependencies.
- Use 16:9 responsive slides that work locally in a browser.
- Preserve the user's requested language; if unspecified, use the language of the user's prompt.
- Return the generated HTML file link only, plus the short note: `已生成互动式学术PPT网页。`

## Default Workflow

1. Infer missing parameters unless ambiguity would change the academic argument materially.
2. Build a slide plan before writing HTML: title, context, problem, conceptual map, distinctions, framework, case/example, analysis, comparison, activity, synthesis, references.
3. Expand or compress to fit the requested duration and content density; default to 12-25 slides.
4. Prefer `scripts/render_academic_deck.py` with a JSON slide spec when the deck can be represented as structured slide objects.
5. Use `assets/academic-deck-template.html` as the implementation baseline when hand-customizing HTML.
6. Read `references/design-contract.md` before making substantial visual/layout changes or when the user asks to match the style closely.
7. Write the final `.html` file in the user's working directory unless they specify another path.
8. Validate the generated file by checking navigation, overview mode, fullscreen control, font controls, print CSS, slide counter, and references.

## Content Rules

- Make each slide express one main idea.
- Prefer concise explanatory prose over slogans.
- Use cards for conceptual grouping, tables for comparisons, and flow diagrams for procedures.
- Include slide-level captions, citations, or source notes where claims need traceability.
- Put every cited source on the references slide.
- Avoid decorative images unless requested; if used, embed or use local assets only.
- Keep academic tone: precise, restrained, and readable for teaching or research settings.

## Required Interface Features

Every deck must include:

- Prev / Next controls
- Overview toggle
- A- / A+ font-size controls
- Fullscreen control
- Progress bar
- Slide counter
- Keyboard shortcuts: ArrowRight, PageDown, Space, ArrowLeft, PageUp, Home, End, O, +, -
- Print CSS that shows all slides cleanly

## Rendering Script

For repeatable generation, create a temporary JSON spec and run:

```bash
python3 scripts/render_academic_deck.py deck.json academic_ppt_<short_topic>.html
```

Each non-title slide should include `kicker`, `title`, `body_html`, and optional `caption`. The script adds the title slide, optional references slide, controls, keyboard support, overview mode, progress bar, and print CSS. Use direct HTML in `body_html` with the classes below.

## Reusable Classes

Prefer these class names so future decks remain visually consistent:

`.slide`, `.slide-inner`, `.kicker`, `.caption`, `.columns`, `.columns3`, `.card`, `.card.blue`, `.card.brown`, `.quote`, `.compare`, `.flow`, `.step`, `.tag`, `.code`, `.small`.

## Quality Gate

Before final response, verify:

- The file opens locally without internet access.
- Slides fit in a 16:9 viewport without obvious overflow.
- No slide is overloaded with dense paragraphs.
- Overview mode and normal mode both work.
- Print mode displays all slides instead of only the active slide.
- All citations or caption references are represented on the references slide.
