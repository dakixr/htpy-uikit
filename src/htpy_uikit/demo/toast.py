from htpy import Node, div

from htpy_uikit.components.button import button_component
from htpy_uikit.components.toast import toast_trigger, toaster

from ._utils import _demo_section


def toast_section() -> Node:
    return _demo_section(
        "Toast",
        "Non-intrusive notifications",
        [
            # Toaster container
            div()[
                toaster(id="toaster", align="end"),
                div(class_="grid grid-cols-4 gap-3")[
                    toast_trigger(
                        category="success",
                        title="Success",
                        description="A success toast called from the front-end.",
                    )[button_component(variant="outline")["Success"]],
                    toast_trigger(
                        category="error",
                        title="Error",
                        description="An error occurred while saving your changes.",
                    )[button_component(variant="outline")["Error"]],
                    toast_trigger(
                        category="info",
                        title="Info",
                        description="This is some informational message.",
                    )[button_component(variant="outline")["Info"]],
                    toast_trigger(
                        category="warning",
                        title="Warning",
                        description="Be careful with this action.",
                    )[button_component(variant="outline")["Warning"]],
                    # HTMX backend-driven toast (event-only; swap none)
                    # button_component(
                    #     variant="outline",
                    #     hx_trigger="click",
                    #     hx_get="/en/events/toast/success",
                    #     hx_swap="none",
                    # )["Toast from backend (HTMX)"],
                ],
            ],
        ],
    )
