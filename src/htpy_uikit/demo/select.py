from htpy import Node, div, p

from htpy_uikit.components.icons import icon_bar, icon_line, icon_pie
from htpy_uikit.components.select import (
    multiselect_component,
    native_select,
    select_component,
)

from ._utils import _demo_section


def select_section() -> Node:
    return _demo_section(
        "Select",
        "Dropdown selection menus",
        [
            div(class_="flex flex-wrap items-center gap-2 md:flex-row")[
                native_select(
                    class_="w-[180px]",
                    options=[
                        {"value": "apple", "label": "Apple"},
                        {"value": "banana", "label": "Banana"},
                        {"value": "blueberry", "label": "Blueberry"},
                    ],
                    placeholder="Fruits",
                ),
                native_select(
                    class_="w-[180px]",
                    options=[{"value": "disabled", "label": "Disabled"}],
                    value="disabled",
                    disabled=True,
                ),
            ],
            div(class_="flex flex-wrap items-center gap-4 mt-4")[
                # Default popover select with groups-like data
                select_component(
                    id="select-default",
                    width_class="w-[180px]",
                    options=[
                        {
                            "type": "group",
                            "label": "Fruits",
                            "items": [
                                {
                                    "type": "item",
                                    "value": "apple",
                                    "label": "Apple",
                                },
                                {
                                    "type": "item",
                                    "value": "banana",
                                    "label": "Banana",
                                },
                                {
                                    "type": "item",
                                    "value": "blueberry",
                                    "label": "Blueberry",
                                },
                            ],
                        },
                        {
                            "type": "group",
                            "label": "Grapes",
                            "items": [
                                {
                                    "type": "item",
                                    "value": "pineapple",
                                    "label": "Pineapple",
                                },
                            ],
                        },
                    ],
                    value="apple",
                ),
                # Scrollable long list
                select_component(
                    id="select-scrollbar",
                    width_class="w-[180px]",
                    scrollable=True,
                    options=[
                        *({"value": f"item-{i}", "label": f"Item {i}"} for i in range(0, 99))
                    ],
                    value="item-0",
                ),
                # Disabled
                select_component(
                    id="select-disabled",
                    width_class="w-[180px]",
                    options=[{"value": "disabled", "label": "Disabled"}],
                    value="disabled",
                    disabled=True,
                ),
                # With icon in options
                select_component(
                    id="select-with-icon",
                    width_class="w-[180px]",
                    options=[
                        {
                            "type": "group",
                            "label": "Charts",
                            "items": [
                                {
                                    "type": "item",
                                    "value": "bar",
                                    "label": "Bar",
                                    "icon": icon_bar(class_="text-muted-foreground"),
                                },
                                {
                                    "type": "item",
                                    "value": "line",
                                    "label": "Line",
                                    "icon": icon_line(class_="text-muted-foreground"),
                                },
                                {
                                    "type": "item",
                                    "value": "pie",
                                    "label": "Pie",
                                    "icon": icon_pie(class_="text-muted-foreground"),
                                },
                            ],
                        }
                    ],
                    value="bar",
                ),
            ],
            div(class_="grid gap-3 mt-6 max-w-4xl")[
                p(class_="text-sm text-muted-foreground")[
                    "Multiselect popover with grouped items and icon options."
                ],
                div(class_="flex flex-wrap items-start gap-4")[
                    multiselect_component(
                        id="multiselect-fruits",
                        name="favorite-fruits",
                        width_class="w-[240px]",
                        options=[
                            {
                                "type": "group",
                                "label": "Berries",
                                "items": [
                                    {
                                        "type": "item",
                                        "value": "strawberry",
                                        "label": "Strawberry",
                                    },
                                    {
                                        "type": "item",
                                        "value": "blueberry",
                                        "label": "Blueberry",
                                    },
                                    {
                                        "type": "item",
                                        "value": "raspberry",
                                        "label": "Raspberry",
                                    },
                                ],
                            },
                            {
                                "type": "group",
                                "label": "Tropical",
                                "items": [
                                    {
                                        "type": "item",
                                        "value": "pineapple",
                                        "label": "Pineapple",
                                    },
                                    {"type": "item", "value": "mango", "label": "Mango"},
                                    {"type": "item", "value": "kiwi", "label": "Kiwi"},
                                ],
                            },
                        ],
                        values=["blueberry", "mango"],
                    ),
                    multiselect_component(
                        id="multiselect-charts",
                        name="chart-types",
                        width_class="w-[240px]",
                        options=[
                            {
                                "type": "item",
                                "value": "bar",
                                "label": "Bar",
                                "icon": icon_bar(class_="text-muted-foreground"),
                            },
                            {
                                "type": "item",
                                "value": "line",
                                "label": "Line",
                                "icon": icon_line(class_="text-muted-foreground"),
                            },
                            {
                                "type": "item",
                                "value": "pie",
                                "label": "Pie",
                                "icon": icon_pie(class_="text-muted-foreground"),
                            },
                            {
                                "type": "item",
                                "value": "area",
                                "label": "Area",
                                "icon": icon_pie(class_="text-muted-foreground rotate-90"),
                            },
                            {
                                "type": "item",
                                "value": "donut",
                                "label": "Donut",
                                "icon": icon_pie(class_="text-muted-foreground/80"),
                            },
                        ],
                        values=["bar", "line"],
                        placeholder="Pick chart types",
                    ),
                ],
            ],
        ],
    )
