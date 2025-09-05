from htpy import Renderable
from htpy import i as i_el
from htpy import script
from sourcetypes import js

from ._types_lucide import LucideName


def lucide_icon(
    variant: LucideName,
    /,
    *,
    class_: str | None = "size-4",
    **attrs,
) -> Renderable:
    """Render a Lucide icon placeholder using the CDN runtime.

    This renders an <i data-lucide="..."> element which Lucide's JS replaces with
    the corresponding inline <svg>. Include the CDN and call `lucide.createIcons()`
    on the page (see helpers below).

    Args:
        variant: Lucide icon name (e.g. "activity", "alert-circle").
        class_: CSS classes to apply (transferred onto the generated <svg>).
        **attrs: Additional attributes forwarded to the element (e.g., stroke_width="1.5").
    """
    attrs["data-lucide"] = variant

    if class_:
        attrs["class_"] = class_

    return i_el(**attrs)


def lucide_cdn_script(version: str = "latest") -> Renderable:
    """Return the <script> tag that loads the Lucide UMD bundle from a CDN.

    Place this once, near the end of <body> or in your layout/template head.
    """
    src = f"https://unpkg.com/lucide@{version}"
    return script(src=src)


def lucide_auto_init_script() -> Renderable:
    code: js = """
        lucide.createIcons();
    """
    return script()[code]
