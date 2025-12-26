from htpy import Renderable
from htpy import div
from htpy import input as input_
from htpy import label
from htpy import option
from htpy import select
from htpy import span
from sourcetypes import js

from ._styles import FOCUS_ACCENT_CLASSES
from ._styles import ICON_INLINE_CLASSES
from ._styles import LISTBOX_EMPTY_CLASSES
from ._styles import LISTBOX_OPTION_BASE_CLASSES
from ._styles import LISTBOX_SECTION_HEADING_CLASSES
from ._styles import POPOVER_PANEL_PADDED_CLASSES
from ._styles import SELECT_NATIVE_BASE_CLASSES
from ._types import SelectGroup
from ._types import SelectItem
from ._types import SelectOption
from .button import button_component
from .icons import icon_check
from .icons import icon_chevron_down
from .icons import icon_circle_alert


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
    """Render a Basecoat-style native ``<select>`` element.

    Args:
        id: Element id applied to the select as well as the optional label.
        name: Name attribute used during form submissions.
        options: Sequence of ``SelectOption`` dictionaries containing ``value`` and ``label`` keys.
        value: Currently selected option value.
        placeholder: Placeholder text rendered as a disabled option when ``multiple`` is False.
        label_text: Optional label text shown above the control.
        error: Validation text rendered below the control.
        disabled: Whether the select should be disabled.
        required: Whether the select should be marked as required.
        multiple: Whether multiple selections are allowed.
        size: Number of visible rows for multi-selects.
        class_: Additional CSS classes appended to the select element.
        **attrs: Additional HTML attributes forwarded to the ``<select>`` tag.

    Returns:
        Renderable: htpy nodes for the label (if any), the select element, and error text.
    """

    # Use shared native select base classes
    base_classes = SELECT_NATIVE_BASE_CLASSES

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
            option(value="", disabled="true", selected="" if value is None else None)[placeholder]
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
        elements.append(span(class_="text-sm text-destructive", **{"role": "alert"})[error])

    # Return single element or fragment
    if len(elements) == 1:
        return elements[0]
    else:
        from htpy import div

        return div(class_="space-y-1")[*elements]


def _coerce_id(id_hint: str | None) -> str:
    """Return ``id_hint`` or generate a deterministic fallback.

    Args:
        id_hint: Caller-provided id.

    Returns:
        str: Stable id suitable for component roots.
    """

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
    empty_text: str = "No options available",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render the popover-based single-select component.

    Args:
        id: Component root id; generated when omitted.
        name: Hidden input name used when submitting the selected value.
        options: List of ``SelectItem`` entries or grouped sections describing the listbox content.
        value: Option value selected on load.
        placeholder: Text displayed in the trigger when no value is selected.
        disabled: Whether user interaction should be disabled.
        side: Popover placement relative to the trigger element.
        align: Popover alignment relative to the trigger.
        width_class: Tailwind width utilities shared by the trigger and popover.
        scrollable: Whether the listbox scrolls when overflowing its max height.
        empty_text: Message displayed when ``options`` does not contain selectable entries.
        class_: Additional CSS classes appended to the root container.
        **attrs: Additional HTML attributes forwarded to the component root.

    Returns:
        Renderable: htpy structure containing the hidden input, trigger button, and popover listbox.
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
        class_=f"{width_class} justify-between! font-normal",
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
    has_selectable_item = False

    def build_item_node(item: SelectItem) -> Renderable:
        nonlocal has_selectable_item
        has_selectable_item = True
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
            children.append(span(class_="select-content flex-1 truncate")[item.get("label", "")])
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
        }
        # Use data-selected for CSS styling of selected state
        # aria-selected:bg-accent handles selected items, hover:bg-accent handles hover
        return div(
            role="option",
            **attrs,
            class_=f"{LISTBOX_OPTION_BASE_CLASSES} transition-none aria-selected:bg-accent aria-selected:text-accent-foreground",
        )[*children]

    group_index = 0
    for entry in options:
        if isinstance(entry, dict) and entry.get("type") == "group":
            group_index += 1
            heading_id = f"group-label-{base_id}-items-{group_index}"
            heading = div(
                role="heading",
                id=heading_id,
                class_=LISTBOX_SECTION_HEADING_CLASSES,
            )[entry.get("label", "")]
            option_nodes.append(
                div(role="group", aria_labelledby=heading_id)[
                    heading,
                    *(build_item_node(it) for it in entry.get("items", [])),
                ]
            )
        else:
            option_nodes.append(build_item_node(entry))  # type: ignore[arg-type]

    if not has_selectable_item:
        option_nodes.append(
            div(
                class_=LISTBOX_EMPTY_CLASSES,
                aria_hidden="true",
            )[icon_circle_alert(), span(class_="text-sm")[empty_text]],
        )

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
            "x-cloak": "",
            "x-transition:enter": "transition ease-out duration-200",
            "x-transition:enter-start": "opacity-0 scale-95",
            "x-transition:enter-end": "opacity-100 scale-100",
            "x-transition:leave": "transition ease-in duration-150",
            "x-transition:leave-start": "opacity-100 scale-100",
            "x-transition:leave-end": "opacity-0 scale-95",
            "data_side": side,
            "data_align": align,
        },
        class_=f"{POPOVER_PANEL_PADDED_CLASSES} fixed min-w-48 w-max z-[9999]",
    )[*pop_children]

    hidden_input = input_(
        type="hidden",
        name=name or f"{base_id}-value",
        value=initial_value,
        **{"x-ref": "input"},
    )

    # Alpine

    initial_value_js = initial_value.replace("'", "\\'") if isinstance(initial_value, str) else ""

    alpine_data: js = f"""{{
        state: {{
            open: false,
            activeIndex: -1,
            selected: '{initial_value_js}'
        }},
        _scrollHandler: null,
        _resizeHandler: null,
        _clickOutsideHandler: null,
        init() {{
            this.$nextTick(() => {{
                this.updateFromValue(this.state.selected, false);
                this.$refs.popover.setAttribute('aria-hidden', 'true');
                this.$el.selectByValue = (v) => this.updateFromValue(v);
            }});
            // Click outside handler
            this._clickOutsideHandler = (e) => {{
                if (this.state.open && !this.$el.contains(e.target) && !this.$refs.popover.contains(e.target)) {{
                    this.closeMenu(false);
                }}
            }};
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
            // Decide whether to show above or below
            let top;
            if (spaceBelow >= popoverHeight || spaceBelow >= spaceAbove) {{
                top = rect.bottom + 4;
            }} else {{
                top = rect.top - popoverHeight - 4;
            }}
            // Horizontal positioning
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
        openMenu() {{
            if ({"true" if disabled else "false"}) return;
            this.state.open = true;
            document.dispatchEvent(new CustomEvent('select:popover', {{ detail: {{ source: this.$el }} }}));
            this.$refs.popover.setAttribute('aria-hidden', 'false');
            this.$refs.trigger?.setAttribute('aria-expanded', 'true');
            this.$nextTick(() => {{
                this._positionPopover();
                this._addPositionListeners();
                document.addEventListener('click', this._clickOutsideHandler, true);
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
            this._removePositionListeners();
            document.removeEventListener('click', this._clickOutsideHandler, true);
            this.$refs.popover.setAttribute('aria-hidden', 'true');
            this.$refs.trigger?.setAttribute('aria-expanded', 'false');
            this.setActive(-1);
            if (focus) this.$refs.trigger?.focus();
        }},
        updateFromValue(val, triggerEvent = true) {{
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            const opt = opts.find((o) => o.dataset.value === val) || opts[0];
            if (!opt) return;
            const content = opt.querySelector('.select-content');
            this.$refs.selected.innerHTML = content ? content.outerHTML : (opt.dataset.label || opt.innerHTML);
            this.state.selected = opt.dataset.value || '';
            this.$refs.input.value = this.state.selected;
            // Update aria-selected attributes - CSS handles the styling via aria-selected:bg-accent
            const prev = this.$refs.listbox.querySelector('[role="option"][aria-selected="true"]');
            if (prev) prev.setAttribute('aria-selected', 'false');
            opt.setAttribute('aria-selected', 'true');
            // Update checkmark visibility
            try {{
                opts.forEach((o) => {{
                    const s = o.querySelector('.select-check svg');
                    if (s) s.style.display = 'none';
                }});
                const s = opt.querySelector('.select-check svg');
                if (s) s.style.display = '';
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
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            if (opts.length > 0) {{
                this.updateFromValue(opts[0].dataset.value);
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
        "@select:popover.window": "if($event.detail.source!==$el) closeMenu(false)",
    }
    root_attrs.update(attrs)

    container_classes = "select relative inline-flex"
    if class_:
        container_classes = f"{container_classes} {class_}"

    if disabled:
        container_classes = f"{container_classes} cursor-not-allowed"

    return div(id=base_id, class_=container_classes, **root_attrs)[hidden_input, trigger, popover]


def multiselect_component(
    *,
    id: str | None = None,
    name: str | None = None,
    options: list[SelectItem | SelectGroup] | None = None,
    values: list[str] | None = None,
    placeholder: str = "Select options...",
    disabled: bool = False,
    side: str = "bottom",
    align: str = "start",
    width_class: str = "w-[220px]",
    scrollable: bool = True,
    empty_text: str = "No options available",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render the popover-based multiselect component.

    Args:
        id: Component root id; generated automatically when omitted.
        name: Form field name applied to each generated hidden input.
        options: List of ``SelectItem`` entries and/or grouped sections displayed inside the popover.
        values: Iterable of option values that should be pre-selected on load.
        placeholder: Text shown in the trigger when nothing is selected.
        disabled: Whether the trigger is interactive.
        side: Popover placement relative to the trigger.
        align: Popover alignment relative to the trigger.
        width_class: Tailwind width utility shared by the trigger and popover.
        scrollable: Whether the options container gains scrolling when overflowing.
        empty_text: Message displayed when no options exist.
        class_: Additional CSS classes appended to the root container.
        **attrs: Additional HTML attributes forwarded to the root container.

    Returns:
        Renderable: htpy structure containing the trigger, checkbox-style listbox, and generated hidden inputs.

    Notes:
        - Items remain selected while the popover stays open for easier multi-selection.
        - Key bindings mirror the single-select component and include Enter for toggling.
        - A ``change`` CustomEvent fires with the latest ``values`` when selections change.

    Examples:
        Traditional Django form submission:

        ```html
        <input type="hidden" name="{name}" value="value1" />
        <input type="hidden" name="{name}" value="value2" />
        ```

        ```python
        selected_values = request.POST.getlist("field_name")
        ```
    """

    options = options or []

    # (No need to pre-flatten; we render groups inline)
    base_id = _coerce_id(id)
    trigger_id = f"{base_id}-trigger"
    popover_id = f"{base_id}-popover"
    listbox_id = f"{base_id}-listbox"
    inputs_id = f"{base_id}-inputs"

    initial_values = values or []
    option_classes = (
        "relative flex cursor-pointer items-center gap-2 rounded-sm pl-2 py-1.5 pr-7.5 "
        "text-sm outline-hidden select-none w-full truncate transition-none mb-1 "
        f"{ICON_INLINE_CLASSES} "
        f"{FOCUS_ACCENT_CLASSES} hover:bg-accent hover:text-accent-foreground "
        "aria-selected:bg-accent aria-selected:text-accent-foreground "
        "aria-selected:hover:bg-accent/80"
    )

    # Trigger button
    trigger = button_component(
        type="button",
        variant="outline",
        id=trigger_id,
        size="md",
        loading=False,
        disabled=disabled,
        icon_only=False,
        class_=f"{width_class} justify-between! font-normal",
        **{
            "aria_haspopup": "listbox",
            "aria_controls": listbox_id,
            ":aria-expanded": "state.open",
            "@click": "state.open ? closeMenu() : openMenu()",
            "@keydown": "onKey($event)",
            "x-ref": "trigger",
        },
    )[
        span(class_="truncate", **{"x-ref": "selected"}),
        icon_chevron_down(class_="text-muted-foreground opacity-50 shrink-0"),
    ]

    # Option nodes (items and groups)
    option_nodes: list[Renderable] = []
    has_selectable_item = False

    def build_item_node(item: SelectItem) -> Renderable:
        nonlocal has_selectable_item
        has_selectable_item = True
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
            children.append(span(class_="select-content flex-1 truncate")[item.get("label", "")])
        children.append(
            span(class_="select-check absolute right-2.5 top-1/2 -translate-y-1/2")[
                icon_check(class_="size-4 opacity-50", **{"style": "display: none;"})
            ]
        )
        attrs_i: dict[str, str] = {
            "data-value": item.get("value", ""),
            "data-label": item.get("label", "") if icon_node is None else "",
            # aria-selected managed by Alpine; seed from initial values
            "aria-selected": "true" if item.get("value") in initial_values else "false",
        }
        return div(
            role="option",
            **attrs_i,
            class_=option_classes,
        )[*children]

    group_index = 0
    for entry in options:
        if isinstance(entry, dict) and entry.get("type") == "group":
            group_index += 1
            heading_id = f"group-label-{base_id}-items-{group_index}"
            heading = div(
                role="heading",
                id=heading_id,
                class_=LISTBOX_SECTION_HEADING_CLASSES,
            )[entry.get("label", "")]
            option_nodes.append(
                div(role="group", aria_labelledby=heading_id)[
                    heading,
                    *(build_item_node(it) for it in entry.get("items", [])),
                ]
            )
        else:
            option_nodes.append(build_item_node(entry))  # type: ignore[arg-type]

    if not has_selectable_item:
        option_nodes.append(
            div(
                class_=LISTBOX_EMPTY_CLASSES,
                aria_hidden="true",
            )[icon_circle_alert(), span(class_="text-sm")[empty_text]],
        )

    # Popover body
    listbox_classes = "p-1"
    if scrollable:
        listbox_classes = f"{listbox_classes} scrollbar overflow-y-auto max-h-64"

    popover = div(
        id=popover_id,
        **{
            "data-popover": "",
            "aria_hidden": "true",
            "x-ref": "popover",
            "x-show": "state.open",
            "x-cloak": "",
            "x-transition:enter": "transition ease-out duration-200",
            "x-transition:enter-start": "opacity-0 scale-95",
            "x-transition:enter-end": "opacity-100 scale-100",
            "x-transition:leave": "transition ease-in duration-150",
            "x-transition:leave-start": "opacity-100 scale-100",
            "x-transition:leave-end": "opacity-0 scale-95",
            "data_side": side,
            "data_align": align,
        },
        class_=f"{POPOVER_PANEL_PADDED_CLASSES} fixed min-w-48 w-max z-[9999]",
    )[
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
                    "$event.target.closest('[role=\"option\"]') && toggleFromEl($event.target.closest('[role=\"option\"]'))"
                ),
            },
        )[*option_nodes]
    ]

    # Hidden inputs container (managed entirely by Alpine)
    inputs_container = div(id=inputs_id, **{"x-ref": "inputs"})

    # Alpine state
    def _escape_js(s: str) -> str:
        return s.replace("'", "\\'")

    initial_values_js = "[" + ",".join(f"'{_escape_js(v)}'" for v in initial_values) + "]"
    input_name_js = (name or f"{base_id}-values").replace("'", "\\'")

    alpine_data: js = f"""{{
        state: {{
            open: false,
            activeIndex: -1,
            selected: {initial_values_js}
        }},
        _scrollHandler: null,
        _resizeHandler: null,
        _clickOutsideHandler: null,
        init() {{
            this.$nextTick(() => {{
                this.updateTrigger(false);
                this.$refs.popover.setAttribute('aria-hidden', 'true');
                this.syncHiddenInputs();
                this.applySelectionStyles();
            }});
            this._clickOutsideHandler = (e) => {{
                if (this.state.open && !this.$el.contains(e.target) && !this.$refs.popover.contains(e.target)) {{
                    this.closeMenu(false);
                }}
            }};
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
            if (idx > -1) this.setActive(idx);
        }},
        openMenu() {{
            if ({"true" if disabled else "false"}) return;
            this.state.open = true;
            document.dispatchEvent(new CustomEvent('multiselect:popover', {{ detail: {{ source: this.$el }} }}));
            this.$refs.popover.setAttribute('aria-hidden', 'false');
            this.$refs.trigger?.setAttribute('aria-expanded', 'true');
            this.$nextTick(() => {{
                this._positionPopover();
                this._addPositionListeners();
                document.addEventListener('click', this._clickOutsideHandler, true);
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
            this._removePositionListeners();
            document.removeEventListener('click', this._clickOutsideHandler, true);
            this.$refs.popover.setAttribute('aria-hidden', 'true');
            this.$refs.trigger?.setAttribute('aria-expanded', 'false');
            this.setActive(-1);
            if (focus) this.$refs.trigger?.focus();
        }},
        toggleFromEl(el) {{
            if (!el) return;
            const val = el.dataset.value || '';
            this.toggleValue(val);
        }},
        toggleValue(val) {{
            const idx = this.state.selected.indexOf(val);
            if (idx > -1) this.state.selected.splice(idx, 1);
            else this.state.selected.push(val);
            this.applySelectionStyles();
            this.updateTrigger();
            this.syncHiddenInputs();
        }},
        applySelectionStyles() {{
            try {{
                const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                opts.forEach((o) => {{
                    const selected = this.state.selected.includes(o.dataset.value || '');
                    o.setAttribute('aria-selected', String(selected));
                    o.dataset.selected = selected ? 'true' : 'false';
                    const s = o.querySelector('.select-check svg');
                    if (s) s.style.display = selected ? '' : 'none';
                }});
            }} catch (e) {{}}
        }},
        updateTrigger(triggerEvent = true) {{
            const ph = '{placeholder}';
            const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
            const labels = this.state.selected.map((v) => {{
                const opt = opts.find((o) => o.dataset.value === v);
                if (!opt) return v;
                const content = opt.querySelector('.select-content');
                const txt = (opt.dataset.label || (content ? content.textContent : opt.textContent) || '').trim();
                return txt;
            }}).filter(Boolean);
            if (labels.length === 0) {{
                this.$refs.selected.textContent = ph;
                this.$refs.selected.removeAttribute('title');
            }} else {{
                const triggerWidth = this.$refs.trigger ? this.$refs.trigger.clientWidth : 180;
                const approxCharPx = 8;
                const maxChars = Math.max(10, Math.floor(triggerWidth / approxCharPx) - 8);
                let acc = '';
                let shown = [];
                for (const lbl of labels) {{
                    const next = shown.length ? (acc + '; ' + lbl) : lbl;
                    if (next.length > maxChars) break;
                    shown.push(lbl);
                    acc = next;
                }}
                const hiddenCount = labels.length - shown.length;
                const display = hiddenCount > 0 ? (shown.join('; ') + ' …') : shown.join('; ');
                this.$refs.selected.textContent = display;
                this.$refs.selected.setAttribute('title', labels.join('; '));
            }}
            if (triggerEvent) this.$el.dispatchEvent(new CustomEvent('change', {{ detail: {{ values: this.state.selected.slice() }}, bubbles: true }}));
        }},
        syncHiddenInputs() {{
            try {{
                const container = this.$refs.inputs;
                while (container.firstChild) container.removeChild(container.firstChild);
                const nm = '{input_name_js}';
                this.state.selected.forEach((v) => {{
                    const i = document.createElement('input');
                    i.type = 'hidden';
                    i.name = nm;
                    i.value = v;
                    container.appendChild(i);
                }});
            }} catch (e) {{}}
        }},
        selectCurrent() {{
            if (this.state.activeIndex > -1) {{
                const opts = Array.from(this.$refs.listbox.querySelectorAll('[role="option"]'));
                const val = opts[this.state.activeIndex].dataset.value;
                if (val != null) this.toggleValue(val);
                return;
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
        "@multiselect:popover.window": "if($event.detail.source!==$el) closeMenu(false)",
    }
    root_attrs.update(attrs)

    container_classes = "select relative inline-flex"
    if class_:
        container_classes = f"{container_classes} {class_}"
    if disabled:
        container_classes = f"{container_classes} cursor-not-allowed"

    return div(id=base_id, class_=container_classes, **root_attrs)[
        inputs_container, trigger, popover
    ]
