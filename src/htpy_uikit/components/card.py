from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import footer as footer_
from htpy import h2
from htpy import header
from htpy import p
from htpy import section
from htpy import with_children

from ._styles import CARD_BASE_CLASSES


@with_children
def card(
    children: Node,
    *,
    title: str | None = None,
    description: str | None = None,
    action: Node | None = None,
    footer_content: Node | None = None,
    class_: str | None = None,
    header_class: str | None = None,
    section_class: str | None = None,
    footer_class: str | None = None,
    bordered_header: bool = False,
    bordered_footer: bool = False,
    **attrs,
) -> Renderable:
    """Render a Basecoat-inspired card layout with optional header and footer.

    Args:
        children: Content rendered inside the card body ``<section>``.
        title: Optional header title.
        description: Optional header description text.
        action: Optional renderable placed in the header action slot.
        footer_content: Optional node rendered inside the footer.
        class_: Extra classes appended to the outer card container.
        header_class: Extra classes appended to the header.
        section_class: Extra classes appended to the body section.
        footer_class: Extra classes appended to the footer.
        bordered_header: Whether to add a bottom border/padding to the header.
        bordered_footer: Whether to add a top border/padding to the footer.
        **attrs: Additional HTML attributes forwarded to the card container.

    Returns:
        Renderable: Card ``<div>`` containing optional header, content, and footer.
    """

    # Container classes
    # Use the same border token as `alert` for consistency and visibility.
    # Keep padding on header/section/footer so the container itself doesn't add extra px.
    # Add container padding so the card contents have consistent inner spacing
    base_classes = f"{CARD_BASE_CLASSES} p-6"
    classes = [base_classes]
    if class_:
        classes.append(class_)

    # Apply container classes
    attrs["class_"] = " ".join(classes)

    nodes: list[Renderable] = []

    # Header (render only if any header piece present)
    if title or description or action:
        header_classes = (
            "@container/card-header grid auto-rows-min grid-rows-[auto_auto] "
            "items-start gap-1.5 has-data-[slot=card-action]:grid-cols-[1fr_auto]"
        )
        if bordered_header:
            header_classes += " border-b border-border pb-6"
        if header_class:
            header_classes += f" {header_class}"

        header_children: list[Renderable] = []
        # Title and description stack
        if title:
            header_children.append(h2(class_="leading-none font-semibold")[title])
        if description:
            header_children.append(p(class_="text-muted-foreground text-sm")[description])
        # Action on the right
        if action:
            header_children.append(div({"data_slot": "card-action"})[action])

        nodes.append(header(class_=header_classes)[*header_children])

    # Section
    sec_classes = "flex flex-col gap-6"
    if section_class:
        sec_classes = f"{sec_classes} {section_class}"
    nodes.append(section(class_=sec_classes)[children])

    # Footer
    if footer_content is not None:
        footer_classes = "flex items-center"
        if bordered_footer:
            footer_classes += " border-t border-border pt-6"
        if footer_class:
            footer_classes += f" {footer_class}"
        nodes.append(footer_(class_=footer_classes)[footer_content])

    return div(**attrs)[*nodes]


@with_children
def card_with_header(
    children: Node,
    *,
    title: str | None = None,
    description: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a card with a populated header.

    Args:
        children: Card body content.
        title: Header title.
        description: Header description.
        class_: Extra classes for the card container.
        **attrs: Additional attributes forwarded to ``card``.

    Returns:
        Renderable: Card ``<div>`` with header and body content.
    """

    # Use the unified card() with proper header handling
    return card(title=title, description=description, class_=class_, **attrs)[children]


@with_children
def card_with_footer(
    children: Node,
    footer_content: Node,
    *,
    title: str | None = None,
    description: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a card with header, body, and footer sections.

    Args:
        children: Body content.
        footer_content: Node rendered inside the footer.
        title: Header title.
        description: Header description.
        class_: Extra classes appended to the card container.
        **attrs: Additional attributes forwarded to ``card``.

    Returns:
        Renderable: Card ``<div>`` with header and footer.
    """

    # Use the unified card() with footer
    return card(
        title=title,
        description=description,
        footer_content=footer_content,
        class_=class_,
        **attrs,
    )[children]


# Convenience functions for common card patterns - following basecoat implementation
def card_simple(children: Node, **kwargs) -> Renderable:
    """Render a simple card containing only body content.

    Args:
        children: Body content nodes.
        **kwargs: Additional keyword arguments forwarded to ``card``.

    Returns:
        Renderable: Card without header/footer sections.
    """
    return card(**kwargs)[children]


def card_header_only(
    title: str | None = None, description: str | None = None, **kwargs
) -> Renderable:
    """Render a card that only displays the header content.

    Args:
        title: Header title.
        description: Header description.
        **kwargs: Additional keyword arguments forwarded to ``card_with_header``.

    Returns:
        Renderable: Card whose body is empty.
    """
    return card_with_header(
        title=title,
        description=description,
        **kwargs,
    )[div()]  # Empty content


def card_content_only(children: Node, **kwargs) -> Renderable:
    """Render a card without header or footer regions.

    Args:
        children: Body content nodes.
        **kwargs: Additional keyword arguments forwarded to ``card``.

    Returns:
        Renderable: Card containing only the provided content.
    """
    return card(**kwargs)[children]


# Card sections for complex layouts - simplified for basecoat
def card_section_header(children: Node, **attrs) -> Renderable:
    """Render a ``<header>`` element suitable for card sub-sections.

    Args:
        children: Header content nodes.
        **attrs: Additional HTML attributes forwarded to the ``<header>`` element.

    Returns:
        Renderable: Header node.
    """
    return header(**attrs)[children]


def card_section_footer(children: Node, **attrs) -> Renderable:
    """Card footer section."""
    return footer_(**attrs)[children]
