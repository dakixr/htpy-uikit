from htpy import Node, div

from htpy_uikit.components.breadcrumb import breadcrumb

from ._utils import _demo_section


def breadcrumb_section() -> Node:
    return _demo_section(
        "Breadcrumb",
        "Navigation hierarchy indicators",
        [
            div(class_="space-y-4")[
                # Simple breadcrumb
                breadcrumb(
                    [
                        {"label": "Home", "url": "/"},
                        {"label": "Components", "url": "/components"},
                        {"label": "Breadcrumb", "url": None},
                    ]
                ),
                # Long breadcrumb that collapses the middle items into an overflow menu
                breadcrumb(
                    [
                        {"label": "Home", "url": "/"},
                        {"label": "Projects", "url": "/projects"},
                        {"label": "2024", "url": "/projects/2024"},
                        {"label": "July", "url": "/projects/2024/July"},
                        {
                            "label": "Design",
                            "url": "/projects/2024/July/design",
                        },
                        {"label": "Components", "url": "/components"},
                        {"label": "Breadcrumb", "url": None},
                    ],
                    collapse=True,
                    max_visible=4,
                ),
                # Explicitly disabled collapsing
                breadcrumb(
                    [
                        {"label": "Home", "url": "/"},
                        {"label": "Components", "url": "/components"},
                        {"label": "Breadcrumb", "url": None},
                    ],
                    collapse=False,
                ),
            ]
        ],
    )
