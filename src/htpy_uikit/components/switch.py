import uuid

from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import label

from ._types import TColor
from ._utils import merge_classes
from .label import label_component


def switch(
    *,
    id: str | None = None,
    name: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    label_text: str | None = None,
    description: str | None = None,
    class_: str | None = None,
    value: str = "true",
    color: TColor = "primary",
    **attrs,
) -> Renderable:
    """Render a Basecoat-style switch (checkbox) with optional text.

    Args:
        id: Switch id attribute (generated when omitted).
        name: Name attribute for form submissions.
        checked: Whether the switch starts in the on position.
        disabled: Whether the switch is disabled.
        label_text: Optional label rendered next to the switch.
        description: Supporting text displayed under the label.
        class_: Extra classes appended to the switch input.
        value: Submitted value when the switch is checked.
        color: Token controlling the checked background color.
        **attrs: Additional HTML attributes forwarded to the ``input`` element.

    Returns:
        Renderable: Switch input alone or wrapped with label/description content.
    """

    # Merge user classes with the input base so overrides are preserved.
    # Inline full tailwind classes from reference for switches.
    # Color-specific classes are appended based on `color`.
    base_switch_classes = (
        "input cursor-pointer appearance-none focus-visible:border-ring focus-visible:ring-ring/50 "
        "inline-flex h-[1.15rem] w-8 shrink-0 items-center rounded-full border "
        "border-border shadow-xs transition-all outline-none focus-visible:ring-[3px] "
        "disabled:cursor-not-allowed disabled:opacity-50 bg-input "
        "before:content-[''] before:pointer-events-none before:block before:size-4 before:rounded-full "
        "before:ring-0 before:transition-all before:bg-background "
        "checked:before:ms-3.5"
    )

    color_classes_map: dict[TColor, str] = {
        "primary": "checked:bg-primary checked:before:bg-primary-foreground",
        "blue": "checked:bg-blue-600 checked:before:bg-white",
        "green": "checked:bg-green-600 checked:before:bg-white",
        "red": "checked:bg-red-600 checked:before:bg-white",
    }
    color_classes = color_classes_map[color]

    switch_attrs = {
        "class_": merge_classes(f"{base_switch_classes} {color_classes}", class_),
        "type": "checkbox",
        "role": "switch",
    }

    if not id:
        id = f"switch-{uuid.uuid4().hex[:8]}"

    switch_attrs["id"] = id

    if name:
        switch_attrs["name"] = name
    if checked:
        switch_attrs["checked"] = "true"
    if disabled:
        switch_attrs["disabled"] = "true"
    switch_attrs["value"] = value

    # Add any additional attributes
    switch_attrs.update(attrs)

    # Build the component following basecoat pattern
    if label_text:
        # Render similar to checkbox: input then a separate label(for=) so the
        # text block is clickable and accessible. This mirrors the working
        # pattern in `checkbox_component`.
        container_class = "flex items-center gap-3"

        # Build left text block
        text_block = div[
            label(for_=id, class_="leading-normal select-none cursor-pointer")[label_text],
            (div(class_="text-sm text-muted-foreground")[description] if description else None),
        ]

        row = (div(class_="opacity-50 pointer-events-none") if disabled else div())[
            div(class_=container_class)[input_(**switch_attrs), text_block]
        ]

        return row
    else:
        # Simple switch without label
        return input_(**switch_attrs)


def switch_card(
    *,
    id: str | None = None,
    name: str | None = None,
    checked: bool = False,
    disabled: bool = False,
    label_text: str | None = None,
    description: str | None = None,
    class_: str | None = None,
    color: TColor = "primary",
    **attrs,
) -> Renderable:
    """Render a card-style switch row with the control aligned to the right.

    Args:
        id: Switch id (generated when omitted).
        name: Name attribute used for form submissions.
        checked: Whether the switch is initially on.
        disabled: Whether interaction is disabled.
        label_text: Heading text on the left.
        description: Supporting description.
        class_: Extra classes appended to the switch input.
        color: Color token controlling the peer-checked border.
        **attrs: Additional attributes forwarded to ``switch``.

    Returns:
        Renderable: Label-wrapped card row containing the switch.
    """
    # container classes per reference and reserve space on the right for the switch
    # base container classes; we'll append a peer-checked border class matching the color
    container_classes_base = (
        "w-full gap-2 flex flex-row items-center justify-between rounded-lg border border-border "
        "p-4 shadow-xs pr-16"
    )

    border_map: dict[TColor, str] = {
        "primary": "peer-checked:border-primary",
        "blue": "peer-checked:border-blue-600",
        "green": "peer-checked:border-green-600",
        "red": "peer-checked:border-red-600",
    }

    container_classes = f"{container_classes_base} {border_map[color]}"

    left_classes = "flex flex-col gap-0.5"
    # dim the left column when disabled
    if disabled:
        left_classes += " opacity-60"

    # Ensure we have a stable id so the left label (for=) points to the same input.
    if not id:
        id = f"switch-{uuid.uuid4().hex[:8]}"

    # Build the input and position it absolutely inside a relative wrapper
    input_position_classes = "peer absolute right-4 top-1/2 -translate-y-1/2 z-10"
    input_node = switch(
        id=id,
        name=name,
        checked=checked,
        disabled=disabled,
        class_=merge_classes(input_position_classes, class_),
        color=color,
        **attrs,
    )

    # Use a relative wrapper for positioning and place input inside the card
    # so it visually sits on the right edge while still preceding the card for peer styles.
    return div(class_="relative w-full")[
        label_component(class_="relative block w-full cursor-pointer", for_=id)[
            input_node,
            div(class_=container_classes)[
                div(class_=left_classes)[
                    label_text,
                    div(class_="text-sm text-muted-foreground")[description]
                    if description
                    else None,
                ],
            ],
        ]
    ]
