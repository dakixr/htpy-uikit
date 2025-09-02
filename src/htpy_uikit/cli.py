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
from .registry import COMPONENTS_DIR
from .registry import Component
from .registry import list_components
from .registry import resolve_name_to_path


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
        if p.parent == PKG_DIR or p.stem in {"icons", "types", "__init__"}:
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
        selected = questionary.checkbox(
            "Select components (space to toggle, enter to confirm):",
            choices=choices,
        ).ask() or []
        return list(selected)
    # Fallback if Choice is unavailable
    selected = questionary.checkbox(
        "Select components (space to toggle, enter to confirm):",
        choices=[f"{c.name} ({c.path.name})" for c in comps],
    ).ask() or []
    lookup = {f"{c.name} ({c.path.name})": c for c in comps}
    return [lookup[s] for s in selected if s in lookup]


@cli.command("add")
@click.argument("components", nargs=-1)
@click.option(
    "--dest",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Destination root. A small package layout will be created here.",
)
@click.option(
    "--force", is_flag=True, help="Overwrite existing files without prompting."
)
def add_cmd(
    components: tuple[str, ...], dest: Path | None, force: bool
) -> None:
    """Copy one or more components into your app (with deps)."""
    comps = list_components()
    chosen: list[Component] = []

    if components:
        for token in components:
            p = resolve_name_to_path(token)
            if not p:
                click.echo(f"Unknown component: {token}", err=True)
                sys.exit(2)
            # find component object
            match = next((c for c in comps if c.path == p), None)
            if match is None:
                # allow internal modules to be copied if explicitly requested
                match = Component(name=p.stem, path=p)
            chosen.append(match)
    else:
        chosen = _interactive_pick(comps)
        if not chosen:
            click.echo("No components selected.")
            return

    # Load config and compute defaults
    cfg = _load_config()
    default_dest = Path(cfg.get("components_dir") or Path("./ui")).resolve()
    if dest is None:
        dest = default_dest

    entry_files = [c.path for c in chosen]
    files = _resolve_dependencies(entry_files)

    # Create a small package layout under dest
    pkg_root = dest
    components_dir = pkg_root / "components"
    pkg_root.mkdir(parents=True, exist_ok=True)
    components_dir.mkdir(parents=True, exist_ok=True)
    for pkg_init in (pkg_root / "__init__.py", components_dir / "__init__.py"):
        if not pkg_init.exists():
            pkg_init.write_text("", encoding="utf-8")

    for src in files:
        if src.parent == COMPONENTS_DIR:
            _copy_file(src, components_dir, force=force)
        else:
            _copy_file(src, pkg_root, force=force)

    # Adjust imports inside copied components: htpy_uikit.utils -> ..utils
    for p in components_dir.glob("*.py"):
        content = _read_text(p)
        newc = content.replace("from htpy_uikit.utils import", "from ..utils import")
        if newc != content:
            _write_text(p, newc)

    click.echo("\nDone. Remember to run your Tailwind build.")


@cli.command("add-theme")
@click.option(
    "--dest",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Path to write the theme CSS file. Defaults to pyproject config or ./styles/htpy-uikit.css.",
)
@click.option(
    "--force", is_flag=True, help="Overwrite existing file without prompting."
)
def add_theme_cmd(dest: Path | None, force: bool) -> None:
    """Copy the default theme CSS into your app."""
    # Resolve default destination from config
    cfg = _load_config()
    default_dest = Path(
        cfg.get("theme_path") or Path("./styles/htpy-uikit.css")
    ).resolve()
    if dest is None:
        dest = default_dest

    src = PKG_DIR / "tailwind-themes" / "theme.css"
    if not src.exists():
        click.echo("Theme file not found in package.", err=True)
        sys.exit(1)
    if dest.exists() and not force:
        if not questionary.confirm(f"{dest} exists. Overwrite?", default=False).ask():
            click.echo("Skipped theme.")
            return
    content = _read_text(src)
    _write_text(dest, content)
    click.echo(f"Copied theme.css -> {dest}")


def main() -> None:  # console_script entrypoint
    cli(prog_name="htpyuikit")
