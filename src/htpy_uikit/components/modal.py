from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import h3
from htpy import span
from htpy import with_children
from markupsafe import Markup
from sourcetypes import js

from ._utils import random_string
from .icons import icon_close


def _modal_panel(
    children: Node,
    *,
    title: str,
    width: str,
    height: str,
    close_button_attrs: dict[str, str] | None = None,
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
        "class_": f"bg-card text-card-foreground rounded-lg shadow-lg border border-border flex flex-col {width} {height}",
        "@click.stop": "",
    }

    button_kwargs: dict[str, str] = {
        "type": "button",
        "class_": (
            "cursor-pointer text-muted-foreground bg-transparent hover:text-foreground rounded-lg "
            "text-sm w-8 h-8 ms-auto inline-flex justify-center items-center hover:bg-accent dark:hover:text-white"
        ),
    }
    if close_button_attrs:
        button_kwargs |= close_button_attrs

    return div(**panel_kwargs)[
        div(class_="flex items-center justify-between p-4 md:p-5 border-b rounded-t border-border")[
            h3(class_="text-lg font-semibold text-card-foreground")[title],
            button(**button_kwargs)[
                icon_close(class_="size-5"),
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

    at_modal_open: js = f"""
        if ($event.detail === '{id}') {{
            console.log('modal-open: ', '{id}');
            show = true;
        }}
    """

    at_modal_close: js = f"""
        if ($event.detail === '{id}') {{
            console.log('modal-close: ', '{id}');
            show = false;
        }}
    """

    return div(
        # id=id,
        tabindex="-1",
        x_cloak="true",
        x_data="{ show: false }",
        x_show="show",
        class_=(
            "fixed top-0 right-0 left-0 z-50 flex justify-center items-center w-screen "
            "inset-0 h-full max-h-full bg-black/50"
        ),
        **{
            "@modal-open.window": Markup(at_modal_open),
            "@modal-close.window": Markup(at_modal_close),
        },
        **attrs_btn_close_modal(id),
    )[
        _modal_panel(
            children,
            title=title,
            width=width,
            height=height,
            close_button_attrs=attrs_btn_close_modal(id),
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
        "x-data": "",
        "@click": Markup(
            f"window.dispatchEvent(new CustomEvent('modal-open', {{ detail: '{id}' }}));"
        ),
    }


def attrs_btn_close_modal(id: str) -> dict:
    """
    Get attributes for closing a modal button using Alpine.js events.

    Note: this can only be used inside a modal component (or any other component that uses x-data).
    """
    close_modal: js = f"""
        window.dispatchEvent(new CustomEvent('modal-close', {{ detail: '{id}' }}));
    """
    return {
        # we do not use the x-data because this is a button is inside the model which is already using x-data
        "@click": Markup(close_modal),
        "@keydown.escape.window": Markup(close_modal),
    }


@with_children
def hx_modal(
    children: Node,
    *,
    id: str | None = None,
    title: str,
    width: str = "w-full max-w-lg",
    height: str = "h-auto",
) -> Renderable:
    """
    Alpine.js modal component (designed to be used with HTMX).

    Args:
        id: Modal ID (if not provided, a random ID will be generated)
        title: Modal title
        width: Modal width classes
        height: Modal height classes

    Returns:
        htpy.div: Alpine.js modal element
    """
    random_id = id or random_string(8)

    delete_modal: js = """
        show = false; 
        setTimeout(() => $el.remove(), 200)
    """

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
        **{"@click": delete_modal},
    )[
        _modal_panel(
            children,
            title=title,
            width=width,
            height=height,
            close_button_attrs={
                "@click": Markup(delete_modal),
                "@keydown.escape.window": Markup(delete_modal),
            },
        )
    ]
