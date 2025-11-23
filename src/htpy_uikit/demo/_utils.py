from htpy import Node, div, h2, p, span


def _demo_section(title: str, description: str | None = None, content: list[Node] = []) -> Node:
    """Helper function to create demo sections."""
    # Render a compact section with a header bar and tighter content area so the
    # demo matches the reference layout more closely.
    return div(class_="rounded-lg shadow-sm border border-border overflow-visible")[
        # header bar
        div(class_="px-4 py-3 border-b border-border flex items-center justify-between")[
            h2(class_="font-semibold text-card-foreground")[title],
            span(class_="text-muted-foreground text-sm"),
        ],
        # content area
        div(class_="p-6")[
            (p(class_="text-sm text-muted-foreground mb-4")[description] if description else None),
            div[*content],
        ],
    ]
