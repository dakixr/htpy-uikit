from uuid import uuid4

from htpy import Renderable
from htpy import div
from htpy import span
from htpy import textarea

from ._styles import INPUT_BASE_CLASSES
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
    """Render a Basecoat-style textarea with optional label and error text.

    Args:
        id: Textarea id attribute (auto-generated when omitted).
        name: Name attribute for form submissions.
        placeholder: Placeholder text.
        value: Initial textarea value.
        label_text: Optional label rendered above the textarea.
        error: Error message rendered below the field.
        disabled: Whether the textarea is disabled.
        required: Whether to set ``required``.
        readonly: Whether the textarea is read-only.
        rows: Visible row count.
        cols: Visible column count.
        class_: Extra classes appended to the ``textarea`` element.
        **attrs: Additional HTML attributes forwarded to the textarea.

    Returns:
        Renderable: Textarea node optionally wrapped with label/error nodes.
    """

    # Use shared input base classes (textarea shares same styling as input)
    # Adjust height and padding for multi-line input
    base_classes = INPUT_BASE_CLASSES.replace("h-9", "min-h-[60px]").replace("py-1", "py-2")

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    # Handle error state with aria-invalid
    if error:
        attrs["aria-invalid"] = "true"

    # Prepare textarea attributes
    textarea_attrs: dict[str, str | bool] = {
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
        elements.append(
            label_component(
                for_=id,
                required=required,
                class_="opacity-50 pointer-events-none" if disabled else None,
            )[label_text]
        )

    # Add textarea with value if provided
    if value:
        elements.append(textarea(**textarea_attrs)[value])
    else:
        elements.append(textarea(**textarea_attrs))

    # Add error message if provided
    if error:
        elements.append(span(class_="text-sm text-destructive", **{"role": "alert"})[error])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        return div(class_="grid gap-3")[*elements]
