# htpy-uikit — htpy components + shadcn-style CLI

## What it is

- Self-contained htpy components, styled with TailwindCSS and Alpine.js
- Copy components into your app (not import at runtime) so Tailwind sees classes and you can fully customize
- Ships a default theme (CSS variables) you can import and override

## Demo

🚀 **[Live Demo](https://dakixr.github.io/htpy-uikit/)** - See all components in action with the kitchen sink demo

## Install

- **Dev-only**: add this library as a development dependency (no runtime import)

- **With uv (recommended)**:
  - `uv tool install git+https://github.com/dakixr/htpy-uikit.git`
- **Or with pip**: 
  - `pip install git+https://github.com/dakixr/htpy-uikit.git`

## CLI

```
Usage: htpyuikit [OPTIONS] COMMAND [ARGS]...

  htpy-uikit CLI: list and scaffold components into your app.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  add        Copy one or more components into your app (with deps).
  add-theme  Copy a theme CSS file into your app.
  list       List available components.
  themes     List available themes.
```


## Config (pyproject.toml)

```toml
[tool.htpy-uikit]
components_dir = "components"             # default for `add`
theme_path     = "styles/htpy-uikit.css"  # default for `add-theme`
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

## Credits

All component styles are adapted from [Basecoat UI](https://basecoatui.com/), a beautiful components library built with Tailwind CSS. A big thank you to the creators for their excellent work and for making it available to the community!

## Notes

- Requires Tailwind and Alpine in your app
- Override protection: existing files prompt for confirmation. Use `-y/--yes` or `--force` to overwrite without prompts
- No production dependency: your app should not import `htpy_uikit` at runtime. The CLI copies components into your codebase, so this package can be dev-only
