from typing import Literal

from htpy import Renderable
from htpy import a
from htpy import div
from htpy import li
from htpy import nav
from htpy import span
from htpy import template
from htpy import ul

from ._utils import merge_classes
from .icons import icon_chevron_left
from .icons import icon_chevron_right
from .icons import icon_more

# Shared Basecoat class presets (used by both backend and Alpine variants)
base_classes_btn = (
    "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium "
    "disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:shrink-0 shrink-0 "
    "outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] "
    "aria-invalid:ring-destructive/20 aria-invalid:border-destructive "
    "cursor-pointer rounded-md"
)
variant_ghost = "hover:bg-accent hover:text-accent-foreground"
variant_outline = (
    "border bg-background shadow-xs border-input hover:bg-accent hover:text-accent-foreground"
)
size_text = {
    "sm": "gap-1.5 h-8 px-3 has-[>svg]:px-2.5 text-xs",
    "md": "gap-2 h-9 px-4 py-2 has-[>svg]:px-3 text-sm",
    "lg": "gap-2 h-10 px-6 has-[>svg]:px-4 text-base",
}
size_icon = {"sm": "size-8", "md": "size-9", "lg": "size-10"}


def classes_btn(variant: str, *, icon: bool, size_key: str) -> str:
    """Return Tailwind utility classes for pagination controls.

    Args:
        variant: Either ``\"outline\"`` or ``\"ghost\"``.
        icon: Whether the control is icon-sized (square) vs text width.
        size_key: Size token (``\"sm\"``, ``\"md\"``, or ``\"lg\"``).

    Returns:
        str: Space-separated CSS class string.
    """
    variant_classes = variant_outline if variant == "outline" else variant_ghost
    return f"{base_classes_btn} {variant_classes} {(size_icon if icon else size_text)[size_key]}".strip()


def pagination(
    *,
    current_page: int = 1,
    total_pages: int = 1,
    show_pages: int = 5,
    base_url: str = "",
    url_param: str = "page",
    show_first_last: bool = True,
    show_prev_next: bool = True,
    size: Literal["sm", "md", "lg"] = "md",
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style pagination bar with optional prev/next controls.

    Args:
        current_page: Currently active page number.
        total_pages: Total number of pages available.
        show_pages: Number of numbered page buttons to display.
        base_url: Base URL used when building page links.
        url_param: Query parameter used for the page number.
        show_first_last: Whether to show first/last buttons.
        show_prev_next: Whether to show previous/next buttons.
        size: Button size token (``\"sm\"``, ``\"md\"``, ``\"lg\"``).
        class_: Extra classes appended to the outer nav.
        **attrs: Additional HTML attributes forwarded to the nav.

    Returns:
        Renderable: Pagination ``<nav>`` element.
    """

    # Base classes - following basecoat pagination styling
    base_classes = "mx-auto flex w-full justify-center"

    # Add custom classes
    attrs["class_"] = merge_classes(base_classes, class_)

    # Helper function to build page URL
    def build_url(page: int) -> str:
        if page == current_page:
            return "#"
        if page < 1 or page > total_pages:
            return "#"
        return f"{base_url}?{url_param}={page}"

    # Calculate page range to show
    half_show = show_pages // 2
    start_page = max(1, current_page - half_show)
    end_page = min(total_pages, start_page + show_pages - 1)

    # Adjust start if we're near the end
    if end_page - start_page + 1 < show_pages:
        start_page = max(1, end_page - show_pages + 1)

    # Build pagination items
    items = []

    # Previous button (ghost style with chevron + label)
    if show_prev_next:
        prev_url = build_url(current_page - 1) if current_page > 1 else "#"
        is_disabled = current_page <= 1

        prev_classes = classes_btn("ghost", icon=False, size_key=size)
        if is_disabled:
            prev_classes += " opacity-50 cursor-not-allowed"

        items.append(
            li()[
                a(
                    class_=prev_classes,
                    href=prev_url if not is_disabled else None,
                    **{
                        "aria-label": "Previous page",
                        "hx-boost": "true",
                        "hx-push-url": "true",
                    },
                )[
                    icon_chevron_left(class_="size-4 shrink-0"),
                    span()[" Previous"],
                ]
            ]
        )

    # First page button (if needed)
    if show_first_last and start_page > 1:
        items.append(
            li()[
                a(
                    class_=classes_btn("ghost", icon=True, size_key=size),
                    href=build_url(1),
                    **{
                        "hx-boost": "true",
                        "hx-push-url": "true",
                    },
                )["1"]
            ]
        )
        if start_page > 2:
            ellipsis_class = f"{size_icon[size]} flex items-center justify-center"
            items.append(li()[div(class_=ellipsis_class)[icon_more(class_="size-4 shrink-0")]])

    # Page number buttons
    for page in range(start_page, end_page + 1):
        is_current = page == current_page
        if is_current:
            page_classes = classes_btn("outline", icon=True, size_key=size)
        else:
            page_classes = classes_btn("ghost", icon=True, size_key=size)

        items.append(
            li()[
                a(
                    class_=page_classes,
                    href="#" if is_current else build_url(page),
                    **{
                        "aria-current": "page" if is_current else None,
                        "hx-boost": "true",
                        "hx-push-url": "true",
                    },
                )[str(page)]
            ]
        )

    # Last page button (if needed)
    if show_first_last and end_page < total_pages:
        if end_page < total_pages - 1:
            ellipsis_class = f"{size_icon[size]} flex items-center justify-center"
            items.append(li()[div(class_=ellipsis_class)[icon_more(class_="size-4 shrink-0")]])
        items.append(
            li()[
                a(
                    class_=classes_btn("ghost", icon=True, size_key=size),
                    href=build_url(total_pages),
                    **{
                        "hx-boost": "true",
                        "hx-push-url": "true",
                    },
                )[str(total_pages)]
            ]
        )

    # Next button
    if show_prev_next:
        next_url = build_url(current_page + 1) if current_page < total_pages else "#"
        is_disabled = current_page >= total_pages

        next_classes = classes_btn("ghost", icon=False, size_key=size)
        if is_disabled:
            next_classes += " opacity-50 cursor-not-allowed"

        items.append(
            li()[
                a(
                    class_=next_classes,
                    href=next_url if not is_disabled else None,
                    **{
                        "aria-label": "Next page",
                        "hx-boost": "true",
                        "hx-push-url": "true",
                    },
                )[
                    span()["Next "],
                    icon_chevron_right(class_="size-4 shrink-0"),
                ]
            ]
        )

    return nav(**{"role": "navigation", "aria-label": "pagination"}, **attrs)[
        ul(class_="flex flex-row items-center gap-1")[*items]
    ]


# Convenience functions - following basecoat implementation
def simple_pagination(**kwargs) -> Renderable:
    """Simple pagination without first/last buttons."""
    return pagination(show_first_last=False, **kwargs)


def compact_pagination(**kwargs) -> Renderable:
    """Compact pagination showing fewer page numbers."""
    return pagination(show_pages=3, show_first_last=False, **kwargs)


def large_pagination(**kwargs) -> Renderable:
    """Large pagination buttons."""
    return pagination(size="lg", **kwargs)


def alpine_pagination(
    *,
    class_: str | None = None,
    x_show: str | None = "hasMultiplePages()",
    size: Literal["sm", "md", "lg"] = "md",
    **attrs,
) -> Renderable:
    """
    Alpine.js-friendly pagination component.

    Expects these properties/methods to exist in the surrounding Alpine data:
    - currentPage, totalPages
    - getPageNumbers() -> array of pages and '...'
    - goToPage(page), prevPage(), nextPage()
    - prevDisabled(), nextDisabled()
    - prevButtonClass(), nextButtonClass(), pageButtonClass(page)

    Args:
        class_: Optional additional classes for the wrapper div.
        x_show: Alpine expression to control visibility (defaults to hasMultiplePages()).
        **attrs: Additional HTML attributes for the wrapper div.

    Returns:
        htpy.div: Wrapper containing the pagination nav/ul.
    """

    # Wrapper classes: keep inline layout so it fits right-aligned container
    base_wrapper = "inline-flex"
    attrs["class_"] = merge_classes(base_wrapper, class_)
    if x_show:
        attrs["x-show"] = x_show
        attrs["x-cloak"] = ""

    # Build class presets to exactly mirror backend pagination visuals
    prev_next_base = classes_btn("ghost", icon=False, size_key=size)
    prev_next_disabled = f"{prev_next_base} opacity-50 cursor-not-allowed pointer-events-none"
    page_current = classes_btn("outline", icon=True, size_key=size)
    page_other = classes_btn("ghost", icon=True, size_key=size)
    ellipsis_class = f"{ {'sm': 'size-8', 'md': 'size-9', 'lg': 'size-10'}[size] } flex items-center justify-center"

    return div(**attrs)[
        nav(aria_label="Page navigation")[
            ul(class_="flex flex-row items-center gap-1")[
                # Previous
                li[
                    a(
                        href="#",
                        **{"@click.prevent": "!prevDisabled() && (prevPage(), $el.blur())"},
                        **{
                            ":class": f"prevDisabled() ? '{prev_next_disabled}' : '{prev_next_base}'"
                        },
                        **{":aria-disabled": "prevDisabled()"},
                        **{":tabindex": "prevDisabled() ? -1 : 0"},
                        **{"aria-label": "Previous page"},
                    )[
                        icon_chevron_left(class_="size-4 shrink-0"),
                        span()[" Previous"],
                    ]
                ],
                # Page numbers and ellipsis
                template(x_for="(page, index) in getPageNumbers()", key="index")[
                    li[
                        template(x_if="page === '...'")[
                            div(class_=ellipsis_class)[icon_more(class_="size-4 shrink-0")]
                        ],
                        template(x_if="page !== '...'")[
                            a(
                                href="#",
                                **{"@click.prevent": "goToPage(page); $el.blur()"},
                                **{
                                    ":class": f"currentPage === page ? '{page_current}' : '{page_other}'"
                                },
                                **{":aria-current": "currentPage === page ? 'page' : null"},
                            )[span(x_text="page")]
                        ],
                    ]
                ],
                # Next
                li[
                    a(
                        href="#",
                        **{"@click.prevent": "!nextDisabled() && (nextPage(), $el.blur())"},
                        **{
                            ":class": f"nextDisabled() ? '{prev_next_disabled}' : '{prev_next_base}'"
                        },
                        **{":aria-disabled": "nextDisabled()"},
                        **{":tabindex": "nextDisabled() ? -1 : 0"},
                        **{"aria-label": "Next page"},
                    )[
                        span()["Next "],
                        icon_chevron_right(class_="size-4 shrink-0"),
                    ]
                ],
            ]
        ]
    ]
