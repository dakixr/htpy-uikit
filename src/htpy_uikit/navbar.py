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
    """Reusable navbar container with left/center/right slots.

    - left: typically logo/brand
    - center: typically primary nav links
    - right: typically actions (theme toggle, profile, etc.)
    - tag: "div" (default) or "nav"
    - sticky: when True applies the sticky top styles used across the app
    - outer_class/inner_class: allow fine grained class overrides/extension
    - container: when True wraps inner content in a max-width container
    - **attrs: forwarded to the outer element (e.g. x-data)
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
    """A convenience variant matching the demo's minimal navbar.

    Renders only a right-aligned area inside the standard sticky shell.
    """
    return navbar(
        right=right,
        inner_class="flex h-14 items-center justify-between space-x-2 max-w-7xl px-4 sm:px-6 lg:px-8 mx-auto",
    )
