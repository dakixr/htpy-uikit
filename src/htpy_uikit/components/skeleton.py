from typing import Literal

from htpy import Renderable
from htpy import div
from htpy import header
from htpy import section


def skeleton(
    *,
    width: str | None = None,
    height: str | None = None,
    size: str | None = None,
    shrink: bool = False,
    class_: str | None = None,
    rounded: Literal["none", "sm", "md", "lg", "full"] = "md",
    animate: bool = True,
    **attrs,
) -> Renderable:
    """Render a customizable skeleton placeholder.

    Args:
        width: Tailwind width class applied when ``size`` is not set.
        height: Tailwind height class applied when ``size`` is not set.
        size: Single Tailwind ``size-*`` class for square skeletons.
        shrink: Whether to apply ``shrink-0``.
        class_: Additional CSS classes appended to the skeleton.
        rounded: Border radius token (``\"md\"`` by default).
        animate: Whether to apply the pulsing animation.
        **attrs: Additional HTML attributes forwarded to the ``div``.

    Returns:
        Renderable: Skeleton ``<div>`` block.
    """

    # Base classes - following basecoat implementation
    base_classes = "bg-accent"

    # Animation classes
    animation_classes = "animate-pulse" if animate else ""

    # Rounded classes
    rounded_classes = {
        "none": "",
        "sm": "rounded-sm",
        "md": "rounded-md",
        "lg": "rounded-lg",
        "full": "rounded-full",
    }

    # Build class list
    classes = [base_classes]

    # Add animation if enabled
    if animation_classes:
        classes.append(animation_classes)

    # Add rounded class
    if rounded_classes[rounded]:
        classes.append(rounded_classes[rounded])

    # Size helpers: prefer explicit size token (e.g., "size-10") if given,
    # otherwise use width/height combos. If neither provided, fallback to full-width small height.
    if size:
        classes.append(size)
        # when size is used it's common to prevent shrinking
        if shrink:
            classes.append("shrink-0")
    else:
        if width:
            classes.append(width)
        else:
            classes.append("w-full")

        if height:
            classes.append(height)
        else:
            classes.append("h-4")

        if shrink:
            classes.append("shrink-0")

    # Add custom classes
    if class_:
        classes.append(class_)

    # Add class to attrs
    attrs["class_"] = " ".join(classes)

    return div(**attrs)


# Convenience functions for common skeleton patterns
def skeleton_text(**kwargs) -> Renderable:
    """Render a text-line skeleton block."""
    return skeleton(height="h-4", rounded="sm", **kwargs)


def skeleton_title(**kwargs) -> Renderable:
    """Render a heading-sized skeleton row."""
    return skeleton(height="h-6", width="w-3/4", rounded="sm", **kwargs)


def skeleton_button(**kwargs) -> Renderable:
    """Render a button-sized skeleton placeholder."""
    return skeleton(height="h-10", width="w-24", rounded="md", **kwargs)


def skeleton_avatar(**kwargs) -> Renderable:
    """Render a circular avatar skeleton."""
    return skeleton(width="w-10", height="h-10", rounded="full", **kwargs)


def skeleton_media_row(**kwargs) -> Renderable:
    """Render a skeleton row with avatar + two text lines."""
    return div(class_="flex items-center gap-6", **kwargs)[
        skeleton(size="size-10", shrink=True, rounded="full"),
        div(class_="grid gap-3")[
            skeleton(height="h-4", width="w-[150px]", rounded="md"),
            skeleton(height="h-4", width="w-[100px]", rounded="md"),
        ],
    ]


def skeleton_card(**kwargs) -> Renderable:
    """Render a card skeleton containing header and section placeholders."""
    return div(class_="card w-full @md:w-auto @md:min-w-sm p-4", **kwargs)[
        header(class_="space-y-2")[
            skeleton(height="h-4", width="w-2/3", rounded="md"),
            skeleton(height="h-4", width="w-1/2", rounded="md"),
        ],
        section(class_="pt-3")[skeleton(class_="rounded-md aspect-square w-full")],
    ]


def skeleton_table(rows: int = 5, columns: int = 4, **kwargs) -> Renderable:
    """Render a table skeleton with configurable dimensions."""
    table_rows = []

    # Header row
    header_cells = [skeleton(height="h-8", width="w-full", rounded="sm") for _ in range(columns)]
    table_rows.append(div(class_="flex gap-6")[*header_cells])

    # Data rows
    for _ in range(rows):
        data_cells = [skeleton(height="h-6", width="w-full", rounded="sm") for _ in range(columns)]
        table_rows.append(div(class_="flex gap-6")[*data_cells])

    return div(class_="space-y-4", **kwargs)[*table_rows]
