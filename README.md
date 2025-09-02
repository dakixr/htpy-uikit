# htpy-uikit — htpy components + shadcn-style CLI

## What it is

- Self-contained htpy components, styled with TailwindCSS and Alpine.js
- Copy components into your app (not import at runtime) so Tailwind sees classes and you can fully customize
- Ships a default theme (CSS variables) you can import and override

## Install

- **Dev-only**: add this library as a development dependency (no runtime import)

- **With uv (recommended)**:
  - Published package: `uv add --dev htpy-uikit`
  - Local checkout: `uv add --dev -e ../path/to/htpy-uikit`
  - Run CLI via your env: `uv run htpyuikit list`
- **Or with pip**: `pip install -e .` (inside this repo)

## CLI

- **List**: `htpyuikit list`
- **Add (interactive)**: `htpyuikit add` (uses questionary)
- **Add specific**: `htpyuikit add button card --dest ./components`
- **Add all**: `htpyuikit add --all --dest ./components`
- **Theme**: `htpyuikit add-theme --dest ./styles/htpy-uikit.css`

## CI/CD (GitHub Pages)

- The workflow at `.github/workflows/gh-pages.yml` builds `demo.py` into `dist/index.html` and deploys to GitHub Pages
- Conventions expected by the workflow:
  - `demo.py` at the repo root, exposing `components_demo_page()` that returns an htpy node (the full page content)
  - Theme is copied from `src/htpy_uikit/tailwind-themes/theme.css` and linked in the page
  - Tailwind and Alpine are provided via CDN in the generated HTML for the demo

## Add copies code with deps into a single directory (no rewriting)

- `./components/*.py` (your selections + shared `_utils.py`, `_types.py`, `icons.py`)
  - `icons.py` can also be selected explicitly from the list

## Config (pyproject.toml)

```toml
[tool.htpy-uikit]
components_dir = "./components"          # default for `add`
theme_path     = "./styles/htpy-uikit.css"  # default for `add-theme`
```

## Themes

- **Light/Dark built-in**: theme CSS defines light variables on `:root` and dark overrides under `.dark { ... }`
  - Activate dark mode by toggling a `.dark` class on a root element (e.g., `html` or `body`)
  - You can scaffold `theme-toggle` via the CLI to manage this in the UI
- **List available themes**: `htpyuikit themes`
- **Copy theme (interactive)**: `htpyuikit add-theme` (prompts for theme and destination)
- **Choose explicitly**: `htpyuikit add-theme --theme <name> --dest ./styles/htpy-uikit.css`
- **Import in your Tailwind input CSS**:
  - `@import "./styles/htpy-uikit.css";`

## Notes

- Requires Tailwind and Alpine in your app
- Override protection: existing files prompt for confirmation. Use `-y/--yes` or `--force` to overwrite without prompts
- No production dependency: your app should not import `htpy_uikit` at runtime. The CLI copies components into your codebase, so this package can be dev-only
