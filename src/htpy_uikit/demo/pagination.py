from htpy import Node

from htpy_uikit.components.pagination import pagination

from ._utils import _demo_section


def pagination_section() -> Node:
    return _demo_section(
        "Pagination",
        "Navigation for multi-page content",
        [
            pagination(current_page=1, total_pages=20, show_pages=5, size="md"),
            pagination(current_page=5, total_pages=20, show_pages=5, size="sm"),
            pagination(current_page=20, total_pages=20, show_pages=5, size="lg"),
        ],
    )
