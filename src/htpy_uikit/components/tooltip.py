from typing import Literal

from htpy import Node
from htpy import Renderable
from htpy import span
from htpy import with_children

from ._types import TAlign
from ._types import TSide
from ._utils import merge_classes


@with_children
def tooltip(
    children: Node,
    *,
    content: Node,
    side: TSide = "top",
    align: TAlign = "center",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Tooltip component using inline Tailwind classes and Alpine for show/hide.

    The component renders a relative wrapper around `children` and an
    absolutely-positioned tooltip bubble. Visibility is controlled with
    Alpine (`x-data`, `x-show`, and `x-transition`) so no external CSS is
    required.

    Args:
        content: Tooltip content (string or Node)
        children: Trigger element
        side: One of "top", "bottom", "left", "right" (default: "top")
        align: One of "start", "center", "end" (default: "center")
        class_: Extra classes for the trigger wrapper
        **attrs: Extra attributes forwarded to the wrapper
    """

    # Position classes based on side/align using a dictionary mapping
    position_map: dict[TSide, dict[TAlign | Literal["base"], str]] = {
        "top": {
            "base": "bottom-full mb-1.5",
            "start": "left-0",
            "end": "right-0",
            "center": "left-1/2 -translate-x-1/2",
        },
        "bottom": {
            "base": "top-full mt-1.5",
            "start": "left-0",
            "end": "right-0",
            "center": "left-1/2 -translate-x-1/2",
        },
        "left": {
            "base": "right-full mr-1.5",
            "start": "top-0",
            "end": "bottom-0",
            "center": "top-1/2 -translate-y-1/2",
        },
        "right": {
            "base": "left-full ml-1.5",
            "start": "top-0",
            "end": "bottom-0",
            "center": "top-1/2 -translate-y-1/2",
        },
    }

    pos = f"{position_map[side]['base']} {position_map[side][align]}"

    # Base classes for bubble
    bubble_base = (
        "absolute z-50 bg-primary text-primary-foreground rounded-md px-3 py-1.5 "
        "text-xs whitespace-nowrap pointer-events-none transform transition-all"
    )

    # Wrapper attributes: Alpine handles open state on hover/focus
    wrapper_attrs = {
        "class_": merge_classes("relative inline-block w-fit", class_),
        "x-data": "{ open: false }",
        "@mouseenter": "open = true",
        "@mouseleave": "open = false",
        "@focus": "open = true",
        "@blur": "open = false",
        "tabindex": "0",
        "aria-describedby": "",
    }

    # Build tooltip bubble with Alpine show/transition attributes
    bubble_attrs = {
        "class_": f"{bubble_base} {pos}",
        "x-show": "open",
        "x-cloak": "",
        "x-transition:enter": "transition ease-out duration-200",
        "x-transition:enter-start": "opacity-0 scale-95",
        "x-transition:enter-end": "opacity-100 scale-100",
        "x-transition:leave": "transition ease-in duration-150",
        "x-transition:leave-start": "opacity-100 scale-100",
        "x-transition:leave-end": "opacity-0 scale-95",
        "role": "tooltip",
    }

    # Create elements
    bubble = span(**bubble_attrs)[content]

    return span(**wrapper_attrs, **attrs)[children, bubble]
