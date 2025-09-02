htpy-uikit — htpy components + shadcn-style CLI

What it is
- Self-contained htpy components, styled with TailwindCSS and Alpine.js.
- Copy components into your app (not import at runtime) so Tailwind sees classes and you can fully customize.
- Ships a default theme (CSS variables) you can import and override.

Install
- `pip install -e .` (inside this repo) or add to your deps.

CLI
- List: `htpyuikit list`
- Add (interactive): `htpyuikit add` (uses questionary)
- Add specific: `htpyuikit add button card --dest ./ui`
- Theme: `htpyuikit add-theme --dest ./styles/htpy-uikit.css`

Add copies code with deps and creates a small package layout:
- `./ui/__init__.py`
- `./ui/components/*.py` (your selections + shared `icons.py`/`types.py`)
- `./ui/utils.py`

Config (pyproject.toml)
[tool.htpy-uikit]
components_dir = "./ui"                  # default for `add`
theme_path     = "./styles/htpy-uikit.css"  # default for `add-theme`

Theme
- Source: `src/htpy_uikit/tailwind-themes/theme.css`
- Copy with `htpyuikit add-theme` and import in your Tailwind input CSS:
  - `@import "./styles/htpy-uikit.css";`

Notes
- Requires Tailwind and Alpine in your app.
