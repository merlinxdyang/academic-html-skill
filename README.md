# Academic HTML PPT Skill / 学术风格互动式网页版 PPT Skill

[English](#english) | [中文](#中文)

## English

`academic-html-ppt` is a Codex skill for generating academic-style interactive HTML slide decks. It is designed for university teaching, research talks, graduate seminars, conference lectures, and browser-based presentation workflows.

The generated deck is a single self-contained `.html` file that works offline in a browser. It includes a 16:9 academic slide layout, keyboard navigation, overview mode, fullscreen support, font-size controls, a progress bar, slide counter, and print-friendly CSS.

### What It Generates

- Offline interactive HTML presentations
- Academic lecture decks and research talk decks
- 16:9 responsive browser slides
- Slide decks with citations, captions, conceptual cards, comparison tables, and flow diagrams
- Print/export-friendly HTML decks

### Design Style

The default style is restrained and academic:

- Paper-like warm background
- Serif title typography
- Sans-serif labels, tables, controls, and captions
- Left vertical accent bar
- Clean hierarchy and generous spacing
- Academic blue/brown color palette
- Slide-level source notes and references

### Interaction Features

Each deck should include:

- Prev / Next controls
- Overview mode
- A- / A+ font-size controls
- Fullscreen button
- Progress bar
- Slide counter
- Keyboard shortcuts for navigation
- Print CSS that displays all slides

### Keyboard Shortcuts

- `ArrowRight`, `PageDown`, `Space`: next slide
- `ArrowLeft`, `PageUp`: previous slide
- `Home`: first slide
- `End`: last slide
- `O`: overview mode
- `+` / `-`: font-size adjustment

### Repository Structure

```text
academic-html-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── academic-deck-template.html
├── references/
│   └── design-contract.md
└── scripts/
    └── render_academic_deck.py
```

### Usage

Invoke the skill in Codex with a request such as:

```text
使用 $academic-html-ppt 生成一个学术风格互动式网页版PPT，主题是：算法治理的制度逻辑
```

or:

```text
Use $academic-html-ppt to create an academic interactive HTML slide deck about platform governance for a 90-minute graduate seminar.
```

### Rendering From JSON

The included renderer can generate an HTML deck from a JSON slide specification:

```bash
python3 scripts/render_academic_deck.py deck.json academic_ppt_topic.html
```

Each content slide may contain:

```json
{
  "kicker": "01 / Context",
  "title": "Core Problem",
  "body_html": "<div class=\"card blue\"><h3>Concept</h3><p>Slide content.</p></div>",
  "caption": "Source: Author-year."
}
```

The renderer adds the title slide, optional references slide, controls, keyboard support, overview mode, progress bar, and print CSS.

## 中文

`academic-html-ppt` 是一个用于生成“学术风格互动式网页版 PPT”的 Codex skill。它适用于大学课程、研究报告、研究生研讨课、会议演讲，以及需要用浏览器展示的学术演示场景。

生成结果是一个完整、自包含、可离线打开的 `.html` 文件。它内置 16:9 学术幻灯片版式、键盘翻页、Overview 总览模式、全屏、字体缩放、进度条、页码计数和适合打印导出的 CSS。

### 可以生成什么

- 离线互动式 HTML 演示文稿
- 学术课程 PPT 和研究报告 PPT
- 16:9 响应式浏览器幻灯片
- 带引用、页脚说明、概念卡片、比较表格、流程图的 slide deck
- 适合打印或导出的 HTML 讲义式幻灯片

### 设计风格

默认视觉风格克制、清晰、学术化：

- 纸张质感的暖色背景
- 标题使用 serif 字体气质
- 标签、表格、控件和注释使用 sans-serif 字体
- 左侧竖向强调色条
- 清楚的层级和充足留白
- 学术蓝 / 棕色配色
- 每页可加入来源说明和参考文献追踪

### 交互功能

每个 deck 应包含：

- Prev / Next 翻页按钮
- Overview 总览模式
- A- / A+ 字体缩放
- Fullscreen 全屏按钮
- 进度条
- 当前页 / 总页数
- 键盘快捷键
- 可显示全部 slides 的打印 CSS

### 键盘快捷键

- `ArrowRight`, `PageDown`, `Space`：下一页
- `ArrowLeft`, `PageUp`：上一页
- `Home`：第一页
- `End`：最后一页
- `O`：Overview 总览模式
- `+` / `-`：调整字体大小

### 仓库结构

```text
academic-html-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── academic-deck-template.html
├── references/
│   └── design-contract.md
└── scripts/
    └── render_academic_deck.py
```

### 使用方式

在 Codex 中这样调用：

```text
使用 $academic-html-ppt 生成一个学术风格互动式网页版PPT，主题是：算法治理的制度逻辑
```

也可以提供更完整的上下文：

```text
使用 $academic-html-ppt 为一场90分钟研究生研讨课生成互动式学术 HTML PPT，主题是平台治理。
```

### 通过 JSON 渲染

仓库包含一个渲染脚本，可从 JSON slide spec 生成 HTML：

```bash
python3 scripts/render_academic_deck.py deck.json academic_ppt_topic.html
```

内容页可以写成：

```json
{
  "kicker": "01 / Context",
  "title": "核心问题",
  "body_html": "<div class=\"card blue\"><h3>概念</h3><p>页面内容。</p></div>",
  "caption": "Source: Author-year."
}
```

脚本会自动加入标题页、可选参考文献页、控制按钮、键盘支持、Overview、进度条和打印 CSS。
