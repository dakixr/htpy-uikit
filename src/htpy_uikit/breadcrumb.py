from typing import List
from typing import Literal
from typing import TypedDict

from htpy import Renderable
from htpy import a
from htpy import div
from htpy import li
from htpy import ol
from htpy import span

from htpy_uikit.utils import merge_classes
from htpy_uikit.utils import random_string

from .dropdown_menu import dropdown_menu
from .dropdown_menu import dropdown_menu_item
from .dropdown_menu import dropdown_menu_label
from .dropdown_menu import dropdown_menu_separator
from .icons import icon_arrow_right
from .icons import icon_chevron_right
from .icons import icon_more

# Type definitions for breadcrumb component
BreadcrumbSeparator = Literal["chevron", "slash", "arrow"]


class BreadcrumbItem(TypedDict):
    """Option structure for breadcrumb items."""

    label: str
    url: str | None


def breadcrumb(
    items: List[BreadcrumbItem],
    *,
    separator: BreadcrumbSeparator = "chevron",
    class_: str | None = None,
    collapse: bool = True,
    max_visible: int = 4,
    **attrs,
) -> Renderable:
    """
    Basecoat-style breadcrumb navigation component.

    Based on Basecoat UI breadcrumb implementation.
    Note: Basecoat doesn't have a dedicated breadcrumb component,
    this uses standard HTML elements with breadcrumb styling.

    Args:
        items: List of BreadcrumbItem dictionaries with label and url
        separator: Separator style
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.ol: Breadcrumb component
    """

    # Base classes - following basecoat breadcrumb styling
    base_classes = "text-muted-foreground flex flex-wrap items-center gap-1.5 text-sm break-words sm:gap-2.5"

    # Add class to attrs
    attrs["class_"] = merge_classes(base_classes, class_)

    # Separator icons - reuse icons for consistent visuals
    separators: dict[BreadcrumbSeparator, Renderable] = {
        "chevron": icon_chevron_right(class_="size-3.5"),
        "slash": span()["/"],
        "arrow": icon_arrow_right(class_="size-3.5"),
    }

    # Build breadcrumb items, optionally collapsing middle items into an overflow menu
    breadcrumb_items: list[Renderable] = []
    total_items = len(items)

    # Decide rendering sequence: full list or collapsed with a menu placeholder
    if collapse and total_items > max_visible and max_visible >= 3:
        tail_count = max_visible - 2
        head = [items[0]]
        tail = items[-tail_count:]
        middle = items[1 : total_items - tail_count]

        sequence: list[BreadcrumbItem | tuple[str, list[BreadcrumbItem]]] = []
        sequence.extend(head)
        sequence.append(("__menu__", middle))
        sequence.extend(tail)
    else:
        sequence = list(items)

    for index, entry in enumerate(sequence):
        is_last = index == len(sequence) - 1

        if isinstance(entry, tuple) and entry[0] == "__menu__":
            middle_items = entry[1]
            assert isinstance(middle_items, list)
            menu_id = f"breadcrumb-menu-{random_string(6)}"

            menu_nodes = [
                dropdown_menu_label["History"],
                dropdown_menu_separator(),
                *[
                    dropdown_menu_item(
                        a(href=item["url"])[item["label"]]
                        if item["url"]
                        else item["label"]
                    )
                    for item in middle_items
                ],
            ]

            breadcrumb_items.append(
                li(class_="inline-flex items-center gap-1.5")[
                    dropdown_menu(
                        trigger=icon_more(
                            class_="size-4 cursor-pointer hover:text-foreground"
                        ),
                        id=menu_id,
                    )[div(class_="flex flex-col")[*menu_nodes]]
                ]
            )
        elif isinstance(entry, dict):
            label = entry["label"]
            url = entry["url"]

            if url:
                breadcrumb_items.append(
                    li(class_="inline-flex items-center gap-1.5")[
                        a(href=url, class_="hover:text-foreground transition-colors")[
                            label
                        ]
                    ]
                )
            else:
                breadcrumb_items.append(
                    li(class_="inline-flex items-center gap-1.5")[
                        span(
                            class_="text-foreground font-normal",
                            **{"aria-current": "page"},
                        )[label]
                    ]
                )

        if not is_last:
            separator_element = separators[separator]
            breadcrumb_items.append(li()[separator_element])

    return ol(**attrs)[*breadcrumb_items]
