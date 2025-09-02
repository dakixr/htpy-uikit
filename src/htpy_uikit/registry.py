from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


PKG_NAME = "htpy_uikit"
PKG_DIR = Path(__file__).resolve().parent
COMPONENTS_DIR = PKG_DIR / "components"


# Files considered internal/shared; they may be dependencies but are not end-user components.
# Support files that shouldn’t be listed as user-facing components
INTERNAL_COMPONENT_MODULES = {"__init__", "_utils", "_types"}
INTERNAL_ROOT_MODULES = {"__init__"}


@dataclass(frozen=True)
class Component:
    name: str
    path: Path


def iter_component_files() -> Iterable[Path]:
    if COMPONENTS_DIR.exists():
        for p in COMPONENTS_DIR.glob("*.py"):
            if p.stem.startswith("_"):
                continue
            if p.stem in INTERNAL_COMPONENT_MODULES:
                continue
            yield p


def list_components() -> list[Component]:
    comps = [Component(name=p.stem.replace("_", "-"), path=p) for p in iter_component_files()]
    # stable, user-friendly ordering
    return sorted(comps, key=lambda c: c.name)


def resolve_name_to_path(name_or_filename: str) -> Path | None:
    """Resolve a user-provided component id to a file path within the package.

    Accepts component name in kebab-case (e.g. "alert-dialog") or module filename (e.g. "alert_dialog").
    """
    raw = name_or_filename.strip()
    candidates = {raw, raw.replace("-", "_")}
    # Prefer components directory
    if COMPONENTS_DIR.exists():
        for p in COMPONENTS_DIR.glob("*.py"):
            if p.stem in candidates:
                return p
    # Fallback to root modules (e.g., utils)
    for p in PKG_DIR.glob("*.py"):
        if p.stem in candidates:
            return p
    return None


def is_internal_module(name: str) -> bool:
    return name.startswith("_") or (name in INTERNAL_COMPONENT_MODULES) or (name in INTERNAL_ROOT_MODULES)
