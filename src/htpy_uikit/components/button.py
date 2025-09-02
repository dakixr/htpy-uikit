from typing import assert_never

from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import span
from htpy import with_children

from ._types import ButtonSize
from ._types import ButtonType
from ._types import ButtonVariant
from .icons import icon_spinner


@with_children
def button_component(
    children: Node,
    *,
    variant: ButtonVariant = "primary",
    size: ButtonSize = "md",
    loading: bool = False,
    disabled: bool = False,
    icon_only: bool = False,
    type: ButtonType = "button",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style button component with multiple variants and states.

    Based on Basecoat UI button component implementation.

    Args:
        children: Button content
        variant: Button style variant
        size: Button size
        loading: Show loading spinner
        disabled: Disable button
        icon_only: Whether this is an icon-only button
        type: Button type attribute
        class_: Additional classes to apply to the button or override the default classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.button: Styled button element
    """

    # Base classes - Tailwind utilities mirroring Basecoat `.btn` defaults
    base_classes = (
        "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium transition-all "
        "disabled:cursor-not-allowed disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 "
        "shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 "
        "focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
        "aria-invalid:border-destructive cursor-pointer rounded-md gap-2 h-9 px-4 has-[>svg]:px-3"
    )

    # Build class list based on variant and size
    classes = [base_classes]

    # Add variant classes - using Tailwind equivalents
    variant_classes: dict[ButtonVariant, str] = {
        "primary": "bg-primary text-primary-foreground shadow-xs hover:bg-primary/90",
        "secondary": "bg-secondary text-secondary-foreground shadow-xs hover:bg-secondary/80",
        # Use white text on destructive buttons to match reference (strong contrast)
        "destructive": (
            "bg-destructive text-white shadow-xs focus-visible:ring-destructive/20 "
            "dark:focus-visible:ring-destructive/40 dark:bg-destructive/60 hover:bg-destructive/90 dark:hover:bg-destructive/50"
        ),
        "outline": "border bg-background shadow-xs dark:bg-input/30 dark:border-input hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50",
        "ghost": "hover:bg-accent hover:text-accent-foreground",
        "link": "text-primary underline-offset-4 hover:underline",
        "danger": (
            "bg-destructive text-white shadow-xs focus-visible:ring-destructive/20 "
            "dark:focus-visible:ring-destructive/40 dark:bg-destructive/60 hover:bg-destructive/90 dark:hover:bg-destructive/50"
        ),
    }
    # All variants should be handled in the dictionary
    if variant in variant_classes:
        classes.append(variant_classes[variant])
    else:
        # This should never happen if ButtonVariant and variant_classes are kept in sync
        raise ValueError(f"Unsupported button variant: {variant}")

    # Add size classes
    if size == "md":
        classes.append("gap-2 h-9 px-4 has-[>svg]:px-3")
    elif size == "sm":
        classes.append("gap-1.5 h-8 px-3 text-xs has-[>svg]:px-2.5")
    elif size == "lg":
        classes.append("gap-2 h-10 px-6 has-[>svg]:px-4")
    else:
        assert_never(size)

    # Add icon variant if icon_only - use padding=0 and square dimensions
    if icon_only:
        # icon-only variants use square sizing similar to `.btn-icon` classes
        if size == "sm":
            classes.append("p-0 size-8")
        elif size == "lg":
            classes.append("p-0 size-10")
        elif size == "md":
            classes.append("p-0 size-9")
        else:
            assert_never(size)

    # Handle disabled state
    if disabled or loading:
        attrs["disabled"] = "true"

    # Add custom classes
    if class_:
        classes.append(class_)

    # Add classes
    attrs["class_"] = " ".join(classes)

    # Add type
    attrs["type"] = type

    # Button content with optional loading spinner
    if loading:
        # When loading, always show the component spinner and a plain text label.
        # Avoid rendering any svg that might be part of `children` to prevent
        # duplicate spinners (demo had an extra idle icon). We render children
        # inside a plain span to ensure no embedded svg from caller is used.
        content = [
            icon_spinner(class_="h-4 w-4", aria_hidden="true"),
            span()[children],
        ]
    else:
        # If the button contains an svg node as first child (icon+text), keep it
        content = [children]

    return button(**attrs)[*content]
