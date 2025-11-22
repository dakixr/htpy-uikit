from htpy import Renderable
from htpy import div
from htpy import h2
from htpy import section

from ._styles import ALERT_BASE_CLASSES
from ._styles import ALERT_DESTRUCTIVE_CLASSES
from ._types import AlertVariant
from ._utils import merge_classes
from .icons import icon_circle_alert
from .icons import icon_circle_check
from .icons import icon_info


def alert(
    *,
    title: str,
    description: str | None = None,
    variant: AlertVariant,
    show_icon: bool = True,
    icon: Renderable | None = None,
    target_id: str | None = None,
    class_: str | None = None,
) -> Renderable:
    """Render a Basecoat-style alert with optional icon and description.

    Args:
        title: Primary alert text.
        description: Optional supporting description.
        variant: Visual variant; controls tone and icon (e.g., ``\"destructive\"``).
        show_icon: Whether to render a contextual icon.
        icon: Override icon renderable (takes precedence over ``variant`` default).
        target_id: Optional id and HTMX swap target when replacing alerts dynamically.
        class_: Additional CSS classes appended to the alert container.

    Returns:
        Renderable: ``<div role=\"alert\">`` tree that matches Basecoat styling.
    """

    # Use shared alert base classes
    root_base_classes = ALERT_BASE_CLASSES

    # Tone classes control text color; destructive uses the destructive token.
    tone_classes = ALERT_DESTRUCTIVE_CLASSES if variant == "destructive" else "text-card-foreground"

    classes_inline = merge_classes(f"{root_base_classes} {tone_classes}", class_)

    root_attrs: dict[str, str] = {"class_": classes_inline, "role": "alert"}
    if target_id:
        root_attrs.update({"id": target_id, "hx-swap-oob": "true", "hx-swap": "transition:true"})

    # Choose icon: prefer injected `icon` if provided, otherwise fall back to
    # the default one based on variant when `show_icon` is True.
    chosen_icon: Renderable | None = None
    if icon is not None:
        chosen_icon = icon
    elif show_icon:
        if variant == "destructive":
            chosen_icon = icon_circle_alert()
        elif variant == "success":
            chosen_icon = icon_circle_check()
        else:
            chosen_icon = icon_info()

    children: list[Renderable] = []
    if chosen_icon is not None:
        children.append(chosen_icon)

    # Title and description with inline styles per reference
    children.append(h2(class_="col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight")[title])
    if description:
        section_base = "col-start-2 grid justify-items-start gap-1 text-sm [&_p]:leading-relaxed"
        section_tone = "text-destructive" if variant == "destructive" else "text-muted-foreground"
        children.append(section(class_=f"{section_base} {section_tone}")[description])

    return div(**root_attrs)[*children]
