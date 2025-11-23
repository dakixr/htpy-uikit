from htpy import Node, div

from htpy_uikit.components.button import button_component
from htpy_uikit.components.icons import (
    icon_arrow_right,
    icon_download,
    icon_more,
    icon_send,
    icon_spinner,
    icon_trash,
    icon_upload,
)

from ._utils import _demo_section


def button_section() -> Node:
    return _demo_section(
        "Button",
        "Interactive buttons with various styles and states",
        [
            div(class_="space-y-6")[
                # Row 1: main variants and a primary action
                div(class_="flex flex-wrap items-center gap-3")[
                    button_component(variant="primary")["Primary"],
                    button_component(variant="outline")["Outline"],
                    button_component(variant="ghost")["Ghost"],
                    button_component(variant="destructive")["Destructive"],
                    button_component(variant="danger")["Danger"],
                    button_component(variant="secondary")["Secondary"],
                    button_component(variant="link")["Link"],
                    button_component(variant="primary")[icon_send(), "Send email"],
                ],
                # Row 2: call-to-action + small controls
                div(class_="flex flex-wrap items-center gap-3")[
                    button_component(variant="primary", class_="rounded-full px-4")[
                        "Learn more",
                        icon_arrow_right(),
                    ],
                    button_component(variant="outline", loading=True)["Loading"],
                    button_component(disabled=True)["Disabled"],
                ],
                # Row 3: a second variation row to match reference spacing
                div(class_="flex flex-wrap items-center gap-3")[
                    button_component(variant="primary")["Primary"],
                    button_component(variant="outline")["Outline"],
                    button_component(variant="ghost")["Ghost"],
                    button_component(variant="danger")["Danger"],
                    button_component(variant="secondary")["Secondary"],
                    button_component(variant="link")["Link"],
                    button_component(variant="primary")[icon_send(), "Send"],
                    button_component(variant="outline", class_="ml-2")[icon_download(), "Download"],
                ],
                # Row 4: sizes and icon-only compact group
                div(class_="flex flex-wrap items-center gap-3")[
                    button_component(variant="primary", size="sm")["Primary sm"],
                    button_component(variant="primary")["Primary md"],
                    button_component(variant="primary", size="lg")["Primary lg"],
                    button_component(icon_only=True)[icon_download()],
                    button_component(variant="outline", icon_only=True)[icon_upload()],
                    button_component(variant="destructive", icon_only=True)[icon_trash()],
                    button_component(icon_only=True)[icon_arrow_right()],
                ],
                # Row 5: mixed compact controls and separators (icon-only set)
                div(class_="flex items-center gap-2")[
                    button_component(icon_only=True)[icon_download()],
                    button_component(variant="secondary", icon_only=True)[icon_upload()],
                    button_component(variant="outline", icon_only=True)[icon_arrow_right()],
                    button_component(variant="ghost", icon_only=True)[icon_more()],
                    button_component(variant="destructive", icon_only=True)[icon_trash()],
                    button_component(variant="outline", icon_only=True)[icon_spinner()],
                ],
            ]
        ],
    )
