"""
This module provides a Tailwind-first slider component using htpy and Alpine.js.
The component inlines minimal styles and uses an overlay input for accessibility.
"""

from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import label
from htpy import span

from ._utils import merge_classes


def slider(
    *,
    id: str | None = None,
    name: str | None = None,
    value: int = 50,
    min: int = 0,
    max: int = 100,
    step: int = 1,
    disabled: bool = False,
    label_text: str | None = None,
    label_alias: str | None = None,
    show_value: bool = False,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style slider with Alpine-powered cosmetics.

    Args:
        id: Slider id attribute.
        name: Name attribute used for form submissions.
        value: Initial slider value.
        min: Minimum permitted value.
        max: Maximum permitted value.
        step: Step increment between values.
        disabled: Whether the slider is disabled.
        label_text: Optional label displayed next to the slider.
        label_alias: Backwards-compatible alias for ``label_text``.
        show_value: Whether to render the live value text.
        class_: Extra classes appended to the visual track wrapper.
        **attrs: Additional HTML attributes forwarded to the ``input`` element.

    Returns:
        Renderable: Slider control comprised of label, track, and overlay range input.
    """

    # Overlay input (accessible) drives the value; visual parts are Tailwind divs
    input_attrs = {
        "class_": (
            "absolute inset-0 w-full h-6 opacity-0 cursor-pointer appearance-none p-0 outline-none"
        ),
        "type": "range",
        "min": str(min),
        "max": str(max),
        "step": str(step),
        "value": str(value),
        # Use explicit input handler and binding to keep Alpine in sync reliably
        "x-bind:value": "val",
        "@input": "val = +$event.target.value",
        # ARIA for accessibility
        "role": "slider",
        "aria-valuemin": str(min),
        "aria-valuemax": str(max),
        "aria-valuenow": str(value),
        "x-bind:aria-valuenow": "val",
    }

    if id:
        input_attrs["id"] = id
    if name:
        input_attrs["name"] = name
    if disabled:
        # keep string to avoid typing issues; htpy will render the attribute
        input_attrs["disabled"] = "true"

    # Merge provided attrs with input defaults (defaults applied first)
    attrs.update({k: v for k, v in input_attrs.items() if v is not None})

    # Compute final merged class for the wrapper (user's class applies here)
    base_wrapper = "group relative w-full select-none"
    if disabled:
        base_wrapper = base_wrapper + " opacity-60 cursor-not-allowed"
    wrapper_class = merge_classes(base_wrapper, class_)

    # Alpine container that owns the state and updates the CSS variable
    container_attrs = {
        "x-data": f"{{ val: {value} }}",
        "x-effect": f"$el.style.setProperty('--slider-value', (((val-({min}))/(({max})-({min})))*100)+'%')",
        "class_": "flex items-center gap-2 w-full",
    }

    # Build the component
    elements = []

    # Backwards-compatible alias: prefer explicit label_text but accept `label`.
    if label_alias is not None:
        label_text = label_alias

    # Add label if provided
    if label_text:
        elements.append(
            label(
                class_=(
                    "flex items-center gap-2 text-sm leading-none font-medium "
                    "select-none peer-disabled:pointer-events-none peer-disabled:opacity-50"
                ),
            )[label_text]
        )

    # Build the visual-only slider (track + thumb) and overlay input.
    # Keep logic simple: pick the track style, build thumb classes, then assemble.
    track_style = (
        "background: linear-gradient(to right, var(--muted) var(--slider-value), var(--muted) var(--slider-value));"
        if disabled
        else "background: linear-gradient(to right, var(--primary) var(--slider-value), var(--muted) var(--slider-value));"
    )

    thumb_parts = [
        "absolute top-1/2 -translate-y-1/2 -translate-x-1/2",
        "size-4",
        "rounded-full",
    ]
    if disabled:
        thumb_parts += ["border", "border-muted-foreground", "bg-muted", "shrink-0"]
    else:
        thumb_parts += [
            "border",
            "border-primary",
            "bg-background",
            "shadow-sm",
            "shrink-0",
            "group-hover:ring-4",
            "group-focus-within:ring-4",
            "ring-ring/50",
        ]

    thumb_class = " ".join(thumb_parts)

    visual = div(class_=wrapper_class)[
        div(class_="h-1.5 w-full rounded-full", style=track_style),
        div(class_=thumb_class, style="left: var(--slider-value);"),
        input_(**attrs),
    ]

    container_children = [visual]
    if show_value:
        # Show the actual numeric value. If `val` is a percentage string (e.g. "25%"),
        # convert it back to the numeric range; otherwise show `val` directly.
        expr = (
            "(String(val).endsWith('%') ? Math.round(parseFloat(val)/100*({max}-{min})+{min}) : val)"
        ).format(min=min, max=max)
        container_children.append(span(class_="text-sm text-muted-foreground", **{"x-text": expr}))

    elements.append(div(**container_attrs)[*container_children])

    # Value display is handled inside the Alpine container above when requested

    return div(class_="space-y-2")[*elements]
