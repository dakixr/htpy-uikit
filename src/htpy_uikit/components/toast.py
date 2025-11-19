import json

from htpy import Node
from htpy import Renderable
from htpy import a
from htpy import div
from htpy import footer
from htpy import h2
from htpy import p
from htpy import section
from htpy import span
from htpy import style
from htpy import template
from htpy import with_children
from markupsafe import Markup
from sourcetypes import js

from ._types import TAlign
from ._types import TCategory
from ._utils import merge_classes
from .button import button_component
from .icons import toast_icon_error
from .icons import toast_icon_info
from .icons import toast_icon_success


def toaster(
    *, align: TAlign = "end", id: str = "toaster", class_: str | None = None, **attrs
) -> Renderable:
    """Render a fixed toaster container managed via Alpine.

    Args:
        align: Horizontal alignment of the toaster stack.
        id: Element id for the toaster container.
        class_: Extra classes appended to the wrapper.
        **attrs: Additional HTML attributes forwarded to the wrapper ``div``.

    Returns:
        Renderable: Toaster container that listens for ``ui:toast`` events.

    Notes:
        Dispatch ``new CustomEvent('ui:toast', { detail: { config } })`` on
        ``window``/``document`` to enqueue toasts. ``config`` can specify
        ``category``, ``title``, ``description``, ``action``/``cancel`` objects,
        and ``duration`` (``-1`` keeps the toast open).
    """

    align_dict: dict[TAlign, str] = {
        "end": "right-0",
        "start": "left-0",
        "center": "left-1/2 -translate-x-1/2",
    }

    align_classes = align_dict[align]

    wrapper_classes = merge_classes(
        base_classes=(
            f"fixed bottom-0 p-4 pointer-events-none z-50 w-full max-w-sm sm:max-w-md md:max-w-lg "
            f"flex flex-col-reverse {align_classes} gap-2"
        ),
        class_=class_,
    )

    # Alpine state and methods with enhanced animations
    alpine_data: js = """
    {
        toasts: [],
        nextId: 1,
        isPaused: false,
        hoverCount: 0,
        addToast(cfg) {
            cfg = cfg || {};
            const id = this.nextId++;
            const d = (cfg.duration === -1) ? -1 : (cfg.duration ?? (cfg.category === 'error' ? 8000 : 5000));
            const toast = {
                id,
                open: true,
                duration: d,
                index: this.toasts.length,
                remainingTime: d,
                timeoutId: null,
                startTime: null,
                ...cfg
            };
            // Prepend so newest appears on top
            this.toasts.unshift(toast);
            if (d !== -1 && !this.isPaused) {
                toast.startTime = Date.now();
                toast.timeoutId = setTimeout(() => this.close(id), d);
            }
            this.updateIndices();
        },
        onToastEnter() {
            this.hoverCount++;
            if (!this.isPaused) {
                this.pauseAll();
            }
        },
        onToastLeave() {
            if (this.hoverCount > 0) this.hoverCount--;
            if (this.hoverCount === 0) {
                this.resumeAll();
            }
        },
        pauseAll() {
            if (this.isPaused) return;
            this.isPaused = true;
            this.toasts.forEach((t) => {
                if (!t.open || t.duration === -1) return;
                if (t.timeoutId) {
                    clearTimeout(t.timeoutId);
                    t.timeoutId = null;
                    if (t.startTime != null) {
                        t.remainingTime = t.remainingTime - (Date.now() - t.startTime);
                    }
                }
            });
        },
        resumeAll() {
            if (!this.isPaused) return;
            this.isPaused = false;
            this.toasts.forEach((t) => {
                if (!t.open || t.duration === -1 || t.timeoutId) return;
                if (t.remainingTime > 0) {
                    t.startTime = Date.now();
                    t.timeoutId = setTimeout(() => this.close(t.id), t.remainingTime);
                } else {
                    this.close(t.id);
                }
            });
        },
        close(id) {
            const i = this.toasts.findIndex(t => t.id === id);
            if (i > -1) {
                const t = this.toasts[i];
                if (t.timeoutId) clearTimeout(t.timeoutId);
                t.timeoutId = null;
                // guard against double-close jitter
                if (!t.open) return;
                t.open = false;
            }
        },
        updateIndices() {
            this.toasts.forEach((toast, i) => {
                toast.index = i;
            });
        },
        finalizeCloseOnTransition(id, evt) {
            // Only act on the wrapper element's own transition end
            if (evt && evt.target !== evt.currentTarget) return;
            const i = this.toasts.findIndex(t => t.id === id);
            if (i === -1) return;
            const t = this.toasts[i];
            // If it's still open or already removed, ignore
            if (t.open || t._removed) return;
            t._removed = true;
            this.toasts.splice(i, 1);
            this.updateIndices();
        },
        runAction(onclick, id) {
            if (!onclick) return;
            try {
                (new Function('close', onclick))(() => this.close(id));
            } catch (e) {
                console.error(e);
                this.close(id);
            }
        },
        runCancel(onclick, id) {
            if (onclick) {
                try {
                    (new Function('close', onclick))(() => this.close(id));
                } catch (e) {
                    console.error(e);
                    this.close(id);
                }
            } else {
                this.close(id);
            }
        }
    }
    """

    toast_classes = "toast pointer-events-auto w-full"

    content_classes = (
        "toast-content text-popover-foreground text-[13px] bg-popover/95 backdrop-blur-sm border border-border "
        "shadow-xl shadow-black/10 rounded-lg overflow-hidden flex gap-2.5 p-3 items-center "
        "ring-1 ring-ring/50 transition-all duration-200 ease-out"
    )

    btn_base = "h-6 px-2.5 text-xs"

    return div(
        id=id,
        class_=wrapper_classes,
        x_data=Markup(alpine_data),
        **{
            "@ui:toast.window": Markup("addToast($event.detail || {})"),
        },
        **attrs,
    )[
        style()[
            Markup(
                """
                /* Toast animation keyframes */
                @keyframes toast-in {
                    from {
                        opacity: 0;
                        transform: translateY(14px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                @keyframes toast-out {
                    from {
                        opacity: 1;
                        transform: translateY(0);
                    }
                    to {
                        opacity: 0;
                        transform: translateY(6px);
                    }
                }
                """
            )
        ],
        template(x_for="t in toasts", x_key="t.id")[
            div(
                class_=toast_classes,
                aria_atomic="true",
                **{":role": Markup("t.category === 'error' ? 'alert' : 'status'")},
                **{":aria-hidden": Markup("!t.open")},
                **{
                    "style": """
                        will-change: transform, opacity; display: grid; 
                        grid-template-rows: 1fr;
                        transition: grid-template-rows 260ms ease, opacity 260ms ease, margin 260ms ease; 
                        animation: toast-in 0.26s ease-out;
                    """,
                    "x-bind:style": Markup(
                        """
                        { 
                            gridTemplateRows: t.open ? '1fr' : '0fr',
                            opacity: t.open ? 1 : 0,
                            marginTop: t.open ? '0.5rem' : 0,
                            overflow: t.open ? '' : 'hidden' 
                        }
                        """
                    ),
                    "@mouseenter": "onToastEnter()",
                    "@mouseleave": "onToastLeave()",
                    "@transitionend": "finalizeCloseOnTransition(t.id, $event)",
                },
            )[
                div(
                    class_=content_classes,
                    x_show="true",
                )[
                    # Left accent bar for category color
                    div(
                        class_="w-1 self-stretch rounded-sm",
                        **{
                            ":class": Markup("""
                            {
                                'bg-green-400': t.category === 'success',
                                'bg-red-400': t.category === 'error',
                                'bg-blue-400': t.category === 'info',
                                'bg-yellow-400': t.category === 'warning'
                            }
                        """)
                        },
                    ),
                    span(
                        class_="inline-flex",
                        **{
                            ":class": Markup("""
                            {
                                'text-green-400': t.category === 'success',
                                'text-red-400': t.category === 'error',
                                'text-blue-400': t.category === 'info',
                                'text-yellow-400': t.category === 'warning'
                            }
                        """)
                        },
                    )[
                        div(x_show="t.category === 'success'", x_cloak="")[toast_icon_success()],
                        div(x_show="t.category === 'error'", x_cloak="")[toast_icon_error()],
                        div(x_show="t.category === 'info'", x_cloak="")[toast_icon_info()],
                        div(x_show="t.category === 'warning'", x_cloak="")[toast_icon_error()],
                    ],
                    section()[
                        h2()[span(x_text="t.title")],
                        p(
                            x_show="t.description",
                            x_text="t.description",
                            class_="text-muted-foreground break-all",
                            x_cloak="",
                        ),
                    ],
                    footer(class_="ml-auto flex flex-col gap-2")[
                        a(
                            class_=f"btn {btn_base}",
                            x_show="t.action && t.action.href",
                            x_bind_href="t.action && t.action.href",
                            **{"data-toast-action": ""},
                            **{"@click.prevent": "close(t.id)"},
                            x_cloak="",
                        )[span(x_text="t.action && t.action.label")],
                        # Action button (custom onclick)
                        button_component(
                            variant="primary",
                            class_=btn_base,
                            type="button",
                            **{  # pyright: ignore[reportArgumentType]
                                "x_show": "t.action && t.action.onclick",
                                "x_cloak": "",
                                "data-toast-action": "",
                                "@click": "runAction(t.action && t.action.onclick, t.id)",
                            },
                        )[span(x_text="t.action && t.action.label")],
                        # Always-present dismiss button (uses cancel handler if provided)
                        button_component(
                            variant="outline",
                            class_=f"rounded-sm {btn_base}",
                            type="button",
                            **{  # pyright: ignore[reportArgumentType]
                                "data-toast-cancel": "",
                                "@click": "runCancel(t.cancel && t.cancel.onclick, t.id)",
                            },
                        )[span(x_text="(t.cancel && t.cancel.label) || 'Dismiss'")],
                    ],
                ],
            ],
        ],
    ]


@with_children
def toast_trigger(
    children: Node,
    *,
    category: TCategory = "info",
    title: str,
    description: str | None = None,
    duration_ms: int | None = None,
    class_: str | None = None,
) -> Renderable:
    """Wrap arbitrary content and dispatch a ``ui:toast`` event on click.

    Args:
        children: Node rendered inside the trigger wrapper.
        category: Toast category token (success, error, info).
        title: Toast title.
        description: Optional supporting text.
        duration_ms: Optional custom duration in milliseconds (``-1`` keeps it open).
        class_: Extra classes appended to the trigger wrapper.

    Returns:
        Renderable: ``<span>`` wrapper with the necessary Alpine hook.
    """

    # Canonical shape: event.detail IS the toast config built by helper

    return span(
        **{
            "x-data": "",
            "@click": (
                code_trigger_toast(
                    category=category,
                    title=title,
                    description=description,
                    duration_ms=duration_ms,
                )
            ),
        },
        class_=class_,
    )[children]


def code_trigger_toast(
    *,
    category: TCategory,
    title: str,
    description: str | None = None,
    duration_ms: int | None = None,
) -> str:
    """Return JavaScript that dispatches the ``ui:toast`` event.

    Args:
        category: Toast category token.
        title: Toast title.
        description: Optional supporting text.
        duration_ms: Custom duration in milliseconds.

    Returns:
        str: Inline JavaScript that dispatches the event when executed.
    """

    const_json: str = build_toast_event(
        category=category,
        title=title,
        description=description,
        duration_ms=duration_ms,
    )

    code: js = f"""
        const payload = JSON.parse('{const_json}')['ui:toast'];
        window.dispatchEvent(new CustomEvent('ui:toast', {{ detail: payload }}));
    """

    return Markup(code)


def build_toast_event(
    *,
    category: TCategory,
    title: str,
    description: str | None = None,
    duration_ms: int | None = None,
) -> str:
    """Build the canonical ``ui:toast`` event payload.

    Args:
        category: Toast category token.
        title: Toast title.
        description: Optional supporting text.
        duration_ms: Custom duration in milliseconds.

    Returns:
        str: JSON string shaped like ``{\"ui:toast\": {...}}``.
    """
    config: dict[str, object] = {"category": category, "title": title}
    if description is not None:
        config["description"] = description
    if duration_ms is not None:
        config["duration"] = duration_ms
    return json.dumps({"ui:toast": config})
