from __future__ import annotations

from typing import Iterable

from htpy import Node
from htpy import div
from htpy import nav as nav_tag


def navbar(
    *,
    left: Node | Iterable[Node] | None = None,
    center: Node | Iterable[Node] | None = None,
    right: Node | Iterable[Node] | None = None,
    tag: str = "div",
    sticky: bool = True,
    outer_class: str | None = None,
    inner_class: str | None = None,
    container: bool = True,
    **attrs,
) -> Node:
    """Render a reusable navbar shell with left/center/right slots.

    Args:
        left: Nodes rendered on the left (e.g., logo).
        center: Nodes rendered in the center (e.g., nav links).
        right: Nodes rendered to the right (e.g., actions).
        tag: HTML tag used for the outer wrapper (``\"div\"`` or ``\"nav\"``).
        sticky: Whether to apply sticky top styles.
        outer_class: Extra classes appended to the outer wrapper.
        inner_class: Extra classes appended to the inner flex container.
        container: Whether to constrain contents to a max-width container.
        **attrs: Additional attributes forwarded to the outer element.

    Returns:
        Node: Renderable navbar wrapper.
    """

    base_outer = (
        (
            "sticky top-0 z-50 w-full border-b border-border/40 "
            "bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60"
        )
        if sticky
        else "w-full border-b border-border/40 bg-background"
    )

    base_inner = (
        "flex h-14 items-center justify-between gap-2 max-w-7xl px-4 sm:px-6 lg:px-8 mx-auto"
    )

    outer_cls = f"{base_outer} {outer_class}".strip() if outer_class else base_outer
    inner_cls = f"{base_inner} {inner_class}".strip() if inner_class else base_inner

    left_children = left
    center_children = center
    right_children = right

    # Choose tag for outer element
    outer = nav_tag if tag == "nav" else div

    # Build the inner content layout
    inner_content: list[Node] = []
    if left_children:
        inner_content.append(div(class_="flex items-center gap-2")[left_children])

    # Center area grows; hide if none provided
    if center_children:
        inner_content.append(div(class_="flex-1 flex items-center justify-center")[center_children])
    else:
        # keep layout stable when center is empty
        inner_content.append(div(class_="flex-1"))

    if right_children:
        inner_content.append(div(class_="flex items-center gap-2")[right_children])

    # Optionally wrap in a container div with sizing classes
    inner = div(class_=inner_cls)[inner_content]

    if container:
        # inner already has sizing classes including max width
        content = inner
    else:
        # when container=False, remove max width classes by overriding
        content = div(class_="flex h-14 items-center justify-between gap-2")[inner_content]

    return outer(class_=outer_cls, **attrs)[content]


def navbar_simple(*, right: Node | Iterable[Node]) -> Node:
    """Render a simplified navbar that only exposes the right slot.

    Args:
        right: Nodes rendered in the right-aligned area.

    Returns:
        Node: Renderable navbar container with only a right slot.
    """
    return navbar(
        right=right,
        inner_class="flex h-14 items-center justify-between space-x-2 max-w-7xl px-4 sm:px-6 lg:px-8 mx-auto",
    )
