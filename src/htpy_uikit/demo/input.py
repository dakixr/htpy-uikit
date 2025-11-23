from htpy import Node, div

from htpy_uikit.components.input import input_component

from ._utils import _demo_section


def input_section() -> Node:
    return _demo_section(
        "Input",
        "Text input fields with labels",
        [
            div(class_="space-y-3")[
                input_component(type="text", placeholder="Text"),
                input_component(type="text", placeholder="Disabled", disabled=True),
                input_component(type="text", placeholder="Error", invalid=True),
                input_component(type="email", placeholder="Email"),
                input_component(type="password", placeholder="Password"),
                input_component(type="number", placeholder="Number"),
                input_component(type="file"),
                input_component(type="tel", placeholder="Tel"),
                input_component(type="url", placeholder="URL"),
                input_component(type="search", placeholder="Search"),
                input_component(type="date"),
                input_component(type="datetime-local"),
                input_component(type="time"),
            ]
        ],
    )
