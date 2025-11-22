from typing import assert_never

from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import span
from htpy import with_children

from ._styles import (
    BTN_BASE_CLASSES,
    BTN_ICON_LG_CLASSES,
    BTN_ICON_MD_CLASSES,
    BTN_ICON_SM_CLASSES,
    BTN_SIZE_LG_CLASSES,
    BTN_SIZE_MD_CLASSES,
    BTN_SIZE_SM_CLASSES,
    BTN_VARIANT_DESTRUCTIVE_CLASSES,
    BTN_VARIANT_GHOST_CLASSES,
    BTN_VARIANT_LINK_CLASSES,
    BTN_VARIANT_OUTLINE_CLASSES,
    BTN_VARIANT_PRIMARY_CLASSES,
    BTN_VARIANT_SECONDARY_CLASSES,
)
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
    """Render a Basecoat-style button supporting variants, sizes, and loading state.

    Args:
        children: Button content nodes.
        variant: Visual variant (e.g., ``\"primary\"``, ``\"outline\"``).
        size: Button size token controlling height/padding.
        loading: Whether to show the loading spinner and disable the button.
        disabled: Whether the button should be disabled.
        icon_only: Whether to size the button as a square icon button.
        type: ``type`` attribute for the ``<button>`` tag.
        class_: Extra CSS classes appended to the button.
        **attrs: Additional HTML attributes forwarded to the ``button``.

    Returns:
        Renderable: Styled ``<button>`` element.
    """

    # Build class list using shared styles
    classes = [BTN_BASE_CLASSES]

    # Add variant classes
    variant_classes: dict[ButtonVariant, str] = {
        "primary": BTN_VARIANT_PRIMARY_CLASSES,
        "secondary": BTN_VARIANT_SECONDARY_CLASSES,
        "destructive": BTN_VARIANT_DESTRUCTIVE_CLASSES,
        "outline": BTN_VARIANT_OUTLINE_CLASSES,
        "ghost": BTN_VARIANT_GHOST_CLASSES,
        "link": BTN_VARIANT_LINK_CLASSES,
        "danger": BTN_VARIANT_DESTRUCTIVE_CLASSES,  # Alias for destructive
    }
    if variant in variant_classes:
        classes.append(variant_classes[variant])
    else:
        raise ValueError(f"Unsupported button variant: {variant}")

    # Add size classes (only if not icon-only)
    if not icon_only:
        if size == "md":
            classes.append(BTN_SIZE_MD_CLASSES)
        elif size == "sm":
            classes.append(BTN_SIZE_SM_CLASSES)
        elif size == "lg":
            classes.append(BTN_SIZE_LG_CLASSES)
        else:
            assert_never(size)
    else:
        # Icon-only variants use square sizing
        if size == "sm":
            classes.append(BTN_ICON_SM_CLASSES)
        elif size == "lg":
            classes.append(BTN_ICON_LG_CLASSES)
        elif size == "md":
            classes.append(BTN_ICON_MD_CLASSES)
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
