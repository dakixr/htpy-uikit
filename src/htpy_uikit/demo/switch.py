from htpy import Node, div

from htpy_uikit.components.switch import switch, switch_card

from ._utils import _demo_section


def switch_section() -> Node:
    return _demo_section(
        "Switch",
        "Toggle switches for boolean values",
        [
            div(class_="space-y-6 max-w-2xl")[
                # Simple inline switches
                div(class_="space-y-3")[
                    switch(label_text="Airplane Mode"),
                    switch(label_text="Bluetooth", checked=True),
                    switch(label_text="Bluetooth", checked=True, color="blue"),
                    switch(label_text="Bluetooth", checked=True, color="green"),
                    switch(label_text="Bluetooth", checked=True, color="red"),
                ],
                # Form-style rows
                div(class_="form grid gap-4 mt-4")[
                    switch_card(
                        id="share-across-devices",
                        label_text="Share across devices",
                        description=(
                            "Focus is shared across devices, and turns off when you leave the app."
                        ),
                    ),
                    switch_card(
                        id="share-across-devices-blue",
                        label_text="Share across devices",
                        description=(
                            "Focus is shared across devices, and turns off when you leave the app."
                        ),
                        color="blue",
                    ),
                    switch_card(
                        id="share-across-devices-green",
                        label_text="Share across devices",
                        description=(
                            "Focus is shared across devices, and turns off when you leave the app."
                        ),
                        color="green",
                    ),
                ],
            ],
        ],
    )
