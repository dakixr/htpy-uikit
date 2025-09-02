from typing import Literal
from typing import assert_never

from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import span
from htpy import with_children
from sourcetypes import js

from htpy_uikit.utils import merge_classes

from .button import button_component
from .icons import icon_check

TAlign = Literal["start", "center", "end"]
TSide = Literal["top", "bottom", "left", "right"]


@with_children
def dropdown_menu(
    children: Node,
    *,
    trigger: Node | str = "Open",
    side: TSide = "bottom",
    align: TAlign = "start",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style dropdown menu component with Alpine.js.

    Based on Basecoat UI dropdown-menu implementation.
    Uses Alpine.js for show/hide functionality and keyboard navigation.

    Args:
        children: Dropdown menu content
        trigger: Element that triggers the dropdown
        side: Dropdown side (top, bottom, left, right)
        align: Dropdown alignment (start, center, end)
        The popover has a sensible default minimum width of 16rem.
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Dropdown menu component
    """

    # Generate unique IDs for the dropdown
    import uuid

    # Respect provided id but avoid passing it twice to the element
    container_id = attrs.pop("id", f"dropdown-{str(uuid.uuid4())[:8]}")
    popover_id = f"{container_id}-popover"
    menu_id = f"{container_id}-menu"
    trigger_id = f"{container_id}-trigger"

    # Set data attributes for positioning
    data_attrs = {
        "data-side": side,
        "data-align": align,
    }

    # Add custom class if provided
    base_container_classes = "relative inline-flex"
    if class_:
        base_container_classes = f"{base_container_classes} {class_}"

    attrs["class_"] = base_container_classes

    # Add data attributes to existing attrs
    attrs.update(data_attrs)

    # Compute Tailwind position classes to avoid JS-driven jumps
    def get_align_classes(align: TAlign) -> str:
        if align == "start":
            return "left-0"
        elif align == "center":
            return "left-1/2 -translate-x-1/2"
        elif align == "end":
            return "right-0 left-auto"
        else:
            assert_never(align)

    def get_vertical_align_classes(align: TAlign) -> str:
        if align == "start":
            return "top-0"
        elif align == "center":
            return "top-1/2 -translate-y-1/2"
        elif align == "end":
            return "bottom-0 top-auto"
        else:
            assert_never(align)

    popover_pos_classes = ""
    if side == "bottom":
        popover_pos_classes = f"{get_align_classes(align)} top-full mt-2"
    elif side == "top":
        popover_pos_classes = f"{get_align_classes(align)} bottom-full mb-2"
    elif side == "right":
        popover_pos_classes = f"left-full ml-2 {get_vertical_align_classes(align)}"
    elif side == "left":
        popover_pos_classes = f"right-full mr-2 {get_vertical_align_classes(align)}"
    else:
        assert_never(side)

    # Alpine.js state + keyboard interactions (no JS positioning)
    alpine_state: js = f"""
    {{
        open: false,
        items: [],
        activeIndex: -1,

        init() {{
            this.$nextTick(() => {{
                this.items = Array.from(this.$refs.menu.querySelectorAll('[role^="menuitem"]'))
                    .filter(el => !el.hasAttribute('disabled') && el.getAttribute('aria-disabled') !== 'true');
            }});
        }},

        close(focus=true) {{
            if (this.open) {{
                this.open = false;
                if (focus) this.$refs.trigger.focus();
                this.activeIndex = -1;
                this.$refs.trigger.setAttribute('aria-expanded', 'false');
                this.$refs.popover.setAttribute('aria-hidden', 'true');
            }}
        }},

        openMenu(focus) {{
            document.dispatchEvent(new CustomEvent('basecoat:popover', {{
                detail: {{ source: this.$el }}
            }}));
            this.open = true;
            this.$refs.trigger.setAttribute('aria-expanded', 'true');
            this.$refs.popover.setAttribute('aria-hidden', 'false');
            if (this.items.length) {{
                if (focus === 'first') this.activeIndex = 0;
                else if (focus === 'last') this.activeIndex = this.items.length - 1;
                this.syncActiveClass();
            }}
        }},

        onKey(e) {{
            const expanded = this.open;
            if (e.key === 'Escape') {{
                if (expanded) {{
                    e.preventDefault();
                    this.close();
                }}
                return;
            }}
            if (!expanded) {{
                if (['Enter', ' '].includes(e.key)) {{
                    e.preventDefault();
                    this.openMenu(false);
                }} else if (e.key === 'ArrowDown') {{
                    e.preventDefault();
                    this.openMenu('first');
                }} else if (e.key === 'ArrowUp') {{
                    e.preventDefault();
                    this.openMenu('last');
                }}
                return;
            }}
            if (this.items.length === 0) return;
            let next = this.activeIndex;
            if (e.key === 'ArrowDown') {{
                e.preventDefault();
                next = this.activeIndex < 0 ? 0 : Math.min(this.activeIndex + 1, this.items.length - 1);
            }} else if (e.key === 'ArrowUp') {{
                e.preventDefault();
                next = this.activeIndex < 0 ? this.items.length - 1 : Math.max(this.activeIndex - 1, 0);
            }} else if (e.key === 'Home') {{
                e.preventDefault();
                next = 0;
            }} else if (e.key === 'End') {{
                e.preventDefault();
                next = this.items.length - 1;
            }} else if (e.key === 'Enter' || e.key === ' ') {{
                e.preventDefault();
                if (this.activeIndex > -1) this.items[this.activeIndex].click();
                this.close();
                return;
            }}
            if (next !== this.activeIndex) {{
                this.activeIndex = next;
                const el = this.items[this.activeIndex];
                if (el) {{
                    if (!el.id) el.id = '{menu_id}-item-' + this.activeIndex;
                    this.$refs.trigger.setAttribute('aria-activedescendant', el.id);
                }}
                this.syncActiveClass();
            }}
        }},

        hoverMove(ev) {{
            const t = ev.target.closest('[role^="menuitem"]');
            if (!t) return;
            const idx = this.items.indexOf(t);
            if (idx > -1 && idx !== this.activeIndex) {{
                this.activeIndex = idx;
                this.syncActiveClass();
            }}
        }},

        resetActive() {{
            this.activeIndex = -1;
            this.$refs.trigger.removeAttribute('aria-activedescendant');
            this.syncActiveClass();
        }},

        onClick(ev) {{
            const item = ev.target.closest('[role^="menuitem"]');
            if (!item) return;
            const role = item.getAttribute('role');
            if (role === 'menuitem') {{
                this.close();
                return;
            }}
            if (role === 'menuitemcheckbox') {{
                const isChecked = item.getAttribute('aria-checked') === 'true';
                item.setAttribute('aria-checked', (!isChecked).toString());
                return;
            }}
            if (role === 'menuitemradio') {{
                const group = item.getAttribute('data-group') || '';
                const scope = group
                    ? this.$refs.menu.querySelectorAll('[role="menuitemradio"][data-group="' + group + '"]')
                    : this.$refs.menu.querySelectorAll('[role="menuitemradio"]');
                scope.forEach(el => el.setAttribute('aria-checked', el === item ? 'true' : 'false'));
                return;
            }}
        }},

        syncActiveClass() {{
            this.items.forEach((it, i) => it.classList.toggle('active', i === this.activeIndex));
        }}
    }}
    """

    alpine_attrs = {"x-data": alpine_state, **attrs}

    if isinstance(trigger, str):
        trigger_node = button_component(variant="outline")[trigger]
        trigger_el = span(
            **{
                "id": trigger_id,
                "x-ref": "trigger",
                "@click": "open ? close() : openMenu(false)",
                "@keydown": "onKey($event)",
                "aria_haspopup": "menu",
                "aria_controls": menu_id,
                "aria_expanded": "false",
            }
        )[trigger_node]
    else:
        trigger_el = span(
            **{
                "id": trigger_id,
                "x-ref": "trigger",
                "@click": "open ? close() : openMenu(false)",
                "@keydown": "onKey($event)",
                "aria_haspopup": "menu",
                "aria_controls": menu_id,
                "aria_expanded": "false",
            }
        )[trigger]

    return div(id=container_id, **alpine_attrs)[
        trigger_el,
        div(
            id=popover_id,
            class_=f"absolute z-50 will-change-transform {popover_pos_classes}",
            **{
                "x-ref": "popover",
                "x-show": "open",
                # translate-y avoids scale jitter
                "x-transition:enter": "transition ease-out duration-150",
                "x-transition:enter-start": "opacity-0 translate-y-1",
                "x-transition:enter-end": "opacity-100 translate-y-0",
                "x-transition:leave": "transition ease-in duration-120",
                "x-transition:leave-start": "opacity-100 translate-y-0",
                "x-transition:leave-end": "opacity-0 translate-y-1",
                "@click.outside": "close(false)",
                "@keydown.escape": "close()",
                "data-popover": "",
                "aria_hidden": "true",
            },
        )[
            div(
                id=menu_id,
                role="menu",
                aria_labelledby=trigger_id,
                class_=(
                    "rounded-md border border-border bg-popover text-popover-foreground "
                    "shadow-md p-2 min-w-[16rem]"
                ),
                **{
                    "x-ref": "menu",
                    "@mousemove": "hoverMove($event)",
                    "@mouseleave": "resetActive()",
                    "@click": "onClick($event)",
                },
            )[children]
        ],
    ]


# Dropdown menu items - following basecoat implementation
def dropdown_menu_item(
    children: Node,
    *,
    disabled: bool = False,
    shortcut: str | None = None,
    inset: bool = False,
    left_icon: Node | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Dropdown menu item component.

    Args:
        children: Menu item content
        disabled: Whether the item is disabled
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Menu item element
    """

    # Base classes - using Tailwind equivalent of Basecoat menu item
    base_classes = (
        "aria-hidden:hidden [&_svg]:text-muted-foreground relative flex cursor-default items-center gap-2 "
        "rounded-sm px-2 py-1.5 text-sm outline-hidden select-none [&_svg]:shrink-0 [&_svg]:size-4 w-full truncate"
    )

    if disabled:
        base_classes += " opacity-50 pointer-events-none"
        attrs["aria-disabled"] = "true"
    else:
        base_classes += (
            " focus-visible:bg-accent focus-visible:text-accent-foreground hover:bg-accent "
            "hover:text-accent-foreground"
        )

    # Add optional inset
    if inset:
        base_classes += " pl-8"

    # Add custom classes
    if class_:
        base_classes += f" {class_}"

    # Add class to attrs
    attrs["class_"] = base_classes

    content_children: list[Node] = []
    if left_icon:
        content_children.append(left_icon)
    content_children.append(children)
    if shortcut:
        content_children.append(
            span(class_="text-muted-foreground ml-auto text-xs tracking-widest")[
                shortcut
            ]
        )

    return div(
        **{
            "role": "menuitem",
            "tabindex": "-1",
            **attrs,
        },
    )[content_children]


def dropdown_menu_separator(
    *,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Dropdown menu separator component.

    Args:
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Menu separator element
    """

    # Base classes - using Tailwind equivalent of Basecoat separator
    base_classes = "-mx-1 my-1 border-b border-border"

    # Add custom classes
    attrs["class_"] = merge_classes(base_classes, class_)

    return div(**{"role": "separator", **attrs})


@with_children
def dropdown_menu_label(
    children: Node,
    *,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Dropdown menu label component.

    Args:
        children: Label content
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.div: Menu label element
    """

    # Base classes - using Tailwind equivalent of Basecoat label
    base_classes = "flex px-2 py-1.5 text-sm font-medium"

    # Add custom classes
    attrs["class_"] = merge_classes(base_classes, class_)

    return span(**{"role": "heading", **attrs})[children]


def _check_icon() -> Renderable:
    """Small check icon toggled via group-aria-checked utility classes."""
    return icon_check(class_="invisible group-aria-checked:visible")


def dropdown_menu_item_checkbox(
    label: Node | str,
    *,
    checked: bool = False,
    disabled: bool = False,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    base_classes = (
        "group aria-hidden:hidden [&_svg]:text-muted-foreground relative flex cursor-default items-center gap-2 "
        "rounded-sm px-2 py-1.5 text-sm outline-hidden select-none [&_svg]:shrink-0 [&_svg]:size-4 w-full truncate"
    )
    if disabled:
        base_classes += " opacity-50 pointer-events-none"
        attrs["aria-disabled"] = "true"
    else:
        base_classes += (
            " focus-visible:bg-accent focus-visible:text-accent-foreground hover:bg-accent "
            "hover:text-accent-foreground"
        )
    if class_:
        base_classes += f" {class_}"
    attrs["class_"] = base_classes

    return div(
        **{
            "role": "menuitemcheckbox",
            "aria-checked": "true" if checked else "false",
            "tabindex": "-1",
            **attrs,
        },
    )[_check_icon(), label]


def dropdown_menu_item_radio(
    label: Node | str,
    *,
    group: str,
    checked: bool = False,
    disabled: bool = False,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    base_classes = (
        "group aria-hidden:hidden relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 "
        "text-sm outline-hidden select-none w-full truncate"
    )
    if disabled:
        base_classes += " opacity-50 pointer-events-none"
        attrs["aria-disabled"] = "true"
    else:
        base_classes += (
            " focus-visible:bg-accent focus-visible:text-accent-foreground hover:bg-accent "
            "hover:text-accent-foreground"
        )
    if class_:
        base_classes += f" {class_}"
    attrs["class_"] = base_classes

    indicator = div(class_="size-4 flex items-center justify-center")[
        div(
            class_=(
                "size-2 rounded-full bg-foreground invisible group-aria-checked:visible"
            ),
            aria_hidden="true",
            focusable="false",
        )
    ]

    return div(
        **{
            "role": "menuitemradio",
            "aria-checked": "true" if checked else "false",
            "data-group": group,
            "tabindex": "-1",
            **attrs,
        },
    )[indicator, label]


def dropdown_menu_group(
    children: Node,
    *,
    label: str | Node | None = None,
    label_id: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Logical grouping for dropdown menu options. If label is provided a heading
    with an id will be rendered and linked via aria-labelledby.
    """
    import uuid

    base_classes = ""
    if class_:
        base_classes = class_
    if base_classes:
        attrs["class_"] = (
            base_classes
            if "class_" not in attrs
            else f"{base_classes} {attrs['class_']}"
        )
    heading = None
    if label is not None:
        lid = label_id or f"dm-group-{str(uuid.uuid4())[:6]}"
        attrs["aria_labelledby"] = lid
        heading = dropdown_menu_label(class_="", id=lid)[label]
    return div(**{"role": "group", **attrs})[
        [heading, children] if heading else [children]
    ]


def dropdown_menu_trigger(
    text: str = "Menu",
    *,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Dropdown menu trigger button component.

    Args:
        text: Button text
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.button: Trigger button element
    """

    # Base classes - using Tailwind equivalent of Basecoat button
    base_classes = (
        "inline-flex items-center justify-center whitespace-nowrap "
        "rounded-md text-sm font-medium transition-all disabled:pointer-events-none "
        "disabled:opacity-50 gap-2 h-9 px-4 py-2 has-[>svg]:px-3"
    )

    # Add custom classes
    if class_:
        base_classes += f" {class_}"

    attrs["class_"] = base_classes

    return button(
        type="button",
        **attrs,
    )[text]
