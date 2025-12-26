from htpy import Renderable
from htpy import div
from htpy import header
from htpy import input as input_
from htpy import span
from sourcetypes import js

from ._styles import LISTBOX_OPTION_BASE_CLASSES
from ._styles import POPOVER_PANEL_PADDED_CLASSES
from ._types import SelectOption
from .button import button_component
from .icons import icon_check
from .icons import icon_chevrons_up_down
from .icons import icon_search


def combobox(
    *,
    name: str | None = None,
    options: list[SelectOption] | None = None,
    value: str | None = None,
    placeholder: str = "Select option...",
    side: str = "bottom",
    align: str = "start",
    width_class: str = "w-auto",
    popover_width_class: str | None = None,
    empty_text: str = "No results found.",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a search-enabled popover combobox.

    Args:
        name: Hidden input name used for the selected value.
        options: Sequence of selectable option dictionaries.
        value: Initially selected value.
        placeholder: Trigger placeholder text.
        side: Popover placement relative to the trigger.
        align: Popover alignment relative to the trigger.
        width_class: Tailwind width classes applied to the trigger.
        popover_width_class: Optional width override for the popover.
        empty_text: Message rendered when client-side filtering leaves no options.
        class_: Extra CSS classes appended to the container.
        **attrs: Additional HTML attributes forwarded to the container.

    Returns:
        Renderable: Combobox trigger, popover, and hidden input nodes.
    """

    import uuid

    options = options or []

    base_id = attrs.pop("id", f"select-{str(uuid.uuid4())[:6]}")
    trigger_id = f"{base_id}-trigger"
    popover_id = f"{base_id}-popover"
    listbox_id = f"{base_id}-listbox"

    # Determine initial selection
    initial_label = placeholder
    initial_value = value or ""
    if value is not None:
        for option in options:
            if option["value"] == value:
                initial_label = option["label"]
                break

    # JS-safe initial value for inlining into x-data factory call
    initial_value_js = initial_value.replace("'", "\\'") if isinstance(initial_value, str) else ""

    # Container classes - match reference CSS exactly
    container_classes = "select relative inline-flex"
    if class_:
        container_classes = f"{container_classes} {class_}"

    # Alpine state defined inline for better compatibility and no timing issues

    trigger_btn = button_component(
        type="button",
        variant="outline",
        id=trigger_id,
        size="md",
        loading=False,
        disabled=False,
        icon_only=False,
        class_=f"{width_class} justify-between!",
        **{
            "x-ref": "trigger",
            "aria_haspopup": "listbox",
            "aria_controls": listbox_id,
            ":aria-expanded": "state.open",
            "@click": "state.open ? closeMenu() : openMenu()",
            "@keydown": "onKey($event)",
        },
    )[
        span(id=f"{base_id}-label", class_="truncate", **{"x-ref": "selected"})[initial_label],
        icon_chevrons_up_down(class_="opacity-50 shrink-0"),
    ]

    # Popover content
    popover_classes = "p-1"
    if popover_width_class:
        popover_classes = f"{popover_classes} {popover_width_class}"

    # Options as div[role=option] - use CSS for hover/selection states
    option_nodes: list[Renderable] = [
        div(
            role="option",
            **{
                "data-value": option["value"],
                "data-label": option["label"],
                "aria-selected": "true" if (option["value"] == initial_value) else "false",
                "@click": "updateLabelFromValue($el.dataset.value); closeMenu();",
            },
            class_=f"{LISTBOX_OPTION_BASE_CLASSES} aria-selected:bg-accent aria-selected:text-accent-foreground",
        )[
            span(class_="flex-1 truncate")[option["label"]],
            # trailing check positioned right (hidden/shown by component JS)
            span(class_="select-check absolute right-2.5 top-1/2 -translate-y-1/2")[
                icon_check(class_="size-4 opacity-50", **{"style": "display: none;"})
            ],
        ]
        for option in options
    ]

    popover = div(
        id=popover_id,
        **{
            "data-popover": "",
            "aria_hidden": "true",
            "x-ref": "popover",
            # Alpine-controlled visibility and transitions
            "x-show": "state.open",
            "x-cloak": "",
            "x-transition:enter": "transition ease-out duration-200",
            "x-transition:enter-start": "opacity-0 scale-95",
            "x-transition:enter-end": "opacity-100 scale-100",
            "x-transition:leave": "transition ease-in duration-150",
            "x-transition:leave-start": "opacity-100 scale-100",
            "x-transition:leave-end": "opacity-0 scale-95",
            # Placement attributes consumed by CSS
            "data_side": side,
            "data_align": align,
        },
        class_=f"{POPOVER_PANEL_PADDED_CLASSES} fixed min-w-48 w-max z-[9999]",
    )[
        # Header with search icon and input - match reference exactly
        header(class_="flex h-9 items-center gap-2 border-b px-3 mb-1 border-border")[
            icon_search(class_="opacity-50 size-4"),
            input_(
                type="text",
                placeholder="Search entries...",
                autocomplete="off",
                autocorrect="off",
                spellcheck="false",
                aria_autocomplete="list",
                role="combobox",
                aria_expanded="false",
                aria_controls=listbox_id,
                aria_labelledby=trigger_id,
                **{
                    "x-ref": "filter",
                    "x-model": "state.search",
                    "@input": "filter()",
                    "@keydown": "onKey($event)",
                },
                class_=(
                    "placeholder:text-muted-foreground flex h-9 flex-1 w-full rounded-md "
                    "bg-transparent py-2 text-sm outline-hidden min-w-0"
                ),
            ),
        ],
        # Listbox with proper attributes - match reference exactly
        div(
            id=listbox_id,
            role="listbox",
            aria_orientation="vertical",
            aria_labelledby=trigger_id,
            class_="max-h-60 overflow-auto p-1",
            **{
                "x-ref": "listbox",
                "data-empty": empty_text,
                "@mousemove": (
                    "$event.target.closest('[role=\"option\"]') && "
                    "setActiveFromElement($event.target.closest('[role=\"option\"]'))"
                ),
                "@mouseleave": "setActive(-1)",
                "@click": (
                    "$event.target.closest('[role=\"option\"]') && "
                    "updateLabelFromValue($event.target.closest('[role=\"option\"]').dataset.value); "
                    "$event.target.closest('[role=\"option\"]') && closeMenu()"
                ),
            },
        )[*option_nodes],
    ]

    # Hidden input - match reference naming pattern
    hidden = input_(
        type="hidden",
        name=name or f"{base_id}-value",
        value=initial_value,
        **{"x-ref": "input"},
    )

    # Root attributes with inline Alpine state
    alpine_data: js = f"""{{
        state: {{
            open: false,
            activeIndex: -1,
            search: '',
            selected: '{initial_value_js}',
            options: [],
            visible: []
        }},
        _scrollHandler: null,
        _resizeHandler: null,
        _clickOutsideHandler: null,
        init() {{
            this.$nextTick(() => {{
                this.state.options = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                this.resetVisible();
                this.updateLabelFromValue(this.state.selected, false);
                this.$refs.popover.setAttribute('aria-hidden', 'true');
            }});
            // Click outside handler
            this._clickOutsideHandler = (e) => {{
                if (this.state.open && !this.$el.contains(e.target) && !this.$refs.popover.contains(e.target)) {{
                    this.closeMenu(false);
                }}
            }};
            // Watch for search changes and filter automatically
            this.$watch('state.search', () => {{
                this.filter();
            }});
        }},
        destroy() {{
            this._removePositionListeners();
            if (this._clickOutsideHandler) {{
                document.removeEventListener('click', this._clickOutsideHandler, true);
            }}
        }},
        _positionPopover() {{
            const trigger = this.$refs.trigger;
            const popover = this.$refs.popover;
            if (!trigger || !popover) return;
            const rect = trigger.getBoundingClientRect();
            const popoverRect = popover.getBoundingClientRect();
            const viewportHeight = window.innerHeight;
            const viewportWidth = window.innerWidth;
            const spaceBelow = viewportHeight - rect.bottom;
            const spaceAbove = rect.top;
            const popoverHeight = popover.offsetHeight || 200;
            let top;
            if (spaceBelow >= popoverHeight || spaceBelow >= spaceAbove) {{
                top = rect.bottom + 4;
            }} else {{
                top = rect.top - popoverHeight - 4;
            }}
            let left = rect.left;
            if (left + popoverRect.width > viewportWidth) {{
                left = Math.max(4, viewportWidth - popoverRect.width - 4);
            }}
            popover.style.top = top + 'px';
            popover.style.left = left + 'px';
            popover.style.minWidth = rect.width + 'px';
        }},
        _addPositionListeners() {{
            this._scrollHandler = () => this._positionPopover();
            this._resizeHandler = () => this._positionPopover();
            window.addEventListener('scroll', this._scrollHandler, true);
            window.addEventListener('resize', this._resizeHandler);
        }},
        _removePositionListeners() {{
            if (this._scrollHandler) {{
                window.removeEventListener('scroll', this._scrollHandler, true);
                this._scrollHandler = null;
            }}
            if (this._resizeHandler) {{
                window.removeEventListener('resize', this._resizeHandler);
                this._resizeHandler = null;
            }}
        }},
        resetVisible() {{
            this.state.visible = [];
            this.state.options.forEach((o) => {{
                o.setAttribute('aria-hidden', 'false');
                // Ensure option is visible when resetting
                try {{
                    o.style.display = '';
                }} catch (e) {{}}
                this.state.visible.push(o);
            }});
        }},
        filter() {{
            const t = this.state.search.trim().toLowerCase();
            this.state.activeIndex = -1;
            this.state.visible = [];
            this.state.options.forEach((o) => {{
                const text = (o.dataset.label || o.textContent).trim().toLowerCase();
                const match = text.includes(t);
                o.setAttribute('aria-hidden', String(!match));
                // Hide/show the element directly so component is self-contained
                try {{
                    o.style.display = match ? '' : 'none';
                }} catch (e) {{}}
                if (match) this.state.visible.push(o);
                // ensure check icon hidden by default (we'll show for selected)
                try {{
                    const chk = o.querySelector('svg');
                    if (chk) chk.style.display = 'none';
                }} catch (e) {{}}
            }});
            // Manage empty placeholder inside the listbox (self-contained)
            try {{
                const lb = this.$refs.listbox;
                const existing = lb.querySelector('.combobox-empty');
                if (this.state.visible.length === 0) {{
                    if (!existing) {{
                        const el = document.createElement('div');
                        el.className = 'combobox-empty px-3 py-4 text-sm text-muted-foreground';
                        el.setAttribute('aria-hidden', 'true');
                        el.textContent = lb.dataset.empty || 'No results found.';
                        lb.prepend(el);
                    }}
                }} else {{
                    if (existing) existing.remove();
                }}
            }} catch (e) {{ /* noop if DOM not available */ }}
        }},
        setActive(i) {{
            if (this.state.activeIndex > -1 && this.state.options[this.state.activeIndex]) {{
                this.state.options[this.state.activeIndex].classList.remove('active');
            }}
            this.state.activeIndex = i;
            if (i > -1 && this.state.options[i]) {{
                const el = this.state.options[i];
                el.classList.add('active');
                if (!el.id) el.id = this.$id('opt');
                this.$refs.trigger.setAttribute('aria-activedescendant', el.id);
            }} else {{
                this.$refs.trigger.removeAttribute('aria-activedescendant');
            }}
        }},
        setActiveFromElement(el) {{
            if (!el) {{
                this.setActive(-1);
                return;
            }}
            const index = this.state.options.indexOf(el);
            if (index > -1) {{
                this.setActive(index);
            }}
        }},
        openMenu() {{
            this.state.open = true;
            document.dispatchEvent(new CustomEvent('combobox:popover', {{ detail: {{ source: this.$el }} }}));
            this.$refs.popover.setAttribute('aria-hidden', 'false');
            this.$refs.trigger.setAttribute('aria-expanded', 'true');
            this.$nextTick(() => {{
                this._positionPopover();
                this._addPositionListeners();
                document.addEventListener('click', this._clickOutsideHandler, true);
                if (this.$refs.filter) this.$refs.filter.focus();
                const sel = this.$refs.listbox.querySelector('[role="option"][aria-selected="true"]');
                if (sel) {{
                    this.setActive(this.state.options.indexOf(sel));
                    sel.scrollIntoView({{ block: 'nearest' }});
                }}
            }});
        }},
        closeMenu(focus = true) {{
            if (!this.state.open) return;
            this.state.open = false;
            this._removePositionListeners();
            document.removeEventListener('click', this._clickOutsideHandler, true);
            this.$refs.popover.setAttribute('aria-hidden', 'true');
            this.$refs.trigger.setAttribute('aria-expanded', 'false');
            if (this.$refs.filter) {{
                this.state.search = '';
                this.resetVisible();
            }}
            this.setActive(-1);
            if (focus) this.$refs.trigger.focus();
        }},
        updateLabelFromValue(val, triggerEvent = true) {{
            const opt = this.state.options.find((o) => o.dataset.value === val) || this.state.options[0];
            if (!opt) return;
            this.$refs.selected.innerHTML = opt.dataset.label || opt.innerHTML;
            this.state.selected = opt.dataset.value || '';
            this.$refs.input.value = this.state.selected;
            // Update aria-selected attributes - CSS handles the styling via aria-selected:bg-accent
            const prev = this.$refs.listbox.querySelector('[role="option"][aria-selected="true"]');
            if (prev) prev.setAttribute('aria-selected', 'false');
            opt.setAttribute('aria-selected', 'true');
            // Update checkmark visibility
            try {{
                this.state.options.forEach((o) => {{
                    const chk = o.querySelector('svg');
                    if (chk) chk.style.display = 'none';
                }});
                const chk = opt.querySelector('svg');
                if (chk) chk.style.display = '';
            }} catch (e) {{}}
            if (triggerEvent) this.$el.dispatchEvent(new CustomEvent('change', {{ detail: {{ value: this.state.selected }}, bubbles: true }}));
        }},
        selectCurrent() {{
            if (this.state.activeIndex > -1) {{
                this.updateLabelFromValue(this.state.options[this.state.activeIndex].dataset.value);
                this.closeMenu();
                return;
            }}
            // If no active index, select the first visible option
            if (this.state.visible.length > 0) {{
                const first = this.state.visible[0];
                this.updateLabelFromValue(first.dataset.value);
                this.closeMenu();
            }}
        }},
        onKey(e) {{
            const open = this.$refs.trigger.getAttribute('aria-expanded') === 'true';
            if (!['ArrowDown', 'ArrowUp', 'Home', 'End', 'Enter', 'Escape'].includes(e.key)) return;
            if (!open) {{
                if (e.key !== 'Enter' && e.key !== 'Escape') {{
                    e.preventDefault();
                    this.openMenu();
                }}
                return;
            }}
            e.preventDefault();
            if (e.key === 'Escape') {{
                this.closeMenu();
                return;
            }}
            if (this.state.visible.length === 0) return;
            let currentVisibleIndex = this.state.activeIndex > -1 ? this.state.visible.indexOf(this.state.options[this.state.activeIndex]) : -1;
            let next = currentVisibleIndex;
            if (e.key === 'ArrowDown') {{
                if (currentVisibleIndex < this.state.visible.length - 1) next = currentVisibleIndex + 1;
                else next = this.state.visible.length - 1;
            }} else if (e.key === 'ArrowUp') {{
                if (currentVisibleIndex > 0) next = currentVisibleIndex - 1;
                else next = 0;
            }} else if (e.key === 'Home') {{
                next = 0;
            }} else if (e.key === 'End') {{
                next = this.state.visible.length - 1;
            }} else if (e.key === 'Enter') {{
                this.selectCurrent();
                return;
            }}
            if (next !== currentVisibleIndex) {{
                const el = this.state.visible[next];
                this.setActive(this.state.options.indexOf(el));
                el.scrollIntoView({{ block: 'nearest' }});
            }}
        }}
    }}"""

    root_attrs: dict[str, str] = {
        "x-data": alpine_data,
        "data-side": side,
        "data-align": align,
        "@combobox:popover.window": "if($event.detail.source!==$el) closeMenu(false)",
    }
    # Merge caller attrs last so they can override if necessary
    root_attrs.update(attrs)

    # Root - no need for external JS file anymore
    root = div(id=base_id, class_=container_classes, **root_attrs)[hidden, trigger_btn, popover]

    return root
