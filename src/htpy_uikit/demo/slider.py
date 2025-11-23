from htpy import Node, div

from htpy_uikit.components.slider import slider

from ._utils import _demo_section


def slider_section() -> Node:
    return _demo_section(
        "Slider",
        "Range input controls",
        [
            div(class_="grid gap-4 max-w-xl")[
                # Simple slider (reference-style)
                slider(min=0, max=100, value=25, show_value=True),
                # Show value beside
                slider(min=0, max=10, value=3, show_value=True),
                # Different min/max/step
                slider(min=-50, max=50, step=5, value=10),
                # Disabled (muted visuals)
                slider(min=140, max=200, value=30, disabled=True),
                # Disabled with value display
                slider(
                    min=30,
                    max=300,
                    value=75,
                    disabled=True,
                    show_value=True,
                ),
                # Form-styled wrapper
                div(class_="form")[slider(min=10, max=450, value=60, show_value=True)],
            ]
        ],
    )
