from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import h3
from htpy import path
from htpy import span
from htpy import svg
from htpy import with_children
from markupsafe import Markup

from ._utils import random_string


def _modal_panel(
    children: Node,
    *,
    title: str,
    width: str,
    height: str,
    close_button_attrs: dict[str, str] | None = None,
    panel_attrs: dict[str, str] | None = None,
) -> Renderable:
    """
    Shared modal panel content using consistent styles.

    Args:
        title: Modal title
        width: Modal width classes
        height: Modal height classes
        close_button_attrs: Attributes for the close button
        panel_attrs: Additional attributes for the panel container

    Returns:
        htpy.div: Panel element
    """

    panel_kwargs: dict[str, str] = {
        "class_": f"bg-background rounded-lg shadow-sm flex flex-col {width} {height}",
    }
    if panel_attrs:
        panel_kwargs |= panel_attrs

    button_kwargs: dict[str, str] = {
        "type": "button",
        "class_": (
            "text-muted-foreground bg-transparent hover:text-foreground rounded-lg "
            "text-sm w-8 h-8 ms-auto inline-flex justify-center items-center hover:bg-accent dark:hover:text-white"
        ),
    }
    if close_button_attrs:
        button_kwargs |= close_button_attrs

    return div(**panel_kwargs)[
        div(
            class_="flex items-center justify-between p-4 md:p-5 border-b rounded-t border-border"
        )[
            h3(class_="text-lg font-semibold text-foreground")[title],
            button(**button_kwargs)[
                svg(
                    class_="w-3 h-3",
                    xmlns="http://www.w3.org/2000/svg",
                    fill="none",
                    viewbox="0 0 14 14",
                )[
                    path(
                        stroke="currentColor",
                        stroke_linecap="round",
                        stroke_linejoin="round",
                        stroke_width="2",
                        d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6",
                    )
                ],
                span(class_="sr-only")[("Close modal")],
            ],
        ],
        div(class_="grow p-4 md:p-5 overflow-auto")[children],
    ]


@with_children
def modal(
    children: Node,
    *,
    id: str,
    title: str,
    width: str = "w-full max-w-lg",
    height: str = "h-auto",
) -> Renderable:
    """
    Basic modal component using the same styles as the HTMX modal.

    Args:
        id: Modal ID
        title: Modal title
        width: Modal width classes
        height: Modal height classes

    Returns:
        htpy.div: Modal element
    """

    return div(
        id=id,
        tabindex="-1",
        x_cloak="true",
        x_data="{ show: false }",
        x_show="show",
        class_=(
            "fixed top-0 right-0 left-0 z-50 flex justify-center items-center w-screen "
            "inset-0 h-full max-h-full bg-black/50"
        ),
        **{
            "@modal-open.window": Markup(f"if ($event.detail === '{id}') show = true;"),
            "@modal-close.window": Markup(
                f"if ($event.detail === '{id}') show = false;"
            ),
            "@click": "show = false",
        },
    )[
        _modal_panel(
            children,
            title=title,
            width=width,
            height=height,
            close_button_attrs={"@click": "show = false"},
            panel_attrs={"@click.stop": ""},
        )
    ]


def attrs_btn_open_modal(id: str) -> dict:
    """
    Get attributes for opening a modal button using Alpine.js events.

    Args:
        id: Modal ID

    Returns:
        dict: Button attributes for Alpine.js
    """
    return {
        "@click": Markup(
            f"window.dispatchEvent(new CustomEvent('modal-open', {{ detail: '{id}' }}));"
        )
    }


@with_children
def hx_modal(
    children: Node,
    *,
    title: str,
    width: str = "w-full max-w-lg",
    height: str = "h-auto",
) -> Renderable:
    """
    Alpine.js modal component (formerly HTMX).

    Args:
        title: Modal title
        content: Modal content
        width: Modal width classes
        height: Modal height classes

    Returns:
        htpy.div: Alpine.js modal element
    """
    random_id = random_string(8)

    return div(
        tabindex="-1",
        id=random_id,
        x_cloak="true",
        x_data="{ show: true }",
        x_show="show",
        class_=(
            "fixed top-0 right-0 left-0 z-50 flex justify-center items-center w-screen "
            "inset-0 h-full max-h-full bg-black/50"
        ),
        **{"@click": "show = false; setTimeout(() => $el.remove(), 200)"},
    )[
        _modal_panel(
            children,
            title=title,
            width=width,
            height=height,
            close_button_attrs={
                "@click": "show = false; setTimeout(() => $el.remove(), 200)",
                "type": "button",
            },
            panel_attrs={
                "@click.stop": "",
            },
        )
    ]
