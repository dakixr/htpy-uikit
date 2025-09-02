from htpy import Renderable
from htpy import div
from htpy import h2
from htpy import section

from htpy_uikit.utils import merge_classes

from .icons import icon_circle_alert
from .icons import icon_circle_check
from .icons import icon_info
from .types import AlertVariant


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
    """Basecoat-style alert with intent-based variants.

    Structure matches the reference:
      <div class="alert[ -destructive]">
        <svg/> (optional)
        <h2/>
        <section/> (optional)
      </div>
    """

    # Inline Basecoat alert classes so the component is self-contained.
    # Use a subtle border (border-border/30) and small shadow to match reference.
    root_base_classes = (
        "relative w-full rounded-lg border border-border px-4 py-3 text-sm grid "
        "grid-cols-[0_1fr] has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] "
        "has-[>svg]:gap-x-3 gap-y-0.5 items-start [&>svg]:size-4 [&>svg]:translate-y-0.5 "
        "[&>svg]:text-current bg-card shadow-sm"
    )

    # Tone classes control text color; destructive uses the destructive token.
    tone_classes = (
        "text-destructive" if variant == "destructive" else "text-card-foreground"
    )

    classes_inline = merge_classes(f"{root_base_classes} {tone_classes}", class_)

    root_attrs: dict[str, str] = {"class_": classes_inline, "role": "alert"}
    if target_id:
        root_attrs.update(
            {"id": target_id, "hx-swap-oob": "true", "hx-swap": "transition:true"}
        )

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
    children.append(
        h2(class_="col-start-2 line-clamp-1 min-h-4 font-medium tracking-tight")[title]
    )
    if description:
        section_base = (
            "col-start-2 grid justify-items-start gap-1 text-sm [&_p]:leading-relaxed"
        )
        section_tone = (
            "text-destructive" if variant == "destructive" else "text-muted-foreground"
        )
        children.append(section(class_=f"{section_base} {section_tone}")[description])

    return div(**root_attrs)[*children]
