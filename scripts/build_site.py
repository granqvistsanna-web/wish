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

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Courier+Prime&display=swap" rel="stylesheet">'


def md_to_html(text: str) -> tuple[str, str]:
    """Convert markdown to HTML. Returns (title, body_html) — title NOT included in body."""
    title = "Kapitel"
    lines = text.split("\n")
    html_lines = []
    in_paragraph = False
    title_emitted = False

    def close_p():
        nonlocal in_paragraph
        if in_paragraph:
            html_lines.append("</p>")
            in_paragraph = False

    def inline(s: str) -> str:
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
        s = re.sub(r"_(.+?)_", r"<em>\1</em>", s)
        return s

    for line in lines:
        stripped = line.strip()

        if stripped.startswith("# ") and not title_emitted:
            # Capture title but DON'T emit <h1> — caller constructs it
            title = stripped[2:]
            title_emitted = True
        elif stripped.startswith("# "):
            # Subsequent h1s (rare) — treat as h2
            close_p()
            html_lines.append(f"<h2>{inline(stripped[2:])}</h2>")
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


def page_html(title: str, body: str, prev_link: str, next_link: str,
              chapter_list: list, ch_num: int) -> str:

    # Sidebar items
    nav_items = ""
    for ch in chapter_list:
        active = ' class="active"' if ch["num"] == ch_num else ""
        nav_items += f'<li><a href="../chapters/{ch["file"]}"{active}>{ch["title"]}</a></li>\n'

    prev_btn = f'<a class="nav-btn" href="{prev_link}">← Föregående</a>' if prev_link else '<span class="nav-btn disabled">← Föregående</span>'
    next_btn = f'<a class="nav-btn" href="{next_link}">Nästa →</a>' if next_link else '<span class="nav-btn disabled">Nästa →</span>'

    num_str = str(ch_num).zfill(2)

    # Strip "Kapitel N: " prefix for the display title if present
    display_title = re.sub(r'^[Kk]apitel\s+\d+\s*[:\-–—]\s*', '', title).strip()
    if not display_title:
        display_title = title

    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{display_title} — Wish</title>
  {FONTS}
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <div class="progress-bar" id="pb"></div>

  <nav class="sidebar" id="sidebar">
    <div class="sidebar-brand">
      <a href="../index.html">WISH</a>
      <button class="sidebar-close" onclick="toggleSidebar()" aria-label="Stäng meny">✕</button>
    </div>
    <div class="sidebar-label">Kapitel</div>
    <ol class="chapter-list">
      {nav_items}
    </ol>
  </nav>
  <div class="overlay" id="overlay" onclick="toggleSidebar()"></div>

  <div class="reader">
    <header class="top-bar">
      <button class="menu-btn" onclick="toggleSidebar()" aria-label="Öppna meny">☰</button>
      <a class="top-brand" href="../index.html">WISH</a>
      <button class="theme-btn" onclick="toggleTheme()" aria-label="Byt tema">◑</button>
    </header>

    <div class="chapter-header">
      <span class="chapter-kicker">Kapitel {num_str}</span>
      <h1>{display_title}</h1>
    </div>

    <article class="chapter-body">
      {body}
    </article>

    <div class="chapter-footer">
      {prev_btn}
      <a class="nav-btn home-btn" href="../index.html">Alla kapitel</a>
      {next_btn}
    </div>
  </div>

  <script>
    // Reading progress
    (function() {{
      const pb = document.getElementById('pb');
      function update() {{
        const el = document.documentElement;
        const pct = el.scrollTop / (el.scrollHeight - el.clientHeight) * 100;
        pb.style.setProperty('--progress', pct.toFixed(1) + '%');
      }}
      window.addEventListener('scroll', update, {{ passive: true }});
      update();
    }})();

    function toggleSidebar() {{
      document.getElementById('sidebar').classList.toggle('open');
      document.getElementById('overlay').classList.toggle('open');
    }}
    function toggleTheme() {{
      const d = document.documentElement;
      const next = d.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      d.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }}
    (function() {{
      const saved = localStorage.getItem('theme') || 'dark';
      document.documentElement.setAttribute('data-theme', saved);
    }})();
  </script>
</body>
</html>"""


def index_html(chapter_list: list) -> str:
    items = ""
    for ch in chapter_list:
        num_str = str(ch["num"]).zfill(2)
        display = re.sub(r'^[Kk]apitel\s+\d+\s*[:\-–—]\s*', '', ch["title"]).strip()
        if not display:
            display = ch["title"]
        items += f"""  <li>
      <a href="chapters/{ch['file']}">
        <span class="ch-num">{num_str}</span>
        <span class="ch-title">{display}</span>
        <span class="ch-arrow">→</span>
      </a>
    </li>\n"""

    return f"""<!DOCTYPE html>
<html lang="sv">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Wish</title>
  {FONTS}
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="index-page">
    <div class="index-hero">
      <button class="index-theme-btn" onclick="toggleTheme()" aria-label="Byt tema">◑</button>
      <span class="book-eyebrow">En roman</span>
      <h1 class="book-title">Wish</h1>
    </div>

    <div class="index-content">
      <div class="index-section-label">Kapitel</div>
      <ol class="index-list">
{items}      </ol>
    </div>
  </div>

  <script>
    function toggleTheme() {{
      const d = document.documentElement;
      const next = d.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
      d.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
    }}
    (function() {{
      const saved = localStorage.getItem('theme') || 'dark';
      document.documentElement.setAttribute('data-theme', saved);
    }})();
  </script>
</body>
</html>"""


def build():
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

    for i, ch in enumerate(chapter_list):
        text = Path(ch["src"]).read_text(encoding="utf-8")
        title, body = md_to_html(text)
        prev_link = f"chapter-{chapter_list[i-1]['num']}.html" if i > 0 else ""
        next_link = f"chapter-{chapter_list[i+1]['num']}.html" if i < len(chapter_list) - 1 else ""
        html = page_html(title, body, prev_link, next_link, chapter_list, ch["num"])
        out = CHAPTERS_OUT / ch["file"]
        out.write_text(html, encoding="utf-8")
        print(f"  wrote {out}")

    idx = index_html(chapter_list)
    (DOCS_DIR / "index.html").write_text(idx, encoding="utf-8")
    print(f"  wrote {DOCS_DIR / 'index.html'}")
    print(f"Done — {len(chapter_list)} chapter(s) built.")


if __name__ == "__main__":
    build()
