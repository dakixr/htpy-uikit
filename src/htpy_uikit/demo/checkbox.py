from htpy import Node, div

from htpy_uikit.components.checkbox import checkbox_card_component, checkbox_component

from ._utils import _demo_section


def checkbox_section() -> Node:
    return _demo_section(
        "Checkbox",
        "Boolean input controls",
        [
            div(class_="space-y-4")[
                checkbox_component(
                    id="demo-cb-1",
                    label_text="Accept terms and conditions",
                ),
                checkbox_component(
                    id="demo-cb-2",
                    label_text="Accept terms and conditions",
                    description=(
                        "By clicking this checkbox, you agree to the terms and conditions."
                    ),
                ),
                checkbox_component(
                    id="demo-cb-3",
                    label_text="Enable notifications",
                    disabled=True,
                ),
                checkbox_card_component(
                    id="demo-cb-card",
                    label_text="Enable notifications",
                    description="You can enable or disable notifications at any time.",
                    card_color="blue",
                ),
                checkbox_card_component(
                    id="demo-cb-card-2",
                    label_text="Enable notifications",
                    description="You can enable or disable notifications at any time.",
                    card_color="red",
                ),
                checkbox_card_component(
                    id="demo-cb-card-3",
                    label_text="Enable notifications",
                    description="You can enable or disable notifications at any time.",
                    card_color="green",
                ),
            ]
        ],
    )
