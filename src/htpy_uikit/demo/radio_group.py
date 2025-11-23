from htpy import Node, div

from htpy_uikit.components.radio_group import radio_group, radio_group_cards

from ._utils import _demo_section


def radio_group_section() -> Node:
    return _demo_section(
        "Radio Group",
        "Single selection from multiple options",
        [
            radio_group(
                name="demo-radio",
                options=[
                    {"value": "default", "label": "Default"},
                    {"value": "comfortable", "label": "Comfortable"},
                    {"value": "compact", "label": "Compact"},
                ],
                label_text="Choose an option",
            ),
            div(class_="mt-6 max-w-sm")[
                radio_group_cards(
                    name="demo-radio-card",
                    options=[
                        {
                            "value": "starter",
                            "title": "Starter Plan",
                            "description": "Perfect for small businesses getting started with our platform",
                        },
                        {
                            "value": "pro",
                            "title": "Pro Plan",
                            "description": "Advanced features for growing businesses with higher demands",
                        },
                    ],
                    card_color="green",
                )
            ],
        ],
    )
