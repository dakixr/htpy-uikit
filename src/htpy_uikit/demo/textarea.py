from htpy import Node, div

from htpy_uikit.components.textarea import textarea_component

from ._utils import _demo_section


def textarea_section() -> Node:
    return _demo_section(
        "Textarea",
        "Multi-line text input fields",
        [
            div(class_="space-y-6")[
                # Default textarea
                textarea_component(
                    id="demo-textarea",
                    placeholder="Type your message here",
                ),
                # With explicit label
                textarea_component(
                    id="demo-textarea-with-label",
                    placeholder="Type your message here",
                    rows=3,
                    label_text="Label",
                ),
                # With label and helper/description
                textarea_component(
                    id="demo-textarea-with-label-and-description",
                    placeholder="Type your message here",
                    rows=3,
                    label_text="With label and description",
                    required=True,
                    error="This is an error message",
                ),
                # Disabled
                textarea_component(
                    id="demo-textarea-disabled",
                    placeholder="Type your message here",
                    rows=3,
                    disabled=True,
                ),
            ]
        ],
    )
