from uuid import uuid4

from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import span

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
    """
    Basecoat-style input component with label, helper text and error states.

    Based on Basecoat UI input component implementation.

    Args:
        id: Input element ID
        name: Input name attribute
        type: Input type
        placeholder: Placeholder text
        value: Default value
        label_text: Label text
        error: Error message to display
        disabled: Disable input
        required: Mark as required
        readonly: Make readonly
        autocomplete: Autocomplete attribute
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy element: Input with optional label and error
    """

    base_classes = (
        "appearance-none file:text-foreground placeholder:text-muted-foreground "
        "selection:bg-primary selection:text-primary-foreground dark:bg-input/30 "
        "border-input flex h-9 w-full min-w-0 rounded-md border bg-transparent "
        "px-3 py-1 text-base shadow-xs transition-[color,box-shadow] outline-none "
        "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm "
        "file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed "
        "disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 "
        "focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
        "aria-invalid:border-destructive"
    )

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
        elements.append(span(class_="text-sm text-red-600", **{"role": "alert"})[error])
    elif description:
        elements.append(span(class_="text-muted-foreground text-sm")[description])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        return div(class_="grid gap-3")[*elements]
