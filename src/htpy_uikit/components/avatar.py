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
    """
    Basecoat-style avatar component.

    Based on Basecoat UI avatar implementation.
    Note: Basecoat doesn't have a dedicated avatar component,
    this uses standard img elements with avatar styling.

    Args:
        src: Image source URL
        alt: Image alt text
        size: Avatar size
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.img: Avatar image element
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
    """Render an initials avatar (fallback) as a centered rounded span.

    Args:
        initials: Text to show inside the avatar (e.g. "CN")
        size: Avatar size key (xs, sm, md, lg, xl)
        class_: Extra classes to append
        **attrs: Additional attributes for the span
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
    """Render a stacked avatar group.

    images may be list of src strings or AvatarImage dictionaries with src and alt.
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
