from typing import Literal

from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import h2
from htpy import p
from htpy import section as section_el
from htpy import span
from htpy import with_children


def _container_classes() -> str:
    return "max-w-(--breakpoint-xl) px-4 mx-auto"


def _pad_classes() -> str:
    return "py-12 sm:py-16 lg:py-20"


def _tone_classes(tone: Literal["default", "muted", "bordered"]) -> str:
    tones: dict[str, str] = {
        "default": "bg-background",
        "muted": "bg-muted/40 border-y border-border",
        "bordered": "bg-background border-t border-border",
    }
    return tones[tone]


@with_children
def section_block(
    children: Node,
    *,
    id: str | None = None,
    tone: Literal["default", "muted", "bordered"] = "default",
    class_: str | None = None,
    container_class: str | None = None,
    padding_classes: str = _pad_classes(),
) -> Renderable:
    """Standard landing page section wrapper.

    Provides consistent background, borders and container width/padding.
    """
    section_classes = _tone_classes(tone)
    if class_:
        section_classes = f"{section_classes} {class_}"

    container = container_class or f"{_container_classes()} {padding_classes}"

    content = div(class_=container)[children]
    attrs: dict[str, str] = {"class_": section_classes}
    if id:
        attrs["id"] = id
    return section_el(**attrs)[content]


def section_header(
    title: str,
    *,
    subtitle: str | None = None,
    overline: str | None = None,
    align: Literal["left", "center", "right"] = "center",
) -> Renderable:
    """Consistent section header block with optional overline and subtitle."""
    align_map = {
        "left": "text-left",
        "center": "text-center",
        "right": "text-right",
    }
    align_class = align_map[align]

    nodes: list[Renderable] = []
    if overline:
        nodes.append(
            span(class_="text-xs tracking-wider text-muted-foreground uppercase")[
                overline
            ]
        )
    nodes.append(
        h2(
            class_=f"mt-1 text-3xl sm:text-4xl font-extrabold tracking-tight {align_class}"
        )[title]
    )
    if subtitle:
        nodes.append(p(class_=f"mt-2 text-muted-foreground {align_class}")[subtitle])

    return div(class_="max-w-3xl mx-auto mb-6 sm:mb-8")[*nodes]
