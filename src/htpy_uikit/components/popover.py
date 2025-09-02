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
    """
    Basecoat-style popover component.

    Based on Basecoat UI popover implementation.
    Uses standard HTML elements with popover class and data attributes.

    Args:
        children: Popover content
        trigger: Element that triggers the popover
        side: Popover side (top, bottom, left, right)
        align: Popover alignment (start, center, end)
        **attrs: Additional HTML attributes (including class_, id, style, etc.)

    Returns:
        htpy.div: Popover component
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
    """Simple popover with basic content."""
    return popover(children=content, trigger=trigger, **kwargs)


def popover_with_title(title: str, content: Node, trigger: Node, **kwargs) -> Renderable:
    """Popover with title and content."""
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
    """Button styled for popover triggers - following basecoat implementation."""
    return button_component(
        variant=variant,
        class_=class_,
        aria_expanded="false",
        aria_controls=f"{popover_id}-content",
        **attrs,
    )[children]
