#!/usr/bin/env python3
"""Build static reader site from story/chapters/*.md into docs/"""

import os
import re
import glob
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent.parent
CHAPTERS_DIR = ROOT / "story" / "chapters"
DOCS_DIR = ROOT / "docs"
CHAPTERS_OUT = DOCS_DIR / "chapters"

CHAPTERS_OUT.mkdir(parents=True, exist_ok=True)


def md_to_html(text: str) -> tuple[str, str]:
    """Convert markdown to HTML. Returns (title, body_html)."""
    title = "Kapitel"
    lines = text.split("\n")
    html_lines = []
    in_paragraph = False

    def close_p():
        nonlocal in_paragraph
        if in_paragraph:
            html_lines.append("</p>")
            in_paragraph = False

    def inline(s: str) -> str:
        # Bold
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        # Italic (handle both * and _)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"_(.+?)_", r"<em>\1</em>", s)
        # Escape any remaining HTML-unsafe chars that weren't intentional
        return s

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# "):
            close_p()
            title = stripped[2:]
            html_lines.append(f"<h1>{inline(title)}</h1>")
        elif stripped.startswith("## "):
            close_p()
            html_lines.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("### "):
            close_p()
            html_lines.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped == "---":
            close_p()
            html_lines.append("<hr>")
        elif stripped == "":
            close_p()
        else:
            if not in_paragraph:
                html_lines.append("<p>")
                in_paragraph = True
            html_lines.append(inline(stripped))

    close_p()
    return title, "\n".join(html_lines)


def page_html(title: str, body: str, prev_link: str, next_link: str, chapter_list: list) -> str:
    nav_items = ""
    for ch in chapter_list:
        nav_items += f'<li><a href="../chapters/{ch["file"]}">{ch["title"]}</a></li>\n'

    prev_btn = f'<a class="nav-btn" href="{prev_link}">← Föregående</a>' if prev_link else '<span class="nav-btn disabled">← Föregående</span>'
    next_btn = f'<a class="nav-btn" href="{next_link}">Nästa →</a>' if next_link else '<span class="nav-btn disabled">Nästa →</span>'

    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <nav class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <a class="site-title" href="../index.html">Wish</a>
      <button class="sidebar-close" onclick="toggleSidebar()" aria-label="Stäng meny">✕</button>
    </div>
    <ol class="chapter-list">
      {nav_items}
    </ol>
  </nav>
  <div class="overlay" id="overlay" onclick="toggleSidebar()"></div>

  <div class="reader">
    <header class="reader-header">
      <button class="menu-btn" onclick="toggleSidebar()" aria-label="Öppna meny">☰</button>
      <a class="site-title-inline" href="../index.html">Wish</a>
      <button class="theme-btn" onclick="toggleTheme()" aria-label="Byt tema">◑</button>
    </header>

    <article class="chapter-content">
      {body}
    </article>

    <div class="chapter-nav">
      {prev_btn}
      <a class="nav-btn home-btn" href="../index.html">Kapitel</a>
      {next_btn}
    </div>
  </div>

  <script>
    function toggleSidebar() {{
      document.getElementById('sidebar').classList.toggle('open');
      document.getElementById('overlay').classList.toggle('open');
    }}
    function toggleTheme() {{
      const d = document.documentElement;
      const current = d.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      d.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }}
    (function() {{
      const saved = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', saved);
    }})();
  </script>
</body>
</html>"""


def index_html(chapter_list: list) -> str:
    items = ""
    for ch in chapter_list:
        items += f"""    <li>
      <a href="chapters/{ch['file']}">
        <span class="ch-num">{ch['num']}</span>
        <span class="ch-title">{ch['title']}</span>
      </a>
    </li>\n"""

    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wish</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="index-page">
    <header class="index-header">
      <h1 class="book-title">Wish</h1>
      <button class="theme-btn" onclick="toggleTheme()" aria-label="Byt tema">◑</button>
    </header>
    <ol class="index-list">
{items}    </ol>
  </div>
  <script>
    function toggleTheme() {{
      const d = document.documentElement;
      const current = d.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      d.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }}
    (function() {{
      const saved = localStorage.getItem('theme') || 'light';
      document.documentElement.setAttribute('data-theme', saved);
    }})();
  </script>
</body>
</html>"""


def build():
    # Find and sort all chapters
    md_files = sorted(glob.glob(str(CHAPTERS_DIR / "chapter-*.md")))

    chapter_list = []
    for path in md_files:
        text = Path(path).read_text(encoding="utf-8")
        title, _ = md_to_html(text)
        m = re.search(r"chapter-(\d+)", path)
        num = int(m.group(1)) if m else 0
        chapter_list.append({
            "num": num,
            "title": title,
            "file": f"chapter-{num}.html",
            "src": path,
        })

    # Build each chapter page
    for i, ch in enumerate(chapter_list):
        text = Path(ch["src"]).read_text(encoding="utf-8")
        title, body = md_to_html(text)
        prev_link = f"chapter-{chapter_list[i-1]['num']}.html" if i > 0 else ""
        next_link = f"chapter-{chapter_list[i+1]['num']}.html" if i < len(chapter_list) - 1 else ""
        html = page_html(title, body, prev_link, next_link, chapter_list)
        out = CHAPTERS_OUT / ch["file"]
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {out}")

    # Build index
    idx = index_html(chapter_list)
    (DOCS_DIR / "index.html").write_text(idx, encoding="utf-8")
    print(f"  wrote {DOCS_DIR / 'index.html'}")

    print(f"Done — {len(chapter_list)} chapter(s) built.")


if __name__ == "__main__":
    build()
