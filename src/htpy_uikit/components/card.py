from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import footer as footer_
from htpy import h2
from htpy import header
from htpy import p
from htpy import section
from htpy import with_children


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
    """Card component matching Basecoat reference styles.

    Structure rendered:
    <div class="card">
      <header> (optional)
        <h2> (optional)
        <p>  (optional)
        <slot data-slot="card-action"> (optional)
      </header>
      <section>children</section>
      <footer> (optional)</footer>
    </div>

    Args:
        children: Inner content for the card's <section>.
        title: Optional header title.
        description: Optional header description.
        action: Optional node rendered on the right side of header.
        footer: Optional node for the footer area.
        class_: Extra classes for the card container.
        header_class: Extra classes for the header.
        section_class: Extra classes for the content section.
        footer_class: Extra classes for the footer.
        bordered_header: If True, add a bottom border to header (with extra padding).
        bordered_footer: If True, add a top border to footer (with extra padding).
        **attrs: Additional HTML attributes for the container.
    """

    # Container classes
    # Use the same border token as `alert` for consistency and visibility.
    # Keep padding on header/section/footer so the container itself doesn't add extra px.
    # Add container padding so the card contents have consistent inner spacing
    base_classes = "bg-card text-card-foreground flex flex-col gap-6 rounded-xl border border-border shadow-sm p-6"
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
    sec_classes = ""
    if section_class:
        sec_classes = f"{sec_classes} {section_class}"
    nodes.append(section(class_=sec_classes)[children])

    # Footer
    if footer_content is not None:
        footer_classes = "flex items-center"
        if bordered_footer:
            footer_classes += " border-t pt-6"
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
    """
    Card with header section.

    Args:
        children: Card content
        title: Card title
        description: Card description
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Card with header
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
    """
    Card with header and footer sections.

    Args:
        children: Card content
        footer_content: Footer content
        title: Card title
        description: Card description
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Card with header and footer
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
    """Simple card without header."""
    return card(**kwargs)[children]


def card_header_only(
    title: str | None = None, description: str | None = None, **kwargs
) -> Renderable:
    """Card with only header content."""
    return card_with_header(
        title=title,
        description=description,
        **kwargs,
    )[div()]  # Empty content


def card_content_only(children: Node, **kwargs) -> Renderable:
    """Card with only content (no header/footer)."""
    return card(**kwargs)[children]


# Card sections for complex layouts - simplified for basecoat
def card_section_header(children: Node, **attrs) -> Renderable:
    """Card header section."""
    return header(**attrs)[children]


def card_section_footer(children: Node, **attrs) -> Renderable:
    """Card footer section."""
    return footer_(**attrs)[children]
