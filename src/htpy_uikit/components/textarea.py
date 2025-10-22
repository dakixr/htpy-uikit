from uuid import uuid4

from htpy import Renderable
from htpy import div
from htpy import span
from htpy import textarea

from .label import label_component


def textarea_component(
    *,
    id: str | None = None,
    name: str | None = None,
    placeholder: str | None = None,
    value: str | None = None,
    label_text: str | None = None,
    error: str | None = None,
    disabled: bool = False,
    required: bool = False,
    readonly: bool = False,
    rows: int = 3,
    cols: int | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style textarea component with label and error states.

    Based on Basecoat UI textarea component implementation.

    Args:
        id: Textarea element ID
        name: Textarea name attribute
        placeholder: Placeholder text
        value: Default value
        label_text: Label text
        error: Error message to display
        disabled: Disable textarea
        required: Mark as required
        readonly: Make readonly
        rows: Number of visible text lines
        cols: Number of visible text columns
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy element: Textarea with optional label and error
    """

    # Base classes - using Tailwind equivalent of Basecoat textarea
    base_classes = (
        "border-input placeholder:text-muted-foreground focus-visible:border-ring "
        "focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 "
        "dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive "
        "dark:bg-input/30 flex min-h-16 w-full rounded-md field-sizing-content"
        "border bg-transparent px-3 py-2 text-base shadow-xs transition-[color,box-shadow] "
        "outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 md:text-sm"
    )

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    # Handle error state with aria-invalid
    if error:
        attrs["aria-invalid"] = "true"

    # Prepare textarea attributes
    textarea_attrs = {
        "class_": " ".join(classes),
        "rows": str(rows),
    }

    if id is None:
        id = uuid4().hex

    textarea_attrs["id"] = id

    if name:
        textarea_attrs["name"] = name
    if placeholder:
        textarea_attrs["placeholder"] = placeholder
    if cols:
        textarea_attrs["cols"] = str(cols)
    if disabled:
        textarea_attrs["disabled"] = "true"
    if required:
        textarea_attrs["required"] = "true"
    if readonly:
        textarea_attrs["readonly"] = "true"

    # Add any additional attributes
    textarea_attrs.update(attrs)

    # Build the component
    elements = []

    # Add label if provided
    if label_text:
        assert id is not None, "id is required when label_text is provided"
        elements.append(label_component(class_="label", for_=id, required=required)[label_text])

    # Add textarea with value if provided
    if value:
        elements.append(textarea(**textarea_attrs)[value])
    else:
        elements.append(textarea(**textarea_attrs))

    # Add error message if provided
    if error:
        elements.append(span(class_="text-sm text-red-600", **{"role": "alert"})[error])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        return div(class_="space-y-1")[*elements]
