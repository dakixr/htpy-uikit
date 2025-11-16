from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import nav

from ._types import TabContentItem
from ._utils import merge_classes


def tabs(
    tabs_content: list[TabContentItem],
    active_tab: str,
    *,
    id: str | None = None,
    class_: str | None = None,
    disabled_values: set[str] | None = None,
    background: bool = True,
    **kwargs,
) -> Renderable:
    """Render Basecoat-style tabs with Alpine state management.

    Args:
        tabs_content: Sequence of tab dictionaries with ``value``, ``label``, and ``content``.
        active_tab: Value of the currently selected tab.
        id: Optional id for the tabs container; generated from content when omitted.
        class_: Extra classes appended to the tabs container.
        disabled_values: Tab values that should be disabled.
        background: Whether to wrap tab panels in card-like backgrounds.
        **kwargs: Additional HTML attributes forwarded to the tabs container.

    Returns:
        Renderable: Tabs wrapper containing the tablist and panels.
    """
    # Validate and normalize input (must be list of TabContentItem dicts)
    tab_elements = []
    container_id = id or f"simple-tabs-{hash(str(tabs_content))}"

    disabled_values = disabled_values or set()

    normalized: list[tuple[str, Node, Node]] = []
    for item in tabs_content:
        if not isinstance(item, dict):
            raise TypeError("tabs_content must be a list of TabContentItem mappings")
        v = item.get("value")
        lbl = item.get("label")
        cnt = item.get("content")
        if v is None:
            raise ValueError("TabContentItem missing required 'value' key")
        if item.get("disabled"):
            disabled_values.add(v)
        normalized.append((v, lbl or "", cnt or div[""]))

    # Determine active index after normalization
    active_index = next((i for i, (val, _, _) in enumerate(normalized) if val == active_tab), 0)

    for index, (tab_value, tab_label, tab_content) in enumerate(normalized):
        tab_id = f"{container_id}-tab-{index}"
        panel_id = f"{container_id}-panel-{index}"

        tab_classes_btn_base = (
            "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:outline-ring "
            "text-muted-foreground inline-flex h-[calc(100%_-_1px)] flex-1 "
            "items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 "
            "text-sm font-medium whitespace-nowrap transition-[color,box-shadow] focus-visible:ring-[3px] "
            "focus-visible:outline-1 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed "
            "[&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4"
        )
        selected_classes = "bg-background text-foreground dark:text-foreground dark:border-input dark:bg-input/30 shadow-sm"

        is_disabled = tab_value in disabled_values

        tab_elements.append(
            button(
                type="button",
                **{
                    "role": "tab",
                    "id": tab_id,
                    "aria-controls": panel_id,
                    ":aria-selected": f"activeTab === {index}",
                    ":tabindex": f"activeTab === {index} ? '0' : '-1'",
                    "@click": f"activeTab = {index}",
                    "x-ref": f"tab{index}",
                    ":class": f"activeTab === {index} ? '{selected_classes}' : ''",
                    "disabled": "true" if is_disabled else None,
                },
                class_=tab_classes_btn_base,
            )[tab_label]
        )

    # Create panels with Alpine.js show/hide
    panel_elements = []
    for index, (tab_value, tab_label, tab_content) in enumerate(normalized):
        panel_id = f"{container_id}-panel-{index}"
        tab_id = f"{container_id}-tab-{index}"

        # Panel background and container styling to match card component (no extra padding)
        panel_elements.append(
            div(
                **{
                    "role": "tabpanel",
                    "id": panel_id,
                    "aria-labelledby": tab_id,
                    "tabindex": "-1",
                    ":aria-selected": f"activeTab === {index}",
                    ":hidden": f"activeTab !== {index}",
                },
                class_=(
                    "mt-3 outline-none bg-card text-card-foreground rounded-xl "
                    "border border-border shadow-sm"
                    if background
                    else "mt-3"
                ),
            )[tab_content]
        )

    # Tab list container with keyboard navigation
    # Create nav for tabs
    nav_attrs = {
        "role": "tablist",
        "class_": (
            "bg-muted text-muted-foreground inline-flex h-9 w-full items-center "
            "justify-center rounded-lg p-[3px]"
        ),
        "@keydown.arrow-right.prevent": "activeTab = (activeTab + 1) % numTabs; $refs['tab'+activeTab].focus()",
        "@keydown.arrow-left.prevent": "activeTab = (activeTab - 1 + numTabs) % numTabs; $refs['tab'+activeTab].focus()",
        "@keydown.home.prevent": "activeTab = 0; $refs['tab'+activeTab].focus()",
        "@keydown.end.prevent": "activeTab = numTabs - 1; $refs['tab'+activeTab].focus()",
    }

    tab_list = nav(**nav_attrs)[*tab_elements]

    # Alpine.js container
    alpine_attrs = {
        "x-data": f"{{ activeTab: {active_index}, numTabs: {len(tabs_content)} }}",
        "id": container_id,
        **kwargs,
    }

    # Tabs container
    container_classes = merge_classes("tabs flex flex-col gap-2", class_)
    alpine_attrs["class_"] = container_classes

    return div(**alpine_attrs)[tab_list, *panel_elements]
