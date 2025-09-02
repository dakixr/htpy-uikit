from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import form as form_element
from htpy import h3
from htpy import p
from htpy import with_children

from ._types import FormAlign
from ._types import FormMethod


@with_children
def form_component(
    children: Node,
    *,
    action: str | None = None,
    method: FormMethod = "post",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style form wrapper component.

    Based on Basecoat UI form implementation.
    Uses standard HTML form elements with form and grid classes.

    Args:
        children: Form content
        action: Form action URL
        method: Form method (get, post)
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.form: Form element
    """

    # Base classes - inline Tailwind equivalents (replacing Basecoat `.form` class)
    # Replaced `.form` with the equivalent utility classes used by Basecoat's
    # components for inputs, labels, textareas, selects, etc.
    base_classes = "grid gap-6 w-full"

    if class_:
        base_classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = base_classes

    # Prepare form attributes
    form_attrs = {
        "method": method,
    }

    if action:
        form_attrs["action"] = action

    # Add any additional attributes
    form_attrs.update(attrs)

    return form_element(**form_attrs)[children]


# Form sections - following basecoat implementation
def form_section(
    children: Node,
    *,
    title: str | None = None,
    description: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Form section with optional title and description.

    Based on Basecoat UI form section implementation.

    Args:
        children: Section content
        title: Section title
        description: Section description
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Form section
    """

    # Base classes - following basecoat implementation
    base_classes = "grid gap-4"

    if class_:
        base_classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = base_classes

    elements = []

    if title:
        elements.append(h3(class_="text-base leading-normal")[title])

    if description:
        elements.append(p(class_="text-sm text-muted-foreground")[description])

    elements.append(children)

    return div(**attrs)[elements]


# Form field wrapper - following basecoat implementation
@with_children
def form_field(
    children: Node,
    *,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Form field wrapper for consistent spacing.

    Based on Basecoat UI form field implementation.

    Args:
        children: Field content
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Form field wrapper
    """

    # Base classes - following basecoat implementation
    base_classes = "grid gap-2"

    if class_:
        base_classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = base_classes

    return div(**attrs)[children]


# Form actions - following basecoat implementation
@with_children
def form_actions(
    children: Node,
    *,
    align: FormAlign = "right",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Form actions wrapper.

    Based on Basecoat UI form actions implementation.

    Args:
        children: Action buttons
        align: Alignment (left, center, right)
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Form actions wrapper
    """

    # Alignment classes
    alignment_classes = {
        "left": "justify-start",
        "center": "justify-center",
        "right": "justify-end",
    }

    # Base classes - following basecoat implementation
    base_classes = f"flex {alignment_classes.get(align, 'justify-end')} gap-3"

    if class_:
        base_classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = base_classes

    return div(**attrs)[children]
