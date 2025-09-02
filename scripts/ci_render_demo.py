from __future__ import annotations

from pathlib import Path

from htpy import body
from htpy import head
from htpy import html
from htpy import link
from htpy import meta
from htpy import script
from htpy import title
from markupsafe import Markup

from htpy_uikit.demo import components_demo_page

ROOT = Path(__file__).resolve().parent.parent
THEME_SRC = ROOT / "src" / "htpy_uikit" / "tailwind-themes" / "theme.css"
DIST = ROOT / "dist"


def _build_shell(content_node) -> str:
    doc = html(lang="en")[
        head()[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title()["htpy-uikit demo"],
            link(rel="stylesheet", href="./theme.css"),
            link(rel="stylesheet", href="./tailwind.css"),
            script(defer=True, src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"),
            # Initialize theme inline to avoid FOUC
            script[
                Markup(
                    """
                    localStorage.getItem('color-theme') !== 'light' ?
                    document.documentElement.classList.add('dark') :
                    document.documentElement.classList.remove('dark');
                    """
                )
            ],
        ],
        body(class_="bg-background text-foreground")[content_node],
    ]
    return str(doc)


def main() -> None:
    content_node = components_demo_page()

    DIST.mkdir(parents=True, exist_ok=True)
    html_text = _build_shell(content_node)
    (DIST / "index.html").write_text(html_text, encoding="utf-8")

    # Copy theme
    if THEME_SRC.exists():
        (DIST / "theme.css").write_text(
            THEME_SRC.read_text(encoding="utf-8"), encoding="utf-8"
        )


if __name__ == "__main__":
    main()
