from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .registry import PKG_DIR


THEMES_DIR = PKG_DIR / "tailwind-themes"


def iter_theme_files() -> Iterable[Path]:
    if THEMES_DIR.exists():
        yield from (p for p in THEMES_DIR.glob("*.css") if p.is_file())


def list_themes() -> list[str]:
    names = sorted(p.stem for p in iter_theme_files())
    # Add a friendly alias if a single unnamed default exists
    return names


def resolve_theme(name: str | None) -> Path | None:
    if name:
        # Accept exact stem or a friendly alias "default" mapping to a single file named "theme.css"
        if name == "default":
            cand = THEMES_DIR / "theme.css"
            return cand if cand.exists() else None
        cand = THEMES_DIR / f"{name}.css"
        return cand if cand.exists() else None
    # No name provided: pick the only theme if there's exactly one, else None
    files = list(iter_theme_files())
    if len(files) == 1:
        return files[0]
    return None
