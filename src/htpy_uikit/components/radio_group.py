from typing import assert_never

from htpy import Renderable
from htpy import div
from htpy import fieldset
from htpy import input as input_
from htpy import label

from ._types import RadioCardColor
from ._types import RadioCardOption
from ._types import RadioDirection
from ._types import RadioOption


def radio_group(
    *,
    name: str,
    options: list[RadioOption],
    value: str | None = None,
    label_text: str | None = None,
    description: str | None = None,
    disabled: bool = False,
    required: bool = False,
    error: str | None = None,
    direction: RadioDirection = "vertical",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style radio group component.

    Based on Basecoat UI radio group implementation.
    Uses standard HTML radio inputs with input and label classes.

    Args:
        name: Radio group name
        options: List of RadioOption dictionaries with value and label
        value: Selected value
        label_text: Group label text
        description: Group description text
        disabled: Disable all radio buttons
        required: Mark group as required
        error: Error message to display
        direction: Layout direction (vertical, horizontal)
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Radio group component
    """

    # Base classes (container) – spacing comes from direction
    attrs["class_"] = class_ or ""

    # Container class based on direction - following basecoat pattern
    container_class = "grid gap-3" if direction == "vertical" else "flex gap-3"

    # Build radio elements
    radio_elements = []
    for option in options:
        # Prepare radio button attributes
        radio_attrs: dict[str, str | bool] = {
            "class_": (
                "appearance-none border-input text-primary focus-visible:border-ring focus-visible:ring-ring/50 "
                "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive "
                "dark:bg-input/30 aspect-square size-4 shrink-0 rounded-full border shadow-xs "
                "transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 "
                "relative checked:before:content-[''] checked:before:absolute checked:before:top-1/2 checked:before:left-1/2 "
                "checked:before:-translate-x-1/2 checked:before:-translate-y-1/2 checked:before:rounded-full checked:before:size-2 checked:before:bg-primary"
            ),
            "type": "radio",
            "name": name,
            "value": option["value"],
        }

        if value == option["value"]:
            radio_attrs["checked"] = True
        if disabled:
            radio_attrs["disabled"] = True
        if required:
            radio_attrs["required"] = True

        # Add error styling if error exists
        if error:
            radio_attrs["aria-invalid"] = "true"

        # Create radio button wrapped in label - following basecoat structure
        label_class = (
            "cursor-pointer flex items-center gap-2 text-sm leading-none font-medium "
            "select-none peer-disabled:pointer-events-none peer-disabled:opacity-50"
        )
        if disabled:
            label_class += " opacity-50 pointer-events-none"

        radio_element = label(class_=label_class)[input_(**radio_attrs), option["label"]]

        radio_elements.append(radio_element)

    # Build the component
    elements = []

    # Add group label if provided
    if label_text:
        elements.append(label(class_="text-base leading-normal")[label_text])

    # Add group description if provided
    if description:
        elements.append(div(class_="text-sm text-muted-foreground")[description])

    # Add radio buttons in container with basecoat class pattern
    elements.append(div(class_=container_class)[*radio_elements])

    # Add error message if provided
    if error:
        elements.append(div(class_="text-sm text-red-600", **{"role": "alert"})[error])

    # Use fieldset if we have a group label, otherwise use div - following basecoat pattern
    if label_text:
        # Add fieldset-specific attributes following basecoat pattern
        fieldset_attrs = attrs.copy()
        if "class_" not in fieldset_attrs:
            fieldset_attrs["class_"] = container_class
        else:
            fieldset_attrs["class_"] = f"{container_class} {fieldset_attrs['class_']}"

        return fieldset(**fieldset_attrs)[*elements]
    else:
        return div(**attrs)[*elements]


def radio_group_cards(
    *,
    name: str,
    options: list[RadioCardOption],
    value: str | None = None,
    disabled: bool = False,
    required: bool = False,
    error: str | None = None,
    class_: str | None = None,
    card_color: RadioCardColor = "green",
    **attrs,
) -> Renderable:
    """
    Card-style radio group. Each option is a bordered card that highlights on selection.

    Args:
        name: Radio group name shared by all inputs
        options: List of RadioCardOption dictionaries with value, title, and description
        value: Selected value
        disabled: Disable all radios
        required: Mark as required
        error: Error text
        class_: Additional classes for the fieldset container
        card_color: Color theme for checked state (border/background)
    """

    # Wrapper label classes and checked-state variants per color
    if card_color == "green":
        wrapper_classes_checked = (
            "has-[input[type='radio']:checked]:border-green-600 has-[input[type='radio']:checked]:bg-green-50 "
            "dark:has-[input[type='radio']:checked]:border-green-900 dark:has-[input[type='radio']:checked]:bg-green-950"
        )
        input_classes_checked = (
            "checked:bg-green-600 checked:border-green-600 dark:checked:bg-input/30 "
            "checked:before:bg-background dark:checked:before:bg-primary"
        )
    elif card_color == "blue":
        wrapper_classes_checked = (
            "has-[input[type='radio']:checked]:border-blue-600 has-[input[type='radio']:checked]:bg-blue-50 "
            "dark:has-[input[type='radio']:checked]:border-blue-900 dark:has-[input[type='radio']:checked]:bg-blue-950"
        )
        input_classes_checked = (
            "checked:bg-blue-600 checked:border-blue-600 dark:checked:bg-input/30 "
            "checked:before:bg-background dark:checked:before:bg-primary"
        )
    elif card_color == "red":
        wrapper_classes_checked = (
            "has-[input[type='radio']:checked]:border-red-600 has-[input[type='radio']:checked]:bg-red-50 "
            "dark:has-[input[type='radio']:checked]:border-red-900 dark:has-[input[type='radio']:checked]:bg-red-950"
        )
        input_classes_checked = (
            "checked:bg-red-600 checked:border-red-600 dark:checked:bg-input/30 "
            "checked:before:bg-background dark:checked:before:bg-primary"
        )
    else:
        assert_never(card_color)

    fieldset_classes = "grid gap-3"
    if class_:
        fieldset_classes = f"{fieldset_classes} {class_}"

    cards: list[Renderable] = []
    for option in options:
        input_classes = (
            "appearance-none border-input text-primary focus-visible:border-ring focus-visible:ring-ring/50 "
            "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive "
            "dark:bg-input/30 aspect-square size-4 shrink-0 rounded-full border shadow-xs transition-[color,box-shadow] "
            "outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 relative "
            "checked:before:content-[''] checked:before:absolute checked:before:top-1/2 checked:before:left-1/2 "
            "checked:before:-translate-x-1/2 checked:before:-translate-y-1/2 checked:before:rounded-full checked:before:size-2 "
            f"{input_classes_checked}"
        )

        radio_attrs: dict[str, str | bool] = {
            "class_": input_classes,
            "type": "radio",
            "name": name,
            "value": option["value"],
        }
        if value == option["value"]:
            radio_attrs["checked"] = True
        if disabled:
            radio_attrs["disabled"] = True
        if required:
            radio_attrs["required"] = True
        if error:
            radio_attrs["aria-invalid"] = "true"

        wrapper_classes_base = (
            "label flex gap-3 items-start hover:bg-accent/50 "
            f"rounded-lg border border-border p-4 {wrapper_classes_checked} "
        )

        if not disabled:
            wrapper_classes_base += "cursor-pointer"
        else:
            wrapper_classes_base += "cursor-not-allowed pointer-events-none opacity-50"

        cards.append(
            label(class_=wrapper_classes_base)[
                input_(**radio_attrs),
                div(class_="grid gap-1 font-normal")[
                    div(class_="font-medium")[option["title"]],
                    option["description"]
                    and div(class_="text-muted-foreground leading-snug")[option["description"]],
                ],
            ]
        )

    children: list[Renderable] = [*cards]
    if error:
        children.append(div(class_="text-sm text-red-600", **{"role": "alert"})[error])

    return fieldset(class_=fieldset_classes, **attrs)[*children]
