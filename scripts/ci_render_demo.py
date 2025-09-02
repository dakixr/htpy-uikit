from __future__ import annotations

import runpy
import sys
from pathlib import Path

from htpy import body, head, html, link, meta, script, title


ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
THEME_SRC = ROOT / "src" / "htpy_uikit" / "tailwind-themes" / "theme.css"
DEMO_FILE = ROOT / "demo.py"
DIST = ROOT / "dist"


def _build_shell(content_node) -> str:
    doc = html(lang="en")[
        head()[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title()["htpy-uikit demo"],
            link(rel="stylesheet", href="./theme.css"),
            script(src="https://cdn.tailwindcss.com"),
            script(defer=True, src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"),
        ],
        body(class_="bg-background text-foreground")[content_node],
    ]
    return str(doc)


def _content_from_demo(ns: dict):
    fn = ns.get("components_demo_page")
    if not callable(fn):
        raise RuntimeError("demo.py must define a callable components_demo_page()")
    return fn()


def main() -> None:
    sys.path.insert(0, str(SRC))
    if not DEMO_FILE.exists():
        raise SystemExit("demo.py not found at repo root")
    ns = runpy.run_path(str(DEMO_FILE))
    content_node = _content_from_demo(ns)

    DIST.mkdir(parents=True, exist_ok=True)
    html_text = _build_shell(content_node)
    (DIST / "index.html").write_text(html_text, encoding="utf-8")

    # Copy theme
    if THEME_SRC.exists():
        (DIST / "theme.css").write_text(THEME_SRC.read_text(encoding="utf-8"), encoding="utf-8")


if __name__ == "__main__":
    main()

