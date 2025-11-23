from htpy import Node, div

from htpy_uikit.components.avatar import avatar
from htpy_uikit.components.button import button_component
from htpy_uikit.components.dropdown_menu import (
    dropdown_menu,
    dropdown_menu_group,
    dropdown_menu_item,
    dropdown_menu_item_checkbox,
    dropdown_menu_item_radio,
    dropdown_menu_separator,
)
from htpy_uikit.components.icons import (
    icon_credit_card,
    icon_logout,
    icon_more,
    icon_settings,
    icon_user,
)

from ._utils import _demo_section


def dropdown_menu_section() -> Node:
    return _demo_section(
        "Dropdown Menu",
        "Contextual menus and actions",
        [
            # Row 1: reference-style trigger buttons
            div(class_="flex items-center gap-4 mb-6")[
                dropdown_menu(trigger=button_component(variant="outline")["Open"])[
                    div[
                        dropdown_menu_group(
                            div[
                                dropdown_menu_item("Profile", left_icon=icon_user()),
                                dropdown_menu_item("Billing", left_icon=icon_credit_card()),
                                dropdown_menu_item("Settings", left_icon=icon_settings()),
                                dropdown_menu_item("Keyboard shortcuts", shortcut="⌘K"),
                            ],
                            label="My Account",
                        ),
                        dropdown_menu_separator(),
                        dropdown_menu_item("GitHub"),
                        dropdown_menu_item("Support"),
                        dropdown_menu_item("API", disabled=True),
                        dropdown_menu_separator(),
                        dropdown_menu_item(
                            "Logout",
                            shortcut="⇧⌘P",
                            left_icon=icon_logout(),
                        ),
                    ]
                ],
                dropdown_menu(trigger=button_component(variant="outline")["Checkboxes"])[
                    div[
                        dropdown_menu_group(
                            div[
                                dropdown_menu_item(
                                    "Profile",
                                    shortcut="⇧⌘P",
                                    left_icon=icon_user(),
                                ),
                                dropdown_menu_item(
                                    "Billing",
                                    shortcut="⌘B",
                                    left_icon=icon_credit_card(),
                                ),
                                dropdown_menu_item(
                                    "Settings",
                                    shortcut="⌘S",
                                    left_icon=icon_settings(),
                                ),
                            ],
                            label="Account Options",
                        ),
                        dropdown_menu_separator(),
                        dropdown_menu_group(
                            div[
                                dropdown_menu_item_checkbox(label="Status Bar", checked=True),
                                dropdown_menu_item_checkbox(label="Activity Bar", disabled=True),
                                dropdown_menu_item_checkbox(label="Panel"),
                            ],
                            label="Appearance",
                        ),
                        dropdown_menu_separator(),
                        dropdown_menu_item(
                            "Logout",
                            shortcut="⇧⌘P",
                            left_icon=icon_logout(),
                        ),
                    ]
                ],
                dropdown_menu(trigger=button_component(variant="outline")["Radio Group"])[
                    div[
                        dropdown_menu_group(
                            div[
                                dropdown_menu_separator(),
                                dropdown_menu_item_radio(label="Status Bar", group="panel-pos"),
                                dropdown_menu_item_radio(
                                    label="Activity Bar",
                                    group="panel-pos",
                                    checked=True,
                                ),
                                dropdown_menu_item_radio(label="Panel", group="panel-pos"),
                            ],
                            label="Panel Position",
                        ),
                    ]
                ],
            ],
            # Row 2: custom trigger examples (icon-only, icon+label, avatar)
            div(class_="flex items-center gap-4")[
                dropdown_menu(
                    trigger=button_component(variant="ghost", class_="p-2 rounded-md")[
                        icon_more()
                    ]
                )[
                    div[
                        dropdown_menu_item("Item A"),
                        dropdown_menu_item("Item B"),
                    ]
                ],
                dropdown_menu(trigger=button_component(variant="outline")[icon_more(), "More"])[
                    div[
                        dropdown_menu_item("Action 1"),
                        dropdown_menu_item("Action 2"),
                    ]
                ],
                dropdown_menu(
                    trigger=button_component(variant="ghost")[
                        avatar(src="https://github.com/dakixr.png", size="sm")
                    ]
                )[
                    div[
                        dropdown_menu_item("Profile", left_icon=icon_user()),
                        dropdown_menu_item("Sign out", left_icon=icon_logout()),
                    ]
                ],
            ],
        ],
    )
