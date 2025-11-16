from typing import Optional

from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import h2
from htpy import p
from htpy import path
from htpy import span
from htpy import svg
from htpy import with_children

from ._utils import merge_classes


def dialog(
    *,
    open: bool = False,
    title: Optional[str] = None,
    description: Optional[str] = None,
    class_: Optional[str] = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style dialog overlay.

    Args:
        open: Whether the dialog is visible.
        title: Title text rendered inside the dialog.
        description: Optional descriptive text.
        class_: Extra classes appended to the outer wrapper.
        **attrs: Additional HTML attributes forwarded to the wrapper ``div``.

    Returns:
        Renderable: Dialog backdrop and content nodes.
    """

    # Base classes
    base_classes = "fixed inset-0 z-50 flex items-center justify-center"

    if class_:
        base_classes += f" {class_}"

    # Combine attrs with required attributes
    combined_attrs = {"data-state": "open" if open else "closed", **attrs}
    if "class_" in combined_attrs:
        combined_attrs["class_"] = f"{base_classes} {combined_attrs['class_']}"
    else:
        combined_attrs["class_"] = base_classes

    return div(**combined_attrs)[
        # Backdrop
        div(class_="fixed inset-0 z-50 bg-black/50"),
        # Dialog content
        div(
            **{"role": "dialog", "aria-modal": "true"},
            class_=(
                "relative z-50 grid w-full max-w-lg gap-4 border border-gray-200 bg-white "
                "p-6 shadow-lg duration-200 sm:rounded-lg dark:border-gray-800 dark:bg-gray-950"
            ),
        )[
            # Close button
            button(
                class_=(
                    "absolute right-4 top-4 rounded-sm opacity-70 ring-offset-white "
                    "transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 "
                    "focus:ring-gray-400 focus:ring-offset-2 disabled:pointer-events-none "
                    "data-[state=open]:bg-gray-100 dark:ring-offset-gray-950 dark:focus:ring-gray-800 "
                    "dark:data-[state=open]:bg-gray-800"
                ),
                **{"data-state": "closed"},
            )[
                svg(
                    class_="h-4 w-4",
                    fill="none",
                    viewbox="0 0 24 24",
                    stroke="currentColor",
                    stroke_width="2",
                )[path(d="M18 6L6 18M6 6l12 12")],
                span(class_="sr-only")["Close"],
            ],
            # Dialog header
            div(class_="flex flex-col space-y-1.5 text-center sm:text-left")[
                h2(class_="text-lg font-semibold leading-none tracking-tight")[title or ""],
                p(class_="text-sm text-gray-500 dark:text-gray-400")[description or ""],
            ],
        ],
    ]


@with_children
def dialog_content(children: Node, **kwargs) -> Renderable:
    """Render the standard dialog with ``children`` as body content.

    Args:
        children: Content rendered inside the dialog body.
        **kwargs: Additional keyword arguments forwarded to ``dialog``.

    Returns:
        Renderable: Dialog tree.
    """
    return dialog(children=children, **kwargs)


def dialog_header(children: Node, *, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render a header section for dialog content.

    Args:
        children: Header content nodes.
        class_: Extra classes appended to the header wrapper.
        **attrs: Additional HTML attributes forwarded to the header ``div``.

    Returns:
        Renderable: Header ``<div>`` node.
    """
    classes = "flex flex-col space-y-1.5 text-center sm:text-left"
    attrs["class_"] = merge_classes(classes, class_)

    return div(**attrs)[children]


def dialog_title(children: Node, *, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render a styled dialog title element.

    Args:
        children: Title content.
        class_: Extra classes appended to the ``<h2>``.
        **attrs: Additional HTML attributes forwarded to the title element.

    Returns:
        Renderable: ``<h2>`` element representing the dialog title.
    """
    classes = "text-lg font-semibold leading-none tracking-tight"
    attrs["class_"] = merge_classes(classes, class_)

    return h2(**attrs)[children]


def dialog_description(children: Node, *, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render supporting description text for a dialog.

    Args:
        children: Description content.
        class_: Extra classes appended to the paragraph.
        **attrs: Additional attributes forwarded to the ``<p>``.

    Returns:
        Renderable: ``<p>`` node with muted styling.
    """
    classes = "text-sm text-gray-500 dark:text-gray-400"
    attrs["class_"] = merge_classes(classes, class_)

    return p(**attrs)[children]


def dialog_footer(children: Node, *, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render the dialog footer layout.

    Args:
        children: Footer content nodes (e.g., buttons).
        class_: Extra classes appended to the footer.
        **attrs: Additional HTML attributes forwarded to the ``div``.

    Returns:
        Renderable: Footer ``<div>`` node.
    """
    classes = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"
    attrs["class_"] = merge_classes(classes, class_)

    return div(**attrs)[children]


def dialog_close_button(*, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render a close button styled to match the dialog footer controls.

    Args:
        class_: Extra classes appended to the button.
        **attrs: Additional HTML attributes forwarded to the ``button``.

    Returns:
        Renderable: Close button renderable.
    """
    classes = (
        "mt-2 inline-flex h-10 items-center justify-center rounded-md border border-gray-300 "
        "bg-white px-4 py-2 text-sm font-medium ring-offset-white transition-colors hover:bg-gray-50 "
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-gray-400 focus-visible:ring-offset-2 "
        "disabled:pointer-events-none disabled:opacity-50 dark:border-gray-700 dark:bg-gray-950 "
        "dark:ring-offset-gray-950 dark:hover:bg-gray-800 dark:focus-visible:ring-gray-800 sm:mt-0"
    )
    attrs["class_"] = merge_classes(classes, class_)

    return button(**attrs)["Close"]


def dialog_action_button(children: Node, *, class_: Optional[str] = None, **attrs) -> Renderable:
    """Render the primary dialog action button.

    Args:
        children: Button label/content.
        class_: Extra classes appended to the button.
        **attrs: Additional HTML attributes forwarded to the ``button``.

    Returns:
        Renderable: Styled action button.
    """
    classes = (
        "inline-flex h-10 items-center justify-center rounded-md bg-blue-600 px-4 py-2 "
        "text-sm font-medium text-white transition-colors hover:bg-blue-700 focus-visible:outline-none "
        "focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 "
        "disabled:pointer-events-none disabled:opacity-50 dark:bg-blue-600 dark:hover:bg-blue-700 "
        "dark:focus-visible:ring-blue-300"
    )
    attrs["class_"] = merge_classes(classes, class_)

    return button(**attrs)[children]
