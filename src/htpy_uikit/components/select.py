from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import label
from htpy import option
from htpy import select
from htpy import span
from sourcetypes import js

from ._types import SelectGroup
from ._types import SelectItem
from ._types import SelectOption
from .button import button_component
from .icons import icon_check
from .icons import icon_chevron_down


def native_select(
    *,
    id: str | None = None,
    name: str | None = None,
    options: list[SelectOption] | None = None,
    value: str | None = None,
    placeholder: str | None = None,
    label_text: str | None = None,
    error: str | None = None,
    disabled: bool = False,
    required: bool = False,
    multiple: bool = False,
    size: int | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Native HTML <select> styled like Basecoat. Useful for forms where
    the browser menu is acceptable. The popover-based Select is exposed
    separately as select_component.

    Based on Basecoat UI select component implementation.

    Args:
        id: Select element ID
        name: Select name attribute
        options: List of SelectOption dictionaries with value and label
        value: Selected value
        placeholder: Placeholder option text
        label_text: Label text
        error: Error message to display
        disabled: Disable select
        required: Mark as required
        multiple: Allow multiple selections
        size: Number of visible options
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy element: Select with optional label and error
    """

    # Base classes - Tailwind utility equivalents for Basecoat `.select` class
    # Mirrors rules from `staticfiles/css/basecoat.0.3.2.css` for native selects
    base_classes = (
        "appearance-none border-input focus-visible:border-ring focus-visible:ring-ring/50 "
        "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive "
        "dark:bg-input/30 dark:hover:bg-input/50 flex w-fit items-center justify-between gap-2 rounded-md border bg-transparent "
        "pl-3 pr-9 py-2 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] "
        "disabled:cursor-not-allowed disabled:opacity-50 h-9 bg-[image:var(--chevron-down-icon-50)] bg-no-repeat bg-position-[center_right_0.75rem] bg-size-[1rem]"
    )

    # Build class list
    classes = [base_classes]

    # Add custom classes
    if class_:
        classes.append(class_)

    # Handle error state with aria-invalid
    if error:
        attrs["aria-invalid"] = "true"

    # Prepare select attributes
    select_attrs = {
        "class_": " ".join(classes),
    }

    if id:
        select_attrs["id"] = id
    if name:
        select_attrs["name"] = name
    if disabled:
        select_attrs["disabled"] = "true"
    if required:
        select_attrs["required"] = "true"
    if multiple:
        select_attrs["multiple"] = "true"
    if size:
        select_attrs["size"] = str(size)

    # Add any additional attributes
    select_attrs.update(attrs)

    # Build options
    option_elements = []

    # Add placeholder option if provided
    if placeholder and not multiple:
        option_elements.append(
            option(value="", disabled="true", selected="" if value is None else None)[
                placeholder
            ]
        )

    # Add actual options
    if options:
        for opt in options:
            option_attrs = {"value": opt["value"]}
            if value == opt["value"]:
                option_attrs["selected"] = "true"
            option_elements.append(option(**option_attrs)[opt["label"]])

    # Build the component
    elements = []

    # Add label if provided
    if label_text:
        # Tailwind utilities for Basecoat `.label`:
        # flex items-center gap-2 text-sm leading-none font-medium select-none
        # peer-disabled:pointer-events-none peer-disabled:opacity-50
        label_attrs = {
            "class_": "flex items-center gap-2 text-sm leading-none font-medium select-none peer-disabled:pointer-events-none peer-disabled:opacity-50"
        }
        if id:
            label_attrs["for"] = id
        elements.append(label(**label_attrs)[label_text])

    # Add select
    elements.append(select(**select_attrs)[*option_elements])

    # Add error message if provided
    if error:
        elements.append(span(class_="text-sm text-red-600", **{"role": "alert"})[error])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        from htpy import div

        return div(class_="space-y-1")[*elements]


def _coerce_id(id_hint: str | None) -> str:
    import uuid

    return id_hint or f"select-{str(uuid.uuid4())[:6]}"


def select_component(
    *,
    id: str | None = None,
    name: str | None = None,
    options: list[SelectItem | SelectGroup] | None = None,
    value: str | None = None,
    placeholder: str = "Select option...",
    disabled: bool = False,
    side: str = "bottom",
    align: str = "start",
    width_class: str = "w-[180px]",
    scrollable: bool = False,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style Select with popover listbox. Tailwind + Alpine.js, no external JS.
    """

    options = options or []

    # Flatten for lookups
    def flatten_items(entries: list[SelectItem | SelectGroup]) -> list[SelectItem]:
        flat: list[SelectItem] = []
        for entry in entries:
            if isinstance(entry, dict) and entry.get("type") == "group":
                flat.extend(entry.get("items", []))
            else:
                flat.append(entry)  # type: ignore[arg-type]
        return flat

    flat_items = flatten_items(options)
    base_id = _coerce_id(id)
    trigger_id = f"{base_id}-trigger"
    popover_id = f"{base_id}-popover"
    listbox_id = f"{base_id}-listbox"

    # Initial label/value
    initial_value = value or (flat_items[0].get("value", "") if flat_items else "")
    # Build initial selected node so icon+label items show their icon in the trigger
    initial_label = placeholder
    initial_selected_node = initial_label
    matched_item: SelectItem | None = None
    for opt in flat_items:
        if opt.get("value") == initial_value:
            matched_item = opt
            break
    if matched_item is not None:
        icon_node = matched_item.get("icon")
        if icon_node is not None:
            initial_selected_node = span(class_="flex items-center gap-2")[
                icon_node, matched_item.get("label", placeholder)
            ]
        else:
            initial_selected_node = matched_item.get("label", placeholder)

    # Trigger button
    trigger = button_component(
        type="button",
        variant="outline",
        id=trigger_id,
        size="md",
        loading=False,
        disabled=disabled,
        icon_only=False,
        class_=f"{width_class} !justify-between font-normal",
        **{
            "aria_haspopup": "listbox",
            "aria_controls": listbox_id,
            ":aria-expanded": "state.open",
            "@click": "state.open ? closeMenu() : openMenu()",
            "@keydown": "onKey($event)",
            "x-ref": "trigger",
        },
    )[
        span(class_="truncate", **{"x-ref": "selected"})[initial_selected_node],
        icon_chevron_down(class_="text-muted-foreground opacity-50 shrink-0"),
    ]

    # Options and groups
    option_nodes: list[Renderable] = []

    def build_item_node(item: SelectItem) -> Renderable:
        children: list[Renderable] = []
        icon_node = item.get("icon")
        if icon_node is not None:
            children.append(
                span(class_="select-content flex items-center gap-2 flex-1 truncate")[
                    icon_node,
                    item.get("label", ""),
                ]
            )
        else:
            children.append(
                span(class_="select-content flex-1 truncate")[item.get("label", "")]
            )
        # trailing check positioned to the far right inside the option
        children.append(
            span(class_="select-check absolute right-2.5 top-1/2 -translate-y-1/2")[
                icon_check(class_="size-4 opacity-50", **{"style": "display: none;"})
            ]
        )
        attrs: dict[str, str] = {
            "data-value": item.get("value", ""),
            # Only plain-text items expose data-label; icon items will use their
            # innerHTML from `.select-content` when updating the trigger.
            "data-label": item.get("label", "") if icon_node is None else "",
            "aria-selected": "true" if item.get("value") == initial_value else "false",
            "@mouseenter": "onHover($el, true)",
            "@mouseleave": "onHover($el, false)",
        }
        return div(
            role="option",
            **attrs,
            class_=(
                "relative flex cursor-pointer items-center gap-2 rounded-sm pl-2 "
                "py-1.5 pr-7.5 text-sm outline-hidden select-none w-full truncate [&_svg]:shrink-0 [&_svg]:size-4 "
                "focus-visible:bg-accent focus-visible:text-accent-foreground hover:bg-accent hover:text-accent-foreground"
            ),
        )[*children]

    group_index = 0
    for entry in options:
        if isinstance(entry, dict) and entry.get("type") == "group":
            group_index += 1
            heading_id = f"group-label-{base_id}-items-{group_index}"
            heading = div(
                role="heading",
                id=heading_id,
                class_="flex text-muted-foreground px-2 py-1.5 text-xs",
            )[entry.get("label", "")]
            option_nodes.append(
                div(role="group", aria_labelledby=heading_id)[
                    heading,
                    *(build_item_node(it) for it in entry.get("items", [])),
                ]
            )
        else:
            option_nodes.append(build_item_node(entry))  # type: ignore[arg-type]

    # Popover body
    pop_children: list[Renderable] = []

    listbox_classes = "p-1"
    if scrollable:
        listbox_classes = f"{listbox_classes} scrollbar overflow-y-auto max-h-64"

    pop_children.append(
        div(
            id=listbox_id,
            role="listbox",
            aria_orientation="vertical",
            aria_labelledby=trigger_id,
            class_=listbox_classes,
            **{
                "x-ref": "listbox",
                "@mousemove": (
                    "$event.target.closest('[role=\"option\"]') && setActiveFromEl($event.target.closest('[role=\"option\"]'))"
                ),
                "@mouseleave": "setActive(-1)",
                "@click": (
                    "$event.target.closest('[role=\"option\"]') && updateFromValue($event.target.closest('[role=\"option\"]').dataset.value); closeMenu()"
                ),
            },
        )[*option_nodes]
    )

    popover = div(
        id=popover_id,
        **{
            "data-popover": "",
            "aria_hidden": "true",
            "x-ref": "popover",
            "x-show": "state.open",
            "x-transition:enter": "transition ease-out duration-200",
            "x-transition:enter-start": "opacity-0 scale-95",
            "x-transition:enter-end": "opacity-100 scale-100",
            "x-transition:leave": "transition ease-in duration-150",
            "x-transition:leave-start": "opacity-100 scale-100",
            "x-transition:leave-end": "opacity-0 scale-95",
            "@click.outside": "closeMenu(false)",
            "data_side": side,
            "data_align": align,
        },
        class_=(
            "absolute left-0 top-full mt-1 z-50 bg-popover text-popover-foreground "
            "rounded-md border shadow-md min-w-[12rem] w-max border-border p-1"
        ),
    )[*pop_children]

    hidden_input = input_(
        type="hidden",
        name=name or f"{base_id}-value",
        value=initial_value,
        **{"x-ref": "input"},
    )

    # Alpine

    initial_value_js = (
        initial_value.replace("'", "\\'") if isinstance(initial_value, str) else ""
    )

    alpine_data: js = f"""{{
        state: {{
            open: false,
            activeIndex: -1,
            selected: '{initial_value_js}'
        }},
        init() {{
            this.$nextTick(() => {{
                this.updateFromValue(this.state.selected, false);
                this.$refs.popover.setAttribute('aria-hidden', 'true');
                this.$el.selectByValue = (v) => this.updateFromValue(v);
            }});
        }},
        setActive(i) {{
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            if (this.state.activeIndex > -1 && opts[this.state.activeIndex]) {{
                opts[this.state.activeIndex].classList.remove('active');
            }}
            this.state.activeIndex = i;
            if (i > -1 && opts[i]) {{
                const el = opts[i];
                el.classList.add('active');
                if (!el.id) el.id = this.$id('opt');
                this.$refs.trigger?.setAttribute('aria-activedescendant', el.id);
            }} else {{
                this.$refs.trigger?.removeAttribute('aria-activedescendant');
            }}
        }},
        setActiveFromEl(el) {{
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            const idx = opts.indexOf(el);
            if (idx > -1) {{
                this.setActive(idx);
            }}
        }},
        onHover(el, enter) {{
            try {{
                if (enter) {{
                    // apply hover bg only when not selected
                    if (el.getAttribute('aria-selected') !== 'true') {{
                        el.style.background = 'rgba(255,255,255,0.03)';
                    }}
                }} else {{
                    // remove hover bg; restore selected bg if needed
                    el.style.background = '';
                    el.style.color = '';
                }}
            }} catch (e) {{}}
        }},

        openMenu() {{
            if ({"true" if disabled else "false"}) return;
            this.state.open = true;
            document.dispatchEvent(new CustomEvent('select:popover', {{ detail: {{ source: this.$el }} }}));
            this.$refs.popover.setAttribute('aria-hidden', 'false');
            this.$refs.trigger?.setAttribute('aria-expanded', 'true');
            this.$nextTick(() => {{
                const sel = this.$refs.listbox.querySelector('[role="option"][aria-selected="true"]');
                if (sel) {{
                    const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                    this.setActive(opts.indexOf(sel));
                    sel.scrollIntoView({{ block: 'nearest' }});
                }}
            }});
        }},
        closeMenu(focus = true) {{
            if (!this.state.open) return;
            this.state.open = false;
            this.$refs.popover.setAttribute('aria-hidden', 'true');
            this.$refs.trigger?.setAttribute('aria-expanded', 'false');
            this.setActive(-1);
            if (focus) this.$refs.trigger?.focus();
        }},
        updateFromValue(val, triggerEvent = true) {{
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            const opt = opts.find((o) => o.dataset.value === val) || opts[0];
            if (!opt) return;
            // When an option has `.select-content` (e.g., icon + label), use it to populate the trigger,
            // otherwise fallback to `data-label`/innerHTML for plain text items.
            const content = opt.querySelector('.select-content');
            this.$refs.selected.innerHTML = content ? content.outerHTML : (opt.dataset.label || opt.innerHTML);
            this.state.selected = opt.dataset.value || '';
            this.$refs.input.value = this.state.selected;
            const prev = this.$refs.listbox.querySelector('[role="option"][aria-selected="true"]');
            if (prev) prev.removeAttribute('aria-selected');
            opt.setAttribute('aria-selected', 'true');
            try {{
                opts.forEach((o) => {{
                    const s = o.querySelector('.select-check svg');
                    if (s) s.style.display = 'none';
                    o.classList.remove('bg-accent', 'text-accent-foreground');
                    // clear hover styles applied by onHover for non-selected items
                    if (o.getAttribute('aria-selected') !== 'true') {{
                        o.style.background = '';
                        o.style.color = '';
                    }}
                }});
                const s = opt.querySelector('.select-check svg');
                if (s) s.style.display = '';
                opt.classList.add('bg-accent', 'text-accent-foreground');
            }} catch (e) {{}}
            if (triggerEvent) this.$el.dispatchEvent(new CustomEvent('change', {{ detail: {{ value: this.state.selected }}, bubbles: true }}));
        }},
        selectCurrent() {{
            if (this.state.activeIndex > -1) {{
                const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                this.updateFromValue(opts[this.state.activeIndex].dataset.value);
                this.closeMenu();
                return;
            }}
            if (this.state.visible.length > 0) {{
                const first = this.state.visible[0];
                this.updateFromValue(first.dataset.value);
                this.closeMenu();
            }}
        }},
        onKey(e) {{
            const open = this.$refs.trigger?.getAttribute('aria-expanded') === 'true';
            if (!['ArrowDown', 'ArrowUp', 'Home', 'End', 'Enter', 'Escape'].includes(e.key)) return;
            if (!open) {{
                if (e.key !== 'Enter' && e.key !== 'Escape') {{
                    e.preventDefault();
                    this.openMenu();
                }}
                return;
            }}
            e.preventDefault();
            const vis = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            if (e.key === 'Escape') {{
                this.closeMenu();
                return;
            }}
            if (vis.length === 0) return;
            let current = this.state.activeIndex > -1 ? vis.indexOf(vis[this.state.activeIndex]) : -1;
            let next = current;
            if (e.key === 'ArrowDown') next = Math.min(current + 1, vis.length - 1);
            else if (e.key === 'ArrowUp') next = Math.max(current - 1, 0);
            else if (e.key === 'Home') next = 0;
            else if (e.key === 'End') next = vis.length - 1;
            else if (e.key === 'Enter') {{
                this.selectCurrent();
                return;
            }}
            if (next !== current) {{
                const el = vis[next];
                const all = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                this.setActive(all.indexOf(el));
                el.scrollIntoView({{ block: 'nearest' }});
            }}
        }} 
    }}"""

    root_attrs: dict[str, str] = {
        "x-data": alpine_data,
        "data-side": side,
        "data-align": align,
        "@click.outside": "closeMenu(false)",
        "@select:popover.window": "if($event.detail.source!==$el) closeMenu(false)",
    }
    root_attrs.update(attrs)

    container_classes = "select relative inline-flex"
    if class_:
        container_classes = f"{container_classes} {class_}"

    if disabled:
        container_classes = f"{container_classes} cursor-not-allowed"

    return div(id=base_id, class_=container_classes, **root_attrs)[
        hidden_input, trigger, popover
    ]
