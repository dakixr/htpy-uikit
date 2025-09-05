from __future__ import annotations

import ast
import shutil
import sys
import tomllib
from pathlib import Path
from typing import Iterable
from typing import Sequence

import click
import questionary

from . import __version__ as VERSION
from .registry import PKG_DIR
from .registry import Component
from .registry import list_components
from .registry import resolve_name_to_path
from .themes import list_themes
from .themes import resolve_theme


def _read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def _write_text(p: Path, content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def _iter_internal_imports(py_src: str, file_dir: Path) -> Iterable[Path]:
    """Yield package file paths imported from this file (relative and absolute)."""
    try:
        tree = ast.parse(py_src)
    except SyntaxError:
        return []

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom):
            # Relative imports e.g. from .icons import x
            if node.level:
                # level=1 -> current package; level=2 -> parent, etc.
                base = file_dir
                steps_up = max(0, node.level - 1)
                for _ in range(steps_up):
                    base = base.parent
                mod = (node.module or "").split(".")[0]
                if mod:
                    cand = base / f"{mod}.py"
                    if cand.exists():
                        yield cand
            # Absolute import from our package
            elif node.module and node.module.startswith("htpy_uikit."):
                parts = node.module.split(".")[1:]
                cand = PKG_DIR.joinpath(*parts).with_suffix(".py")
                if cand.exists():
                    yield cand
        elif isinstance(node, ast.Import):
            # import htpy_uikit.icons as icons
            for n in node.names:
                name = n.name
                if name.startswith("htpy_uikit."):
                    parts = name.split(".")[1:]
                    cand = PKG_DIR.joinpath(*parts).with_suffix(".py")
                    if cand.exists():
                        yield cand


def _resolve_dependencies(entry_files: Sequence[Path]) -> list[Path]:
    """Given starting files, return all required files in package order (unique)."""
    wanted: dict[str, Path] = {}
    queue: list[Path] = list(entry_files)

    while queue:
        fp = queue.pop(0)
        name = fp.stem
        if name not in wanted:
            wanted[name] = fp
            src = _read_text(fp)
            for dep in _iter_internal_imports(src, file_dir=fp.parent):
                queue.append(dep)
    # return in stable order: support files first so copies don’t break imports
    internals = []
    components = []
    for p in wanted.values():
        if p.stem in {"_utils", "_types", "__init__"}:
            internals.append(p)
        else:
            components.append(p)
    # keep deterministic order by name
    internals.sort(key=lambda p: p.stem)
    components.sort(key=lambda p: p.stem)
    return internals + components


def _copy_file(src: Path, dest_dir: Path, force: bool) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    if dest.exists() and not force:
        overwrite = questionary.confirm(f"{dest} exists. Overwrite?", default=False).ask()
        if not overwrite:
            click.echo(f"Skipped {dest}")
            return dest
    shutil.copy2(src, dest)
    click.echo(f"Copied {src.name} -> {dest}")
    return dest


def _find_pyproject(start: Path | None = None) -> Path | None:
    """Find pyproject.toml by walking up from the starting directory."""
    cur = (start or Path.cwd()).resolve()
    root = cur.anchor
    while True:
        cand = cur / "pyproject.toml"
        if cand.exists():
            return cand
        if str(cur) == root:
            return None
        cur = cur.parent


def _load_config() -> dict:
    """Load configuration from pyproject.toml under [tool.htpy-uikit] or [tool.htpy_uikit]."""
    pj = _find_pyproject()
    if not pj:
        return {}
    try:
        data = tomllib.loads(_read_text(pj))
    except Exception:
        return {}
    tool = data.get("tool", {}) or {}
    cfg = tool.get("htpy-uikit") or tool.get("htpy_uikit") or {}
    # Normalize simple keys
    out: dict = {}
    if isinstance(cfg, dict):
        if isinstance(cfg.get("components_dir"), str):
            out["components_dir"] = str((pj.parent / cfg["components_dir"]).resolve())
        if isinstance(cfg.get("theme_path"), str):
            out["theme_path"] = str((pj.parent / cfg["theme_path"]).resolve())
    return out


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(
    package_name="htpy-uikit", version=VERSION if isinstance(VERSION, str) else None
)
def cli() -> None:
    """htpy-uikit CLI: list and scaffold components into your app."""


@cli.command("list")
def list_cmd() -> None:
    """List available components."""
    comps = list_components()
    if not comps:
        click.echo("No components found.")
        return
    width = max(len(c.name) for c in comps)
    click.echo("Available components:\n")
    for i, c in enumerate(comps, start=1):
        click.echo(f"{i:>2}. {c.name:<{width}}  ({c.path.name})")


def _interactive_pick(comps: list[Component]) -> list[Component]:
    qChoice = getattr(questionary, "Choice", None)
    if qChoice is not None:
        choices = [qChoice(title=f"{c.name} ({c.path.name})", value=c) for c in comps]
        selected = (
            questionary.checkbox(
                "Select components (space to toggle, enter to confirm):",
                choices=choices,
            ).ask()
            or []
        )
        return list(selected)
    # Fallback if Choice is unavailable
    selected = (
        questionary.checkbox(
            "Select components (space to toggle, enter to confirm):",
            choices=[f"{c.name} ({c.path.name})" for c in comps],
        ).ask()
        or []
    )
    lookup = {f"{c.name} ({c.path.name})": c for c in comps}
    return [lookup[s] for s in selected if s in lookup]


@cli.command("add")
@click.argument("components", nargs=-1)
@click.option(
    "--dest",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Destination directory for components (files copied here).",
)
@click.option("-A", "--all", "select_all", is_flag=True, help="Add all available components.")
@click.option(
    "-y",
    "--yes",
    "force",
    is_flag=True,
    help="Overwrite existing files without prompting (alias: --force).",
)
@click.option("--force", "force", is_flag=True, help="Overwrite existing files without prompting.")
def add_cmd(components: tuple[str, ...], dest: Path | None, select_all: bool, force: bool) -> None:
    """Copy one or more components into your app (with deps)."""
    comps = list_components()
    chosen: list[Component] = []

    selected_paths: list[Path] = []
    if select_all:
        selected_paths.extend([c.path for c in comps])
    if components:
        for token in components:
            p = resolve_name_to_path(token)
            if not p:
                click.echo(f"Unknown component: {token}", err=True)
                sys.exit(2)
            selected_paths.append(p)
    if not selected_paths and not select_all:
        chosen = _interactive_pick(comps)
        if not chosen:
            click.echo("No components selected.")
            return
        selected_paths = [c.path for c in chosen]
    # Dedup preserve order
    seen: set[Path] = set()
    unique_paths: list[Path] = []
    for p in selected_paths:
        if p not in seen:
            unique_paths.append(p)
            seen.add(p)
    # Convert to components
    chosen = []
    for p in unique_paths:
        match = next((c for c in comps if c.path == p), None)
        chosen.append(match or Component(name=p.stem, path=p))

    # Load config and compute defaults
    cfg = _load_config()
    default_dest = Path(cfg.get("components_dir") or Path("./components")).resolve()
    if dest is None:
        dest = default_dest

    entry_files = [c.path for c in chosen]
    files = _resolve_dependencies(entry_files)

    # Copy everything directly into the destination directory
    dest.mkdir(parents=True, exist_ok=True)
    # Ensure destination is a Python package by adding an empty __init__.py if missing
    init_py = dest / "__init__.py"
    if not init_py.exists():
        _write_text(init_py, "")
    for src in files:
        _copy_file(src, dest, force=force)

    click.echo("\nDone. Remember to run your Tailwind build.")


@cli.command("add-theme")
@click.option("--theme", help="Theme name to copy (omit to choose interactively if multiple).")
@click.option(
    "--dest",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Path to write the theme CSS file. Defaults to pyproject config or ./styles/htpy-uikit.css.",
)
@click.option("--force", is_flag=True, help="Overwrite existing file without prompting.")
def add_theme_cmd(theme: str | None, dest: Path | None, force: bool) -> None:
    """Copy a theme CSS file into your app."""
    # Resolve theme path
    src = resolve_theme(theme)
    if src is None:
        names = list_themes()
        if not names:
            click.echo("No themes available.")
            sys.exit(1)
        if len(names) == 1:
            src = resolve_theme(names[0])
        else:
            qChoice = getattr(questionary, "Choice", None)
            choices = [qChoice(title=n, value=n) for n in names] if qChoice else names
            chosen = questionary.select("Select a theme:", choices=choices).ask()
            if not chosen:
                click.echo("No theme selected.")
                return
            src = resolve_theme(chosen)
    if src is None or not src.exists():
        click.echo("Theme file not found in package.", err=True)
        sys.exit(1)

    cfg = _load_config()
    default_dest = Path(cfg.get("theme_path") or Path("./styles/htpy-uikit.css")).resolve()
    if dest is None:
        dest = default_dest

    if dest.exists() and not force:
        if not questionary.confirm(f"{dest} exists. Overwrite?", default=False).ask():
            click.echo("Skipped theme.")
            return
    content = _read_text(src)
    _write_text(dest, content)
    click.echo(f"Copied {src.name} -> {dest}")


@cli.command("themes")
def themes_cmd() -> None:
    """List available themes."""
    names = list_themes()
    if not names:
        click.echo("No themes available.")
        return
    click.echo("Available themes:\n")
    for i, n in enumerate(sorted(names), start=1):
        click.echo(f"{i:>2}. {n}")


def main() -> None:  # console_script entrypoint
    cli(prog_name="htpyuikit")
