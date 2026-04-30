#!/usr/bin/env python3
"""Render an academic interactive HTML slide deck from a small JSON spec."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_DIR / "assets" / "academic-deck-template.html"


def esc(value: object) -> str:
    return html.escape(str(value or ""), quote=True)


def slide_article(slide: dict, active: bool = False) -> str:
    kicker = esc(slide.get("kicker", ""))
    title = esc(slide.get("title", ""))
    body_html = str(slide.get("body_html", ""))
    caption = esc(slide.get("caption", ""))
    data_title = esc(slide.get("data_title") or title or kicker)
    active_class = " active" if active else ""
    caption_html = f'\n        <p class="caption">{caption}</p>' if caption else ""
    return f'''    <article class="slide{active_class}" data-title="{data_title}">
      <div class="slide-inner">
        <p class="kicker">{kicker}</p>
        <h2>{title}</h2>
        {body_html}{caption_html}
      </div>
    </article>'''


def title_slide(deck: dict) -> str:
    title = esc(deck.get("title", "Untitled Academic Presentation"))
    subtitle = esc(deck.get("subtitle", ""))
    context = esc(deck.get("context", ""))
    caption = esc(deck.get("caption", ""))
    kicker = esc(deck.get("kicker", "Academic Presentation"))
    subtitle_html = f"\n        <p>{subtitle}</p>" if subtitle else ""
    context_html = f"\n        <p class=\"small\">{context}</p>" if context else ""
    caption_html = f"\n        <p class=\"caption\">{caption}</p>" if caption else ""
    return f'''    <article class="slide active" data-title="Title">
      <div class="slide-inner">
        <p class="kicker">{kicker}</p>
        <h1>{title}</h1>{subtitle_html}{context_html}{caption_html}
      </div>
    </article>'''


def references_slide(refs: list[str], language: str) -> str:
    if not refs:
        return ""
    title = "参考文献" if language.lower().startswith("zh") else "Selected References"
    items = "\n".join(f"          <li>{esc(ref)}</li>" for ref in refs)
    return f'''    <article class="slide" data-title="References">
      <div class="slide-inner">
        <p class="kicker">References</p>
        <h2>{title}</h2>
        <ol class="small">
{items}
        </ol>
      </div>
    </article>'''


def render(spec_path: Path, output_path: Path) -> None:
    deck = json.loads(spec_path.read_text(encoding="utf-8"))
    language = str(deck.get("language", "zh-CN"))
    html_text = TEMPLATE.read_text(encoding="utf-8")
    slides = [title_slide(deck)]
    slides.extend(slide_article(slide) for slide in deck.get("slides", []))
    refs = deck.get("references", [])
    if refs:
        slides.append(references_slide(refs, language))
    html_text = html_text.replace("{{LANG}}", esc(language))
    html_text = html_text.replace("{{TITLE}}", esc(deck.get("title", "Academic Presentation")))
    html_text = html_text.replace("{{SLIDES}}", "\n".join(slides))
    output_path.write_text(html_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render academic interactive HTML slides from JSON.")
    parser.add_argument("spec", type=Path, help="Path to deck JSON spec")
    parser.add_argument("output", type=Path, help="Output .html path")
    args = parser.parse_args()
    render(args.spec, args.output)


if __name__ == "__main__":
    main()
