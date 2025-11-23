from htpy import Node, div, h5

from htpy_uikit.components.skeleton import (
    skeleton_avatar,
    skeleton_button,
    skeleton_card,
    skeleton_media_row,
    skeleton_table,
    skeleton_text,
    skeleton_title,
)

from ._utils import _demo_section


def skeleton_section() -> Node:
    return _demo_section(
        "Skeleton",
        "Loading state placeholders",
        [
            div(class_="space-y-6")[
                # Individual skeleton components
                div[
                    h5(class_="text-xs font-medium text-muted-foreground mb-2")[
                        "Basic Skeletons"
                    ],
                    div(class_="space-y-2")[
                        skeleton_text(),
                        skeleton_text(width="w-3/4"),
                        skeleton_text(width="w-1/2"),
                        skeleton_title(),
                        skeleton_button(),
                        skeleton_avatar(),
                    ],
                ],
                # Media row example
                div[
                    h5(class_="text-xs font-medium text-muted-foreground mb-2")[
                        "Media rows"
                    ],
                    div(class_="space-y-2")[
                        skeleton_media_row(),
                        skeleton_media_row(),
                    ],
                ],
                # Complex skeletons
                div[
                    h5(class_="text-xs font-medium text-muted-foreground mb-2")[
                        "Complex Skeletons"
                    ],
                    div(class_="flex max-sm:flex-col gap-4 w-full")[
                        skeleton_card(),
                        skeleton_card(),
                    ],
                    div(class_="mt-4")[skeleton_table(rows=3, columns=3)],
                ],
            ]
        ],
    )
