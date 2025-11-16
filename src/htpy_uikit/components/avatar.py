from htpy import Renderable
from htpy import div
from htpy import img
from htpy import span

from ._types import AvatarImage
from ._types import AvatarSize

_size_classes: dict[AvatarSize, str] = {
    "xs": "size-6",
    "sm": "size-8",
    "md": "size-8",
    "lg": "size-10",
    "xl": "size-12",
}


def avatar(
    *,
    src: str,
    alt: str = "Avatar",
    size: AvatarSize = "md",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render an image avatar with Basecoat sizing tokens.

    Args:
        src: Image source URL.
        alt: Alt text describing the avatar.
        size: Size token mapping to Tailwind ``size-*`` classes.
        class_: Extra CSS classes appended to the ``img`` element.
        **attrs: Additional HTML attributes forwarded to the ``img`` tag.

    Returns:
        Renderable: Configured ``<img>`` node.
    """

    # Base classes - following basecoat avatar styling
    base_classes = "shrink-0 object-cover rounded-full"

    # Combine classes
    classes = f"{base_classes} {_size_classes[size]}"

    if class_:
        classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = classes

    # Add src and alt to attrs
    attrs["src"] = src
    attrs["alt"] = alt

    return img(**attrs)


def avatar_text(
    initials: str, *, size: AvatarSize = "md", class_: str | None = None, **attrs
) -> Renderable:
    """Render an initials avatar fallback as a rounded ``<span>``.

    Args:
        initials: Text or initials displayed inside the avatar.
        size: Size token controlling the diameter.
        class_: Extra CSS classes appended to the span.
        **attrs: Additional HTML attributes forwarded to the span.

    Returns:
        Renderable: Styled ``<span>`` element with initials.
    """

    base = f"{_size_classes[size]} shrink-0 bg-muted flex items-center justify-center rounded-full text-sm font-medium"
    if class_:
        base = f"{base} {class_}"

    attrs["class_"] = base

    return span(**attrs)[initials]


def avatar_group(
    images: list[str] | list[AvatarImage],
    *,
    size: AvatarSize = "sm",
    ring: bool = True,
    grayscale: bool = False,
    hover_expand: bool = False,
    class_: str | None = None,
) -> Renderable:
    """Render overlapping avatar images with optional rings and hover expansion.

    Args:
        images: List of avatar URLs or ``AvatarImage`` dicts with ``src``/``alt``.
        size: Size token applied to each child avatar.
        ring: Whether to render rings (via ``ring-2``) around each avatar.
        grayscale: Whether to desaturate avatars.
        hover_expand: Whether to animate spacing on hover.
        class_: Extra CSS classes appended to the container ``div``.

    Returns:
        Renderable: Stacked avatar ``<div>`` containing ``<img>`` children.
    """
    selectors = []
    # ring styles applied to child imgs
    if ring:
        selectors.append("[&_img]:ring-background")
        selectors.append("[&_img]:ring-2")
    if grayscale:
        selectors.append("[&_img]:grayscale")
    selectors.append(f"[&_img]:{_size_classes[size]}")
    selectors.append("[&_img]:shrink-0")
    selectors.append("[&_img]:object-cover")
    selectors.append("[&_img]:rounded-full")

    if hover_expand:
        selectors.append("hover:space-x-1")
        selectors.append("[&_img]:transition-all")
        selectors.append("[&_img]:duration-300")

    base = "flex -space-x-2 " + " ".join(selectors)
    if class_:
        base = f"{base} {class_}"

    # normalize images to (src, alt)
    normalized: list[tuple[str, str]] = []
    for it in images:
        if isinstance(it, dict):
            normalized.append((it["src"], it["alt"]))
        else:
            normalized.append((it, "Avatar"))

    children = []
    for src, alt in normalized:
        # Build explicit classes for each child image so sizing works even
        # when parent selectors are not picked up by the build.
        child_classes = f"{_size_classes[size]} shrink-0 object-cover rounded-full"
        if ring:
            child_classes += " ring-background ring-2"
        if grayscale:
            child_classes += " grayscale"
        if hover_expand:
            child_classes += " transition-all duration-300 ease-in-out"

        children.append(img(src=src, alt=alt, class_=child_classes))

    return div(class_=base)[*children]
