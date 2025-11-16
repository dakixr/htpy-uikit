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
    """Render a Basecoat-style form wrapper.

    Args:
        children: Form body nodes.
        action: Form submission URL.
        method: HTTP method for submission.
        class_: Extra classes appended to the ``<form>``.
        **attrs: Additional HTML attributes forwarded to the ``form`` element.

    Returns:
        Renderable: ``<form>`` element containing ``children``.
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
    """Render a form section with optional heading text.

    Args:
        children: Section content nodes.
        title: Section heading.
        description: Supporting description text.
        class_: Extra classes appended to the wrapping ``div``.
        **attrs: Additional HTML attributes forwarded to the wrapper.

    Returns:
        Renderable: Section ``div`` containing the provided content.
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
    """Render a field wrapper with consistent spacing.

    Args:
        children: Field nodes.
        class_: Extra classes appended to the wrapper.
        **attrs: Additional HTML attributes forwarded to the wrapper.

    Returns:
        Renderable: Wrapper ``div`` around the field content.
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
    """Render an action-row wrapper for form buttons.

    Args:
        children: Button nodes or other controls.
        align: Horizontal alignment of the action row.
        class_: Extra classes appended to the wrapper ``div``.
        **attrs: Additional HTML attributes forwarded to the wrapper.

    Returns:
        Renderable: Flexbox container for form actions.
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
