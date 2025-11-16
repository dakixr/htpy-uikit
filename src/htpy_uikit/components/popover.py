from typing import Literal

from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import with_children

from ._utils import merge_classes
from .button import ButtonVariant
from .button import button_component


@with_children
def popover(
    children: Node,
    *,
    id: str,
    trigger: Node,
    side: Literal["top", "bottom", "left", "right"] = "bottom",
    align: Literal["start", "center", "end"] = "start",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render an Alpine-controlled popover shell.

    Args:
        children: Popover body content.
        id: Root element id used to derive the popover content id.
        trigger: Node that toggles the popover.
        side: Popover placement relative to the trigger.
        align: Popover alignment relative to the trigger.
        class_: Extra classes appended to the root container.
        **attrs: Additional HTML attributes forwarded to the wrapper ``div``.

    Returns:
        Renderable: Popover trigger and content nodes.
    """

    # Generate unique IDs for the popover
    popover_id = f"{id}-content"

    # Set data attributes for positioning
    data_attrs = {
        "data-side": side,
        "data-align": align,
    }

    # Add custom class if provided
    attrs["class_"] = merge_classes("relative inline-flex", class_)

    # Add data attributes to existing attrs
    attrs.update(data_attrs)

    # Alpine.js implementation for popover
    alpine_attrs = {"x-data": "{ open: false }", **attrs}

    return div(id=id, **alpine_attrs)[
        # Trigger element with Alpine.js
        div(
            **{
                "@click": "open = !open",
                "@keydown.escape": "open = false",
                ":aria-expanded": "open",
            },
        )[trigger],
        # Popover content with Alpine.js
        div(
            id=popover_id,
            class_=" ".join(
                [
                    # Surface + layout
                    "absolute bg-popover text-popover-foreground overflow-x-hidden overflow-y-auto",
                    "rounded-md border border-border shadow-md z-50 visible opacity-100 scale-100",
                    "min-w-full w-max transition-all p-4 w-80 will-change-transform",
                    # Side positioning
                    (
                        "mt-1 top-full"
                        if side == "bottom"
                        else (
                            "mb-1 bottom-full"
                            if side == "top"
                            else ("mr-1 right-full" if side == "left" else "ml-1 left-full")
                        )
                    ),
                    # Align rules
                    (
                        (
                            "left-0"
                            if align == "start"
                            else ("right-0" if align == "end" else "left-1/2 -translate-x-1/2")
                        )
                        if side in ("top", "bottom")
                        else (
                            "top-0"
                            if align == "start"
                            else ("bottom-0" if align == "end" else "top-1/2 -translate-y-1/2")
                        )
                    ),
                ]
            ),
            **{
                "x-show": "open",
                "x-cloak": "",
                "x-transition:enter": "transition ease-out duration-150",
                "x-transition:enter-start": "opacity-0 translate-y-1",
                "x-transition:enter-end": "opacity-100 translate-y-0",
                "x-transition:leave": "transition ease-in duration-120",
                "x-transition:leave-start": "opacity-100 translate-y-0",
                "x-transition:leave-end": "opacity-0 translate-y-1",
                "@click.outside": "open = false",
                "@keydown.escape": "open = false",
                "data-popover": "",
                ":aria-hidden": "!open",
            },
        )[children],
    ]


# Convenience functions for common popover patterns - following basecoat implementation
def popover_simple(content: Node, trigger: Node, **kwargs) -> Renderable:
    """Render a popover with the provided content/trigger nodes.

    Args:
        content: Popover body nodes.
        trigger: Trigger element.
        **kwargs: Additional keyword arguments forwarded to ``popover``.

    Returns:
        Renderable: Popover structure.
    """
    return popover(children=content, trigger=trigger, **kwargs)


def popover_with_title(title: str, content: Node, trigger: Node, **kwargs) -> Renderable:
    """Render a popover that includes a heading element above the content.

    Args:
        title: Heading text inside the popover.
        content: Popover body nodes.
        trigger: Trigger element.
        **kwargs: Additional keyword arguments forwarded to ``popover``.

    Returns:
        Renderable: Popover structure with title.
    """
    from htpy import h4

    content_with_title = div[h4(class_="font-semibold mb-2")[title], content]
    return popover(children=content_with_title, trigger=trigger, **kwargs)


@with_children
def popover_trigger_button(
    children: Node,
    *,
    popover_id: str,
    variant: ButtonVariant = "outline",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a button that targets a popover by id.

    Args:
        children: Button content.
        popover_id: Id of the popover being controlled.
        variant: Button variant passed to ``button_component``.
        class_: Extra classes appended to the button.
        **attrs: Additional attributes forwarded to ``button_component``.

    Returns:
        Renderable: Button configured with proper aria attributes.
    """
    return button_component(
        variant=variant,
        class_=class_,
        aria_expanded="false",
        aria_controls=f"{popover_id}-content",
        **attrs,
    )[children]
