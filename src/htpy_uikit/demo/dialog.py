from htpy import Node, div, p

from htpy_uikit.components.button import button_component
from htpy_uikit.components.modal import attrs_btn_open_modal, modal

from ._utils import _demo_section


def dialog_section() -> Node:
    return _demo_section(
        "Dialog",
        "Modal dialogs for user interactions",
        [
            div(class_="flex gap-4")[
                button_component(**attrs_btn_open_modal("demo-modal"))["Open Modal"],
                modal(id="demo-modal", title="Demo Modal")[
                    div[
                        p["This is a modal dialog with custom content."],
                        p[
                            "You can put any content here, including forms, images, or other components."
                        ],
                    ]
                ],
            ]
        ],
    )
