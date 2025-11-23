from htpy import Node, div

from htpy_uikit.components.badge import badge, badge_count, badge_link
from htpy_uikit.components.icons import icon_check, icon_chevron_right, icon_info

from ._utils import _demo_section


def badge_section() -> Node:
    return _demo_section(
        "Badge",
        "Status indicators and labels",
        [
            div(class_="flex flex-wrap items-center gap-2")[
                badge(variant="primary")["Primary"],
                badge(variant="secondary")["Secondary"],
                badge(variant="destructive")["Destructive"],
                badge(variant="outline")["Outline"],
                # With icons
                badge(variant="primary", left_icon=icon_check())["Badge"],
                badge(variant="destructive", left_icon=icon_info())["Alert"],
                badge(variant="outline", right_icon=icon_chevron_right())["With icon"],
                # Counters (compact)
                badge_count(8, variant="primary"),
                badge_count(99, variant="destructive"),
                badge_count(27, variant="outline"),
                # Small pill examples
                badge(class_="ml-2 px-2 py-0.5")["20+"],
                # With link
                badge_link(
                    "Link to GitHub",
                    href="https://github.com/dakixr",
                    new_tab=True,
                ),
            ]
        ],
    )
