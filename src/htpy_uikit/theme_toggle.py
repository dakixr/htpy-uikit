from htpy import button, div

from .icons import icon_moon, icon_sun


def theme_toggle():
    """
    Create a theme toggle button component.

    Returns:
        htpy.div: Theme toggle button with Alpine.js functionality
    """
    return div(x_data="ThemeToggle()", class_="cursor-pointer")[
        button(
            id="theme-toggle",
            type="button",
            class_="block w-full px-4 py-2 text-sm text-left text-muted-foreground hover:bg-accent dark:text-muted-foreground hover:bg-accent dark:hover:text-white",
            role="menuitem",
            **{"@click": "toggle()"},
        )[
            # Moon icon (dark mode off)
            icon_moon(class_="w-5 h-5", x_show="!darkMode"),
            # Sun icon (dark mode on)
            icon_sun(class_="w-5 h-5", x_show="darkMode"),
        ]
    ]
