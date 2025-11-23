from htpy import Node
from htpy import Renderable
from htpy import button
from htpy import div
from htpy import nav

from ._styles import CARD_BASE_CLASSES
from ._styles import TAB_BASE_CLASSES
from ._styles import TAB_LIST_CONTAINER_CLASSES
from ._styles import TAB_SELECTED_CLASSES
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
        tab_elements.append(
            button(
                type="button",
                **{
                    "role": "tab",
                    "id": f"{container_id}-tab-{index}",
                    "aria-controls": f"{container_id}-panel-{index}",
                    ":aria-selected": f"activeTab === {index}",
                    ":tabindex": f"activeTab === {index} ? '0' : '-1'",
                    "@click": f"activeTab = {index}",
                    "x-ref": f"tab{index}",
                    ":class": f"activeTab === {index} ? '{TAB_SELECTED_CLASSES}' : ''",
                    "disabled": "true" if tab_value in disabled_values else None,
                },
                class_=TAB_BASE_CLASSES,
            )[tab_label]
        )

    # Create panels with Alpine.js show/hide
    panel_elements = []
    for index, (tab_value, tab_label, tab_content) in enumerate(normalized):
        # Panel background and container styling to match card component (no extra padding)
        panel_elements.append(
            div(
                **{
                    "role": "tabpanel",
                    "id": f"{container_id}-panel-{index}",
                    "aria-labelledby": f"{container_id}-tab-{index}",
                    "tabindex": "-1",
                    ":aria-selected": f"activeTab === {index}",
                    ":hidden": f"activeTab !== {index}",
                },
                class_=(f"mt-3 outline-none {CARD_BASE_CLASSES}" if background else "mt-3"),
            )[tab_content]
        )

    # Tab list container with keyboard navigation
    # Create nav for tabs
    nav_attrs = {
        "role": "tablist",
        "class_": TAB_LIST_CONTAINER_CLASSES,
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
    container_classes = merge_classes("flex flex-col gap-2", class_)
    alpine_attrs["class_"] = container_classes

    return div(**alpine_attrs)[tab_list, *panel_elements]
