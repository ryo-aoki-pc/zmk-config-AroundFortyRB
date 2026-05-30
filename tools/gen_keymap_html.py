#!/usr/bin/env python3
"""Generate a standalone KEYMAP.html from KEYMAP.md.

Converts the Markdown source into a self-contained HTML document:
- Markdown tables become HTML tables.
- Each "■ Row N" heading row gets a background color so it stands out.
- Inline code (`&kp Q`) becomes <code>, prose becomes headings/lists/paragraphs.

Inline styles are kept inline so the highlight renders in any standalone
HTML viewer (unlike GitHub-rendered Markdown, which strips style attributes).
"""
import re
import sys
from pathlib import Path

ROW_BG = "#fff3cd"
SRC = "KEYMAP.md"
OUT = "KEYMAP.html"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def cell_html(text):
    """Convert one Markdown table cell to inline HTML."""
    text = text.strip()
    holds = []

    def stash(m):
        holds.append(m.group(0))
        return f"\x00{len(holds) - 1}\x00"

    # Protect existing <br> tags and numeric/named entities (e.g. &#96;).
    text = re.sub(r"<br\s*/?>", stash, text)
    text = re.sub(r"&#\d+;|&\w+;", stash, text)

    # Code spans -> <code>...</code>, protected as a unit.
    def code_repl(m):
        holds.append("<code>" + esc(m.group(1)) + "</code>")
        return f"\x00{len(holds) - 1}\x00"

    text = re.sub(r"`([^`]*)`", code_repl, text)
    text = esc(text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: holds[int(m.group(1))], text)
    return text


def inline(text):
    """Convert inline code in prose to <code>, escaping the rest."""
    holds = []

    def code_repl(m):
        holds.append("<code>" + esc(m.group(1)) + "</code>")
        return f"\x00{len(holds) - 1}\x00"

    text = re.sub(r"`([^`]*)`", code_repl, text)
    text = esc(text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: holds[int(m.group(1))], text)
    return text


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return line.split("|")


def is_sep(line):
    return bool(re.match(r"^\s*\|(\s*:?-+:?\s*\|)+\s*$", line))


def convert_table(block):
    header = block[0]
    body = block[2:]  # skip header + separator
    out = ["<table>", "<thead>", "<tr>"]
    for c in split_row(header):
        out.append(f"<th>{cell_html(c)}</th>")
    out += ["</tr>", "</thead>", "<tbody>"]
    for line in body:
        cells = split_row(line)
        first = cells[0].strip()
        tr = f'<tr style="background-color:{ROW_BG}">' if first.startswith("■ Row") else "<tr>"
        out.append(tr)
        for c in cells:
            out.append(f"<td>{cell_html(c)}</td>")
        out.append("</tr>")
    out += ["</tbody>", "</table>"]
    return out


STYLE = """\
  body {
    font-family: -apple-system, "Segoe UI", "Hiragino Kaku Gothic ProN",
                 "Noto Sans JP", Meiryo, sans-serif;
    line-height: 1.6;
    color: #1f2328;
    max-width: 1400px;
    margin: 2rem auto;
    padding: 0 1.5rem;
  }
  h1 { border-bottom: 2px solid #d0d7de; padding-bottom: .3em; }
  h2 { border-bottom: 1px solid #d0d7de; padding-bottom: .3em; margin-top: 2em; }
  h3 { margin-top: 1.6em; }
  table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0 2em;
    font-size: 13px;
  }
  th, td {
    border: 1px solid #d0d7de;
    padding: 4px 8px;
    text-align: center;
    vertical-align: middle;
  }
  thead th { background: #f6f8fa; position: sticky; top: 0; }
  /* "■ Row N" heading rows are highlighted via inline background-color. */
  code {
    background: rgba(175,184,193,.2);
    padding: .1em .3em;
    border-radius: 4px;
    font-size: 85%;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  }
  tr[style] code { background: rgba(0,0,0,.06); }
"""


def build(src_text):
    lines = src_text.split("\n")
    body = []
    i, n = 0, len(lines)
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            body.append("</ul>")
            in_list = False

    while i < n:
        line = lines[i]
        stripped = line.strip()

        # Markdown table block.
        if stripped.startswith("|"):
            close_list()
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            if len(block) >= 2 and is_sep(block[1]):
                body += convert_table(block)
            else:
                body += [esc(b) for b in block]
            continue

        if stripped.startswith("### "):
            close_list()
            body.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            close_list()
            body.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            close_list()
            body.append(f"<h1>{inline(stripped[2:])}</h1>")
        elif stripped.startswith("- "):
            if not in_list:
                body.append("<ul>")
                in_list = True
            body.append(f"<li>{inline(stripped[2:])}</li>")
        elif stripped == "":
            close_list()
        else:
            close_list()
            body.append(f"<p>{inline(stripped)}</p>")
        i += 1

    close_list()

    return (
        '<!DOCTYPE html>\n<html lang="ja">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>キー割り当て一覧</title>\n<style>\n" + STYLE + "</style>\n</head>\n<body>\n"
        + "\n".join(body)
        + "\n</body>\n</html>\n"
    )


def main():
    root = Path(__file__).resolve().parent.parent
    src = (root / SRC).read_text(encoding="utf-8")
    html = build(src)
    (root / OUT).write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    sys.exit(main())
