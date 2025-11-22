# htpy-uikit - Agent Guide

## What is htpy-uikit?

htpy-uikit is a Python port of [Basecoat UI](https://basecoatui.com/) components, built with [htpy](https://github.com/lemon24/htpy), Tailwind CSS, and Alpine.js. It provides self-contained htpy component functions that users vendor into their applications via a CLI tool. Unlike traditional Python UI libraries, htpy-uikit is a dev-only dependency—components are copied into your codebase (not imported at runtime), allowing Tailwind to see all classes and enabling full customization.

## Quickstart

- Install dependencies: `uv sync` (or `pip install -e .[dev]`)
- Run demo server: `uv run python -m scripts.server_demo` (serves at `http://127.0.0.1:8000`)
- Build Tailwind CSS: The demo server automatically builds CSS via `npx @tailwindcss/cli`; standalone builds can use the same command
- List components: `htpyuikit list`
- Add components: `htpyuikit add <component-name>` or `htpyuikit add --all`

## Project layout

- `src/htpy_uikit/` - Main package:
  - `components/` - Component modules (htpy functions)
  - `tailwind-themes/` - Theme CSS files (CSS variables for light/dark)
  - `cli.py` - CLI entry point (`htpyuikit` command)
  - `registry.py` - Component discovery
  - `themes.py` - Theme discovery
  - `demo.py` - Demo page HTML generation
- `scripts/` - Development and build helpers:
  - `server_demo.py` - Flask server for local demo
  - `input.css` - Tailwind input CSS
  - `_utils.py` - Build utilities
- `dist/` - Generated demo assets (Tailwind output, demo HTML)
- `.basecoat/` - Upstream Basecoat reference (cloned for reference, not edited)

## Conventions

- Python style:
  - Type hints everywhere (`from __future__ import annotations`)
  - Use `htpy` for HTML generation (e.g., `button()`, `div()`, `span()`)
  - Component functions use `@with_children` decorator when accepting children
  - Use `click` for CLI commands
- Component naming:
  - Module files: `snake_case.py` (e.g., `alert_dialog.py`, `button.py`)
  - Component functions: descriptive names (e.g., `button_component`, `alert_dialog`, `tabs`)
  - CLI exposes kebab-case names (e.g., `alert-dialog`, `button`)
- Tailwind usage:
  - All Tailwind classes written inline (no `@apply` directives or layers)
  - Use Tailwind utilities directly in component `class_` attributes
  - Theme variables via CSS custom properties (e.g., `bg-primary`, `text-primary-foreground`)
- Alpine.js usage:
  - Use `x-data` for component state
  - Use `x-show`, `:hidden`, `:class` for conditional rendering/styling
  - Use `@click`, `@keydown.*` for event handlers
  - Use `x-ref` for element references
  - Prefer Alpine over custom JavaScript for interactive behavior

## Design Principles

- **Inline Tailwind**: Write Tailwind classes directly in component code (no `@apply` or CSS layers). This ensures Tailwind can purge unused classes and users can easily customize.
- **Alpine.js for behavior**: Use Alpine.js directives (`x-data`, `x-show`, `@click`, etc.) instead of custom JavaScript. Components should be self-contained and declarative.
- **Accessibility-first**: Semantic HTML, proper ARIA attributes (`role`, `aria-*`), keyboard navigation support, and focus management.
- **Theming via CSS variables**: Theme tokens defined in `tailwind-themes/theme.css` using CSS custom properties. Light mode on `:root`, dark mode under `.dark` selector. Users toggle dark mode by adding/removing `.dark` class on a root element.
- **Composable and minimal**: Prefer composition over complex components. If something is just HTML + Tailwind classes, document the pattern rather than creating a component.
- **Vendor-in model**: Components are copied into user projects via CLI, not imported at runtime. This allows full customization and ensures Tailwind sees all classes.

## Common tasks

- Update a component's markup/styles: Edit `src/htpy_uikit/components/<component>.py`, rebuild demo (`python scripts/server_demo.py`), verify visually
- Port a new component from Basecoat:
  1. Review `.basecoat/src/css/basecoat.css` for CSS classes
  2. Review `.basecoat/src/js/<component>.js` for JavaScript behavior
  3. Create `src/htpy_uikit/components/<component>.py` with htpy functions
  4. Convert CSS to inline Tailwind classes
  5. Convert JS to Alpine.js directives
  6. Add component to `src/htpy_uikit/demo.py` showcase
  7. Test via demo server
- Adjust theme tokens: Edit `src/htpy_uikit/tailwind-themes/theme.css`, rebuild demo to see changes
- Wire new component into demo: Add import and usage example to `src/htpy_uikit/demo.py`

## Testing

No automated testing configured. Validate changes manually:
- Run demo server: `uv run python -m scripts.server_demo`
- Open `http://127.0.0.1:8000` in browser
- Visually verify component rendering and behavior
- Test keyboard navigation and accessibility (screen reader, tab order)
- Ensure Tailwind CSS builds without errors (`npx @tailwindcss/cli` should succeed)