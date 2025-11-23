from htpy import Node, div

from htpy_uikit.components.button import button_component
from htpy_uikit.components.form import form_component
from htpy_uikit.components.input import input_component

from ._utils import _demo_section


def form_section() -> Node:
    return _demo_section(
        "Form",
        "Structured form layouts and validation",
        [
            form_component(
                method="post",
                action="/submit",
            )[
                div(class_="space-y-4")[
                    input_component(
                        name="name",
                        placeholder="Enter your name",
                        label_text="Full Name",
                        required=True,
                    ),
                    input_component(
                        name="email",
                        type="email",
                        placeholder="john@example.com",
                        label_text="Email Address",
                        required=True,
                    ),
                    button_component(variant="primary", type="submit")["Submit"],
                ]
            ]
        ],
    )
