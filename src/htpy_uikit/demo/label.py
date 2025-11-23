from htpy import Node, div, p

from htpy_uikit.components.checkbox import checkbox_component
from htpy_uikit.components.input import input_component
from htpy_uikit.components.label import label_component

from ._utils import _demo_section


def label_section() -> Node:
    return _demo_section(
        "Label",
        "Form field labels and descriptions",
        [
            div(class_="space-y-4")[
                # Label wrapping a control (checkbox inline label example)
                div[
                    label_component(
                        for_="demo-accept",
                        class_="flex items-center gap-2",
                    )[
                        checkbox_component(id="demo-accept"),
                        p["Accept terms and conditions"],
                    ]
                ],
                # Label with description
                input_component(
                    placeholder="Enter your name",
                    label_text="Full Name",
                    description="This is your legal name",
                ),
                input_component(
                    placeholder="Disabled",
                    label_text="Disabled",
                    description="This is a disabled input",
                    disabled=True,
                ),
                input_component(
                    type="email",
                    placeholder="john@example.com",
                    label_text="Email Address",
                    description="We'll never share your email with anyone",
                ),
            ]
        ],
    )
