from htpy import Node
from htpy import Renderable
from htpy import span
from htpy import template
from htpy import with_children
from markupsafe import Markup
from sourcetypes import js

from ._types import TAlign
from ._types import TSide
from ._utils import merge_classes


@with_children
def tooltip(
    children: Node,
    *,
    content: Node,
    side: TSide = "top",
    align: TAlign = "center",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render an Alpine-powered tooltip with viewport-aware positioning.

    The component renders a wrapper around `children` and a tooltip bubble
    that is fixed-positioned to the viewport to avoid clipping within
    overflow-hidden containers. Visibility and positioning are controlled with
    Alpine (`x-data`, `x-show`, `x-ref`). No external CSS is required.

    Args:
        content: Tooltip content (string or Node)
        children: Trigger element
        side: One of "top", "bottom", "left", "right" (default: "top")
        align: One of "start", "center", "end" (default: "center")
        class_: Extra classes for the trigger wrapper
        **attrs: Extra attributes forwarded to the tooltip bubble

    Returns:
        Renderable: Trigger span plus teleported tooltip template.
    """

    # Use viewport-based positioning calculated with Alpine to avoid overflow clipping

    # Base classes for bubble
    bubble_classes_base = (
        "fixed z-50 bg-primary text-primary-foreground rounded-md px-3 py-1.5 "
        "text-xs whitespace-nowrap pointer-events-none transform transition-all"
    )

    x_data: js = f"""
        {{
            open: false,
            style: '',
            side: '{side}',
            align: '{align}',
            _raf: null,
            schedule() {{
                cancelAnimationFrame(this._raf || 0);
                this._raf = requestAnimationFrame(() => {{
                    this.update();
                    // Run a second time next frame to account for late layout/teleport
                    this._raf = requestAnimationFrame(() => this.update());
                }});
            }},
            cancel() {{
                cancelAnimationFrame(this._raf || 0);
                this._raf = null;
            }},
            update() {{
                const trigger = this.$refs.trigger;
                const bubble = this.$refs.bubble;
                if (!trigger || !bubble) return;
                const r = trigger.getBoundingClientRect();
                const spacing = 6;
                let top = 0, left = 0;
                const bw = bubble.offsetWidth, bh = bubble.offsetHeight;

                if (this.side === 'top') {{
                    top = r.top - bh - spacing;
                    if (this.align === 'start') left = r.left;
                    else if (this.align === 'end') left = r.right - bw;
                    else left = r.left + (r.width - bw) / 2;
                }} else if (this.side === 'bottom') {{
                    top = r.bottom + spacing;
                    if (this.align === 'start') left = r.left;
                    else if (this.align === 'end') left = r.right - bw;
                    else left = r.left + (r.width - bw) / 2;
                }} else if (this.side === 'left') {{
                    left = r.left - bw - spacing;
                    if (this.align === 'start') top = r.top;
                    else if (this.align === 'end') top = r.bottom - bh;
                    else top = r.top + (r.height - bh) / 2;
                }} else if (this.side === 'right') {{
                    left = r.right + spacing;
                    if (this.align === 'start') top = r.top;
                    else if (this.align === 'end') top = r.bottom - bh;
                    else top = r.top + (r.height - bh) / 2;
                }}

                // Clamp to viewport with padding
                const pad = 8;
                const vw = window.innerWidth, vh = window.innerHeight;
                left = Math.max(pad, Math.min(left, vw - bw - pad));
                top = Math.max(pad, Math.min(top, vh - bh - pad));
                this.style = `top:${{top}}px;left:${{left}}px`;
            }}
        }}
    """

    # Wrapper attributes: Alpine handles open state on hover/focus
    wrapper_attrs = {
        "class_": merge_classes("relative inline-block w-fit", class_),
        "x-ref": "trigger",
        "x-data": Markup(x_data),
        "@mouseenter": "open = true; $nextTick(() => schedule())",
        "@mouseleave": "open = false; cancel()",
        "@focus": "open = true; $nextTick(() => schedule())",
        "@blur": "open = false; cancel()",
        "@resize.window": "open && schedule()",
        "@scroll.window": "open && schedule()",
        "tabindex": "0",
        "aria-describedby": "",
    }

    # Build tooltip bubble with Alpine show/transition attributes
    bubble_attrs = {
        "class_": f"{bubble_classes_base}",
        "x-ref": "bubble",
        ":style": "style",
        "x-show": "open",
        "x-cloak": "",
        "x-transition:enter": "transition ease-out duration-200",
        "x-transition:enter-start": "opacity-0 scale-95",
        "x-transition:enter-end": "opacity-100 scale-100",
        "x-transition:leave": "transition ease-in duration-150",
        "x-transition:leave-start": "opacity-100 scale-100",
        "x-transition:leave-end": "opacity-0 scale-95",
        "role": "tooltip",
    }

    # Create elements
    bubble = span(**bubble_attrs, **attrs)[content]
    teleported = template(x_teleport="body")[bubble]

    return span(**wrapper_attrs)[children, teleported]
