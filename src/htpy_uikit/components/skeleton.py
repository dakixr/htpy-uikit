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
    """
    Basecoat-style skeleton loading component.

    Based on Basecoat UI skeleton implementation.
    Note: Basecoat doesn't have a dedicated skeleton component,
    this uses standard HTML elements with bg-accent and animate-pulse classes.

    Args:
        width: Width of skeleton (e.g., "w-32", "w-full")
        height: Height of skeleton (e.g., "h-4", "h-10")
        class_: Additional CSS classes
        rounded: Border radius (none, sm, md, lg, full)
        animate: Whether to animate the skeleton
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Skeleton component
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
    """Text skeleton with default height."""
    return skeleton(height="h-4", rounded="sm", **kwargs)


def skeleton_title(**kwargs) -> Renderable:
    """Title skeleton with larger height."""
    return skeleton(height="h-6", width="w-3/4", rounded="sm", **kwargs)


def skeleton_button(**kwargs) -> Renderable:
    """Button skeleton."""
    return skeleton(height="h-10", width="w-24", rounded="md", **kwargs)


def skeleton_avatar(**kwargs) -> Renderable:
    """Avatar skeleton (circular)."""
    return skeleton(width="w-10", height="h-10", rounded="full", **kwargs)


def skeleton_media_row(**kwargs) -> Renderable:
    """Avatar + two text lines, matching reference media row.

    Slightly increased gaps for a more balanced, professional layout.
    """
    return div(class_="flex items-center gap-6", **kwargs)[
        skeleton(size="size-10", shrink=True, rounded="full"),
        div(class_="grid gap-3")[
            skeleton(height="h-4", width="w-[150px]", rounded="md"),
            skeleton(height="h-4", width="w-[100px]", rounded="md"),
        ],
    ]


def skeleton_card(**kwargs) -> Renderable:
    """Single card with header/section placeholders as per reference.

    Add modest padding and spacing to match demo layout improvements.
    """
    return div(class_="card w-full @md:w-auto @md:min-w-sm p-4", **kwargs)[
        header(class_="space-y-2")[
            skeleton(height="h-4", width="w-2/3", rounded="md"),
            skeleton(height="h-4", width="w-1/2", rounded="md"),
        ],
        section(class_="pt-3")[skeleton(class_="rounded-md aspect-square w-full")],
    ]


def skeleton_table(rows: int = 5, columns: int = 4, **kwargs) -> Renderable:
    """Table skeleton with specified rows and columns.

    Use slightly larger gaps and vertical spacing for readability.
    """
    table_rows = []

    # Header row
    header_cells = [skeleton(height="h-8", width="w-full", rounded="sm") for _ in range(columns)]
    table_rows.append(div(class_="flex gap-6")[*header_cells])

    # Data rows
    for _ in range(rows):
        data_cells = [skeleton(height="h-6", width="w-full", rounded="sm") for _ in range(columns)]
        table_rows.append(div(class_="flex gap-6")[*data_cells])

    return div(class_="space-y-4", **kwargs)[*table_rows]
