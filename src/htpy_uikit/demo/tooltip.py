from typing import cast

from htpy import Node, div

from htpy_uikit.components._types import TAlign, TSide
from htpy_uikit.components.button import button_component
from htpy_uikit.components.tooltip import tooltip

from ._utils import _demo_section


def tooltip_section() -> Node:
    return _demo_section(
        "Tooltip",
        "Contextual help and information",
        [
            div(class_="grid grid-cols-3 gap-4 justify-items-center-safe")[
                # Generate tooltips for all sides and alignments
                [
                    tooltip(
                        content=f"{side.capitalize()} tooltip",
                        side=side,
                        align=align,
                    )[button_component(variant="outline")[f"{side.capitalize()} - {align}"]]
                    for side in cast(
                        list[TSide],
                        ["top", "bottom", "left", "right"],
                    )
                    for align in cast(
                        list[TAlign],
                        ["start", "center", "end"],
                    )
                ]
            ]
        ],
    )
