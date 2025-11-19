from htpy import button
from htpy import div
from sourcetypes import js

from .icons import icon_moon
from .icons import icon_sun


def theme_toggle():
    """Render an Alpine-powered button that toggles dark/light theme."""

    x_data: js = """
    {
        darkMode: (localStorage.getItem('color-theme') ?? 'dark') === 'dark',
        toggle() {
            this.darkMode = !this.darkMode;
            if (this.darkMode) {
                document.documentElement.classList.add('dark');
                localStorage.setItem('color-theme', 'dark');
            } else {
                document.documentElement.classList.remove('dark');
                localStorage.setItem('color-theme', 'light');
            }
        },
        init() {
            if (this.darkMode) {
                document.documentElement.classList.add('dark');
            } else {
                document.documentElement.classList.remove('dark');
            }
        }
    }
    """

    return div(
        x_data=x_data,
        x_init="init()",
        class_="cursor-pointer",
    )[
        button(
            id="theme-toggle",
            type="button",
            class_="cursor-pointer block w-full px-4 py-2 text-sm text-left text-muted-foreground rounded-xl hover:bg-accent hover:text-foreground",
            role="menuitem",
            **{"@click": "toggle()"},
        )[
            # Moon icon (dark mode off)
            icon_moon(class_="w-5 h-5", x_show="!darkMode", x_cloak=""),
            # Sun icon (dark mode on)
            icon_sun(class_="w-5 h-5", x_show="darkMode", x_cloak=""),
        ]
    ]
