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
    """Render the inner modal panel with consistent styling.

    Args:
        children: Body content rendered inside the panel.
        title: Heading text displayed in the sticky header.
        width: Tailwind width classes applied to the panel container.
        height: Tailwind height classes applied to the panel container.
        close_button_attrs: Attributes merged into the close button.

    Returns:
        Renderable: Panel ``div`` containing header and scrollable body.
    """

    panel_kwargs: dict[str, str] = {
        "class_": f"bg-card text-card-foreground rounded-lg shadow-lg border border-border flex flex-col {width} {height}",
        "@click.stop": "",
    }

    button_kwargs: dict[str, str] = {
        "type": "button",
        "class_": (
            "cursor-pointer text-muted-foreground bg-transparent hover:text-foreground rounded-lg "
            "text-sm w-8 h-8 ms-auto inline-flex justify-center items-center hover:bg-accent hover:text-white"
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
    """Render a modal shell controlled via Alpine custom events.

    Args:
        children: Modal body content.
        id: Identifier used for the open/close events.
        title: Modal title displayed in the header.
        width: Tailwind width classes for the panel.
        height: Tailwind height classes for the panel.

    Returns:
        Renderable: Overlay and panel nodes.
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
    """Return attributes that dispatch the ``modal-open`` event.

    Args:
        id: Modal identifier to include in the event detail.

    Returns:
        dict: Attribute dictionary suitable for ``button_component``.
    """
    return {
        "x-data": "",
        "@click": Markup(
            f"window.dispatchEvent(new CustomEvent('modal-open', {{ detail: '{id}' }}));"
        ),
    }


def attrs_btn_close_modal(id: str) -> dict:
    """Return attributes that dispatch the ``modal-close`` event."""
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
    """Render a standalone Alpine modal suitable for HTMX swaps.

    Args:
        children: Modal content.
        id: Optional id; generated when omitted.
        title: Modal title.
        width: Tailwind width classes for the panel.
        height: Tailwind height classes for the panel.

    Returns:
        Renderable: Modal overlay and panel nodes.
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
