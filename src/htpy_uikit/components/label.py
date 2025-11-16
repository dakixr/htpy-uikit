from htpy import Node
from htpy import Renderable
from htpy import label
from htpy import span
from htpy import with_children


@with_children
def label_component(
    children: Node,
    *,
    for_: str,
    required: bool = False,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a label with Basecoat utility classes.

    Args:
        children: Text or nodes displayed inside the label.
        for_: Id of the form control associated with the label.
        required: Whether to append a ``*`` indicator.
        class_: Extra classes appended to the label element.
        **attrs: Additional HTML attributes forwarded to ``<label>``.

    Returns:
        Renderable: Styled ``<label>`` node.
    """

    # Base classes - follow reference utility classes so we don't rely on
    # a global `.label` CSS token. This mirrors the reference:
    # flex items-center gap-2 text-sm leading-none font-medium select-none
    # peer-disabled:pointer-events-none peer-disabled:opacity-50
    base_classes = (
        "flex items-center gap-2 text-sm leading-none font-medium select-none "
        "peer-disabled:pointer-events-none peer-disabled:opacity-50"
    )

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    attrs["class_"] = " ".join(classes)

    attrs["for"] = for_

    # Handle required indicator
    if required:
        content = [children, span(class_="font-bold")["*"]]
    else:
        content = [children]

    return label(**attrs)[*content]


# Convenience function for required labels - following basecoat implementation
def required_label(children: Node, **kwargs) -> Renderable:
    """Render a label that always shows the required indicator."""
    return label_component(required=True, **kwargs)[children]
