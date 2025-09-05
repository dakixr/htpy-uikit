from pathlib import Path

from htpy_uikit.demo import demo_page

ROOT = Path(__file__).resolve().parent.parent
THEME_SRC = ROOT / "src" / "htpy_uikit" / "tailwind-themes" / "theme.css"
DIST = ROOT / "dist"
INPUT_TAILWIND_CSS = ROOT / "scripts" / "input.css"


def build_demo_assets() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / "index.html").write_text(demo_page(), encoding="utf-8")
    (DIST / "theme.css").write_text(THEME_SRC.read_text(encoding="utf-8"), encoding="utf-8")
    (DIST / "input.css").write_text(
        INPUT_TAILWIND_CSS.read_text(encoding="utf-8"), encoding="utf-8"
    )
