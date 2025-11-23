from htpy import Node, div, form as form_, h4, header, p

from htpy_uikit.components.input import input_component
from htpy_uikit.components.label import label_component
from htpy_uikit.components.popover import popover, popover_trigger_button

from ._utils import _demo_section


def popover_section() -> Node:
    return _demo_section(
        "Popover",
        "Floating content overlays",
        [
            popover(
                id="demo-popover",
                trigger=popover_trigger_button(popover_id="demo-popover")["Open popover"],
                width_class="w-80",
            )[
                div(class_="grid gap-4")[
                    header(class_="grid gap-1.5")[
                        h4(class_="leading-none font-medium")["Dimensions"],
                        p(class_="text-muted-foreground text-sm")[
                            "Set the dimensions for the layer."
                        ],
                    ],
                    form_(class_="form grid gap-2")[
                        div(class_="grid grid-cols-3 items-center gap-4")[
                            label_component(for_="demo-popover-width")["Width"],
                            input_component(
                                type="text",
                                id="demo-popover-width",
                                value="100%",
                                class_="col-span-2 h-8",
                                autofocus="true",
                            ),
                        ],
                        div(class_="grid grid-cols-3 items-center gap-4")[
                            label_component(for_="demo-popover-max-width")["Max. width"],
                            input_component(
                                type="text",
                                id="demo-popover-max-width",
                                value="300px",
                                class_="col-span-2 h-8",
                            ),
                        ],
                        div(class_="grid grid-cols-3 items-center gap-4")[
                            label_component(for_="demo-popover-height")["Height"],
                            input_component(
                                type="text",
                                id="demo-popover-height",
                                value="25px",
                                class_="col-span-2 h-8",
                            ),
                        ],
                        div(class_="grid grid-cols-3 items-center gap-4")[
                            label_component(for_="demo-popover-max-height")["Max. height"],
                            input_component(
                                type="text",
                                id="demo-popover-max-height",
                                value="none",
                                class_="col-span-2 h-8",
                            ),
                        ],
                    ],
                ]
            ]
        ],
    )
