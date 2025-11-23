from htpy import Node

from htpy_uikit.components.badge import badge_status
from htpy_uikit.components.table import table_component

from ._utils import _demo_section


def table_section() -> Node:
    return _demo_section(
        "Table",
        "Data display in tabular format",
        [
            table_component(
                headers=["Name", "Email", "Status", "Role"],
                rows=[
                    [
                        "John Doe",
                        "john@example.com",
                        badge_status("active"),
                        "Admin",
                    ],
                    [
                        "Jane Smith",
                        "jane@example.com",
                        badge_status("pending"),
                        "User",
                    ],
                    [
                        "Bob Johnson",
                        "bob@example.com",
                        badge_status("inactive"),
                        "User",
                    ],
                ],
            )
        ],
    )
