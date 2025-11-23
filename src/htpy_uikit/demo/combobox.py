from htpy import Node, div

from htpy_uikit.components.combobox import combobox

from ._utils import _demo_section


def combobox_section() -> Node:
    return _demo_section(
        "Combobox",
        "Searchable dropdown selections",
        [
            div(class_="grid grid-cols-1 md:grid-cols-2 gap-4")[
                # Simple combobox
                combobox(
                    name="fruit",
                    options=[
                        {"value": "apple", "label": "Apple"},
                        {"value": "banana", "label": "Banana"},
                        {"value": "orange", "label": "Orange"},
                        {"value": "grape", "label": "Grape"},
                    ],
                    placeholder="Select a fruit...",
                    width_class="w-[220px]",
                ),
                # Combobox with initial value and wider popover
                combobox(
                    name="framework",
                    options=[
                        {"value": "next", "label": "Next.js"},
                        {"value": "svelte", "label": "SvelteKit"},
                        {"value": "nuxt", "label": "Nuxt.js"},
                        {"value": "remix", "label": "Remix"},
                        {"value": "astro", "label": "Astro"},
                    ],
                    value="svelte",
                    placeholder="Search framework...",
                    width_class="w-[220px]",
                    popover_width_class="w-72",
                ),
            ]
        ],
    )
