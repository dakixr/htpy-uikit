from typing import Literal
from typing import assert_never

from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import label
from htpy import p
from htpy import span


def checkbox_component(
    *,
    id: str | None = None,
    name: str | None = None,
    value: str | None = None,
    label_text: str | None = None,
    description: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    error: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style checkbox with optional label and description.

    Args:
        id: Element id applied to the checkbox.
        name: Name attribute for form submissions.
        value: Value submitted when checked.
        label_text: Optional label text.
        description: Optional supporting text displayed under the label.
        checked: Whether the checkbox is initially checked.
        disabled: Whether the checkbox is disabled.
        required: Whether to set the ``required`` attribute.
        error: Optional error message appended below the field.
        class_: Extra CSS classes appended to the checkbox input.
        **attrs: Additional HTML attributes forwarded to the checkbox input.

    Returns:
        Renderable: Checkbox, label/description, and error nodes.
    """

    # Base classes – Tailwind utilities matching Basecoat checkbox styles
    # Checked indicator using :after pseudo-element with mask icon
    base_classes = (
        "appearance-none cursor-pointer border-input bg-card checked:bg-primary checked:border-primary "
        "focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 aria-invalid:border-destructive "
        "size-4 shrink-0 rounded-[4px] border shadow-xs transition-shadow outline-none focus-visible:ring-[3px] "
        "disabled:cursor-not-allowed disabled:opacity-50 "
        "checked:after:content-[''] checked:after:block checked:after:size-3.5 checked:after:bg-primary-foreground "
        "checked:after:mask-(--check-icon) checked:after:mask-size-[0.875rem] checked:after:mask-no-repeat checked:after:mask-center"
    )

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    # Handle error state with aria-invalid
    if error:
        attrs["aria-invalid"] = "true"

    # Prepare checkbox attributes
    checkbox_attrs: dict[str, str | bool] = {
        "class_": " ".join(classes),
        "type": "checkbox",
        "value": value or "on",
    }

    if id:
        checkbox_attrs["id"] = id
    if name:
        checkbox_attrs["name"] = name
    if checked:
        checkbox_attrs["checked"] = True
    if disabled:
        checkbox_attrs["disabled"] = True
    if required:
        checkbox_attrs["required"] = True

    # Add any additional attributes
    checkbox_attrs.update(attrs)

    # Build the component
    elements = []

    # Default inline checkbox with right-aligned label/description block
    container_class = "flex items-start gap-3" if description else "flex items-center gap-3"
    # Nudge checkbox down slightly when we have a description so titles align visually
    if description:
        checkbox_attrs["class_"] = f"{checkbox_attrs['class_']} mt-1"
    row = div(class_=("opacity-50 pointer-events-none" if disabled else None))[
        div(class_=container_class)[
            input_(**checkbox_attrs),
            div[
                label_text
                and label(
                    class_="leading-snug select-none cursor-pointer",
                    **({"for": id} if id else {}),
                )[label_text],
                description and p(class_="text-muted-foreground text-sm leading-snug")[description],
            ]
            if label_text or description
            else None,
        ]
    ]
    elements.append(row)

    # Add error message if provided
    if error:
        elements.append(span(class_="text-sm text-destructive", **{"role": "alert"})[error])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        return div(class_="space-y-1")[*elements]


def checkbox_card_component(
    *,
    id: str | None = None,
    name: str | None = None,
    value: str | None = None,
    label_text: str | None = None,
    description: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    required: bool = False,
    error: str | None = None,
    card_color: Literal["blue", "green", "red"] = "blue",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a card-style checkbox where the entire card toggles state.

    Args:
        id: Element id for the checkbox input.
        name: Name attribute used for form submissions.
        value: Value submitted when checked.
        label_text: Primary text displayed inside the card.
        description: Supporting text displayed under the label.
        checked: Whether the checkbox is initially checked.
        disabled: Whether interaction is disabled.
        required: Whether the checkbox is required.
        error: Optional error string for ``aria-invalid``.
        card_color: Tone that controls checked/hover colors.
        class_: Additional classes appended to the card inner container.
        **attrs: Additional attributes forwarded to the wrapping label.

    Returns:
        Renderable: Checkbox card node.
    """
    # Base input classes (same as reference "input" class)
    # Position the checkbox absolutely so it appears inside the card area
    input_classes = (
        "peer absolute left-4 top-4 z-20 appearance-none border-input bg-card checked:bg-primary checked:border-primary "
        "focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 aria-invalid:border-destructive "
        "size-4 shrink-0 rounded-[4px] border shadow-xs transition-shadow outline-none focus-visible:ring-[3px] "
        "disabled:cursor-not-allowed disabled:opacity-50 "
        "checked:after:content-[''] checked:after:block checked:after:size-3.5 checked:after:bg-primary-foreground "
        "checked:after:mask-(--check-icon) checked:after:mask-size-[0.875rem] checked:after:mask-no-repeat checked:after:mask-center"
    )

    # Wrapper label acts as the clickable card (visual container)
    if not disabled:
        wrapper_classes = (
            "relative cursor-pointer select-none flex items-start gap-3 rounded-md p-0"
        )
    else:
        wrapper_classes = "relative cursor-not-allowed select-none flex items-start gap-3 rounded-md p-0 opacity-50 pointer-events-none"

    # Build input attributes (we'll use a visually hidden input that is a peer)
    checkbox_attrs: dict[str, str | bool] = {
        "class_": input_classes,
        "type": "checkbox",
        "value": value or "on",
    }
    if id:
        checkbox_attrs["id"] = id
    if name:
        checkbox_attrs["name"] = name
    if checked:
        checkbox_attrs["checked"] = True
    if disabled:
        checkbox_attrs["disabled"] = True
    if required:
        checkbox_attrs["required"] = True
    if error:
        attrs["aria-invalid"] = "true"

    # Determine card-inner classes to color full card area on checked state and hover effects.
    # Light theme keeps colored tints; dark theme uses softer, token-based overlays.
    if card_color == "blue":
        classes_card_checked = "peer-checked:bg-blue-700/30 peer-checked:border-blue-700/60"
        classes_card_hover = (
            "peer-not-checked:hover:bg-blue-50 peer-not-checked:hover:border-blue-200 "
            "dark:peer-not-checked:hover:bg-accent/20 dark:peer-not-checked:hover:border-border"
        )
    elif card_color == "green":
        classes_card_checked = "peer-checked:bg-green-700/30 peer-checked:border-green-700/60"
        classes_card_hover = (
            "peer-not-checked:hover:bg-green-50 peer-not-checked:hover:border-green-200 "
            "dark:peer-not-checked:hover:bg-accent/20 dark:peer-not-checked:hover:border-border"
        )
    elif card_color == "red":
        classes_card_checked = "peer-checked:bg-red-700/30 peer-checked:border-red-700/60"
        classes_card_hover = (
            "peer-not-checked:hover:bg-red-50 peer-not-checked:hover:border-red-200 "
            "dark:peer-not-checked:hover:bg-accent/20 dark:peer-not-checked:hover:border-border"
        )
    else:
        assert_never(card_color)

    card_inner_classes = (
        "w-full rounded-md border border-input p-3 pl-12 shadow-xs transition-colors "
        f"{classes_card_checked} {classes_card_hover} peer-checked:after:bg-white {class_ or ''}"
    )

    # Place the input first (peer) then the inner card that reacts to peer-checked
    return label(class_=wrapper_classes)[
        input_(**checkbox_attrs),
        div(class_=card_inner_classes)[
            div(class_="grid gap-2")[
                label_text and span(class_="text-sm leading-none font-medium")[label_text],
                description and p(class_="text-muted-foreground text-sm")[description],
            ],
        ],
    ]
