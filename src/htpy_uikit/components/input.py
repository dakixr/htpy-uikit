from uuid import uuid4

from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import span

from ._styles import INPUT_BASE_CLASSES
from ._types import InputType
from .label import label_component


def input_component(
    *,
    id: str | None = None,
    name: str | None = None,
    type: InputType = "text",
    placeholder: str | None = None,
    value: str | None = None,
    label_text: str | None = None,
    error: str | None = None,
    description: str | None = None,
    invalid: bool = False,
    disabled: bool = False,
    required: bool = False,
    readonly: bool = False,
    autocomplete: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style text input with optional label and helper text.

    Args:
        id: Input id attribute (auto-generated when omitted).
        name: Name attribute for form submissions.
        type: Input type (e.g., ``\"text\"``, ``\"email\"``).
        placeholder: Placeholder string.
        value: Initial value to populate.
        label_text: Optional label displayed above/beside the input.
        error: Error message displayed below the control.
        description: Helper text displayed when ``error`` is absent.
        invalid: Whether to set ``aria-invalid`` regardless of ``error``.
        disabled: Whether the input is disabled.
        required: Whether to mark the input as required.
        readonly: Whether to make the input read-only.
        autocomplete: ``autocomplete`` attribute value.
        class_: Extra CSS classes appended to the ``input`` element.
        **attrs: Additional HTML attributes forwarded to the ``input`` tag.

    Returns:
        Renderable: Input node optionally wrapped with label/error elements.
    """

    # Use shared input base classes
    base_classes = INPUT_BASE_CLASSES

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    # Handle error state with aria-invalid
    if error or invalid:
        attrs["aria-invalid"] = "true"

    # Prepare input attributes
    input_attrs: dict[str, str | bool] = {
        "class_": " ".join(classes),
        "type": type,
    }

    id = id or str(uuid4().hex)
    input_attrs["id"] = id

    if name:
        input_attrs["name"] = name
    if placeholder:
        input_attrs["placeholder"] = placeholder
    if value:
        input_attrs["value"] = value
    if disabled:
        input_attrs["disabled"] = "true"
    if required:
        input_attrs["required"] = "true"
    if readonly:
        input_attrs["readonly"] = "true"
    if autocomplete:
        input_attrs["autocomplete"] = autocomplete
    # Add any additional attributes
    input_attrs.update(attrs)

    # Build the component
    elements = []

    # Add label if provided
    if label_text:
        # Use the shared label component so label styling/behavior is consistent
        # across the codebase (handles peer-disabled and required states).
        elements.append(
            label_component(
                for_=id,
                required=required,
                class_="opacity-50 pointer-events-none" if disabled else None,
            )[label_text]
        )

    # Add input
    elements.append(input_(**input_attrs))

    # Add helper or error message if provided
    if error:
        elements.append(span(class_="text-sm text-destructive", **{"role": "alert"})[error])
    elif description:
        elements.append(span(class_="text-muted-foreground text-sm")[description])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        return div(class_="grid gap-3")[*elements]
