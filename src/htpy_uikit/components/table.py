from htpy import Node
from htpy import Renderable
from htpy import div
from htpy import table
from htpy import tbody
from htpy import td
from htpy import th
from htpy import thead
from htpy import tr

from ._utils import merge_classes


def table_component(
    *,
    headers: list[str],
    rows: list[list[Node]],
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style table component.

    Based on Basecoat UI table implementation.
    Uses standard HTML table elements with table class.

    Args:
        headers: List of header texts
        rows: List of rows, each containing list of cell contents
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.table: Table component
    """

    # Base classes - using Tailwind equivalent of Basecoat table
    base_classes = (
        "w-full caption-bottom text-sm border-border "
        # Header border color
        "[&_thead_tr]:border-b [&_thead_tr]:border-border/70 "
        # Body row borders: subtle but visible
        "[&_tbody_tr]:border-border/60 [&_tr]:border-b [&_tr]:transition-colors "
        "[&_tr]:hover:bg-muted/50 "
        # Footer styling and border color
        "[&_tfoot]:bg-muted/50 [&_tfoot]:border-t [&_tfoot]:border-border/70 [&_tfoot]:font-medium "
        "[&_tfoot_tr]:last:border-b-0 "
        # Cell and header text/layout
        "[&_th]:text-foreground [&_th]:h-10 [&_th]:px-2 [&_th]:text-left [&_th]:align-middle "
        "[&_th]:font-medium [&_th]:whitespace-nowrap [&_th:has([role=checkbox])]:pr-0 "
        "[&_th_[role=checkbox]]:translate-y-[2px] [&_td]:p-2 [&_td]:align-middle "
        "[&_td]:whitespace-nowrap [&_td:has([role=checkbox])]:pr-0 "
        "[&_td_[role=checkbox]]:translate-y-[2px] [&_caption]:text-muted-foreground "
        "[&_caption]:mt-4 [&_caption]:text-sm"
    )

    # Add custom classes
    attrs["class_"] = merge_classes(base_classes, class_)

    # Build table header
    header_cells = [th(scope="col")[header] for header in headers]

    # Build table body
    table_rows = []
    for row in rows:
        row_cells = [td[cell] for cell in row]
        table_rows.append(tr[row_cells])

    return div(class_="overflow-x-auto")[
        table(**attrs)[
            thead[tr[header_cells]],
            tbody[*table_rows],
        ]
    ]


# Convenience functions for common table patterns - following basecoat implementation
def simple_table(data: list[dict], columns: list[str], **kwargs) -> Renderable:
    """
    Simple table from dictionary data.

    Args:
        data: List of dictionaries containing row data
        columns: List of column keys to display
        **kwargs: Additional arguments for table_component
    """

    # Extract headers from columns
    headers = columns

    # Build rows from data
    rows = []
    for item in data:
        row = []
        for column in columns:
            value = item.get(column, "")
            if isinstance(value, (int, float)):
                row.append(str(value))
            elif isinstance(value, bool):
                row.append("Yes" if value else "No")
            else:
                row.append(str(value) if value else "")
        rows.append(row)

    return table_component(headers=headers, rows=rows, **kwargs)


def table_with_actions(
    *,
    headers: list[str],
    rows: list[list[Node]],
    actions: list[Node] | None = None,
    **kwargs,
) -> Renderable:
    """Table with actions column."""
    if actions:
        headers = headers + ["Actions"]
        rows = [row + [actions[i] if i < len(actions) else []] for i, row in enumerate(rows)]

    return table_component(headers=headers, rows=rows, **kwargs)
