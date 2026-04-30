# Academic HTML PPT Design Contract

Use this reference when generating or customizing decks with `$academic-html-ppt`.

## Visual Direction

The deck should feel like a polished university lecture handout translated into an interactive browser presentation: paper-like, structured, calm, and citation-aware.

Default palette:

```css
:root {
  --bg:#f7f6f2;
  --paper:#fffdf8;
  --ink:#1e242b;
  --muted:#5e6874;
  --line:#d8d2c4;
  --accent:#254e70;
  --accent2:#7a4e2d;
  --soft:#ebe6da;
  --soft2:#e8eef3;
}
```

Typography:

- Use serif typography for slide titles and major conceptual headings.
- Use sans-serif typography for labels, controls, captions, tables, and metadata.
- Use local/system fonts only; no remote font loading.
- Keep body text readable from a projector: generally 24-34px scaled by the deck font variable.

Layout:

- Use a 16:9 slide stage with `aspect-ratio: 16 / 9`.
- Use a paper card surface against a warm neutral background.
- Use a left vertical accent bar on slide content cards.
- Use generous margins and clear hierarchy.
- Keep citations or source notes in a small footer/caption zone.

## Slide Planning Heuristics

Default structure:

1. Title slide
2. Research / teaching context
3. Core problem
4. Conceptual map
5. Key distinctions
6. Method / theory / framework
7. Case or example
8. Analysis
9. Comparison table
10. Classroom / research activity
11. Summary framework
12. References

For longer lectures, group slides into sections with short section divider slides. Keep section dividers minimal: kicker, title, one-sentence orientation.

## Density Rules

Use these as hard limits unless the user provides dense source material and asks for handout-like slides:

- Title slide: title, subtitle, presenter/context/date only.
- Standard content slide: 3-5 bullets or 2-3 cards.
- Comparison slide: 3-5 rows and 2-4 comparison columns.
- Flow slide: 3-6 steps.
- Quote slide: one quotation or paraphrased excerpt plus interpretation.
- References slide: compact list, smaller text, allow multiple columns if needed.

## Interaction Requirements

The template must support:

- Click controls and keyboard navigation.
- Overview mode displaying slide thumbnails in a grid.
- Fullscreen toggle using the browser Fullscreen API when available.
- Font scaling by changing a CSS variable or body class.
- Progress bar based on active slide index.
- Print CSS where all slides are visible and page-broken.

## HTML Implementation Notes

- Store slides as `.slide` elements with `data-title` when useful.
- Keep one active slide outside overview mode.
- Update slide counter and progress on every navigation event.
- In overview mode, clicking a slide should jump to that slide and exit overview.
- Avoid inline event handlers; use one small script at the bottom of the file.
- Keep CSS class names stable across decks.

## Final File Checklist

- No `http://` or `https://` asset references.
- No `<script src=...>` or `<link href=...>` external dependency.
- All text is selectable and printable.
- Controls are visible but unobtrusive.
- The deck remains usable on laptop and projector resolutions.
