from typing import assert_never

from htpy import Node
from htpy import Renderable
from htpy import a
from htpy import span
from htpy import with_children

from ._types import BadgeStatus
from ._types import BadgeVariant
from .icons import icon_arrow_right


def _compute_badge_classes(variant: BadgeVariant, extra: str | None = None) -> str:
    """Compute the badge class string for a given variant and optional extra classes.

    Kept as a module-level helper so other helpers (like `badge_link`) can reuse the
    exact same visuals as `badge`.
    """
    base_classes = (
        "inline-flex items-center justify-center rounded-full border px-2 py-0.5 text-xs font-medium h-6 "
        "whitespace-nowrap shrink-0 gap-1 [&>svg]:size-3 [&>svg]:pointer-events-none focus-visible:border-ring "
        "focus-visible:ring-ring/50 focus-visible:ring-[3px] transition-[color,box-shadow] overflow-hidden"
    )

    if variant == "primary":
        var = "border-transparent bg-primary text-primary-foreground [a&]:hover:bg-primary/90"
    elif variant == "secondary":
        var = "border-transparent bg-secondary text-secondary-foreground [a&]:hover:bg-secondary/90"
    elif variant == "destructive":
        var = (
            "border-transparent bg-destructive text-destructive-foreground [a&]:hover:bg-destructive/90 "
            "focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 dark:bg-destructive/60"
        )
    elif variant == "outline":
        var = (
            "bg-background dark:bg-input/30 border border-border text-foreground "
            "[a&]:hover:bg-accent [a&]:hover:text-accent-foreground"
        )
    else:
        assert_never(variant)

    parts = [base_classes, var]
    if extra:
        parts.append(extra)
    return " ".join(parts)


@with_children
def badge(
    children: Node,
    *,
    variant: BadgeVariant = "primary",
    class_: str | None = None,
    left_icon: Renderable | None = None,
    right_icon: Renderable | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style badge component.

    Based on Basecoat UI badge component implementation.

    Args:
        children: Badge content
        variant: Badge style variant
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.span: Badge element
    """

    # Build classes via helper so other utilities can reuse same visual
    classes_str = _compute_badge_classes(variant, class_)

    # Add class to attrs
    attrs["class_"] = classes_str

    content = [left_icon, children, right_icon]
    return span(**attrs)[*(c for c in content if c)]


def badge_primary(children: Node, **kwargs) -> Renderable:
    """Primary badge variant."""
    return badge(variant="primary", **kwargs)[children]


def badge_secondary(children: Node, **kwargs) -> Renderable:
    """Secondary badge variant."""
    return badge(variant="secondary", **kwargs)[children]


def badge_destructive(children: Node, **kwargs) -> Renderable:
    """Destructive badge variant."""
    return badge(variant="destructive", **kwargs)[children]


def badge_outline(children: Node, **kwargs) -> Renderable:
    """Outline badge variant."""
    return badge(variant="outline", **kwargs)[children]


# Specific use case badges - simplified for basecoat
def badge_status(
    status: BadgeStatus,
    **kwargs,
) -> Renderable:
    """Status badge with automatic variant selection."""
    status_variants: dict[BadgeStatus, BadgeVariant] = {
        "active": "primary",
        "inactive": "secondary",
        "pending": "outline",
        "error": "destructive",
        "success": "primary",
        "failed": "destructive",
        "processing": "outline",
        "completed": "primary",
    }

    variant = status_variants.get(status, "primary")
    return badge(variant=variant, **kwargs)[status.title()]


def badge_count(
    count: int,
    *,
    cap: int = 20,
    variant: BadgeVariant = "primary",
    class_: str | None = None,
    **kwargs,
) -> Renderable:
    """Circular/pill style counter badge similar to reference screenshot.

    Args:
        count: Numeric value to display
        cap: Maximum value before showing "+" (e.g., 20+)
        variant: Badge style variant for the counter background
        class_: Extra classes to merge
    """
    display = str(count if count < cap else f"{cap}+")

    counter_classes = "rounded-full h-6 px-2 min-w-[1.5rem] flex items-center justify-center"
    merged_class = f"{counter_classes} {class_}" if class_ else counter_classes
    return badge(variant=variant, class_=merged_class, **kwargs)[display]


def badge_link(
    children: Node,
    *,
    href: str = "#",
    right_icon: Renderable | None = icon_arrow_right(),
    class_: str | None = None,
    new_tab: bool = True,
    **attrs,
) -> Renderable:
    """Render a link-styled badge (anchor) with optional right icon.

    Args:
        children: Link text/content
        href: href target for the anchor
        right_icon: Optional icon to show on the right
        class_: Extra classes to merge
        **attrs: Additional attributes for the anchor
    """
    # Reuse the badge outline visual but as an anchor
    base = (
        "inline-flex items-center justify-center rounded-full border px-2 py-0.5 text-xs font-medium h-6 "
        "whitespace-nowrap shrink-0 gap-1 [&>svg]:size-3 [&>svg]:pointer-events-none transition-[color,box-shadow] overflow-hidden"
    )
    outline = "bg-background dark:bg-input/30 border border-border text-foreground [a&]:hover:bg-accent [a&]:hover:text-accent-foreground"
    classes = f"{base} {outline}"
    if class_:
        classes = f"{classes} {class_}"

    attrs["class_"] = classes

    if new_tab:
        attrs["target"] = "_blank"

    attrs["href"] = href

    content = [children]
    if right_icon:
        content.append(right_icon)

    return a(**attrs)[*content]
