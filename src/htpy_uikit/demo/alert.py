from htpy import Node, div

from htpy_uikit.components.alert import alert
from htpy_uikit.components.icons import icon_download

from ._utils import _demo_section


def alert_section() -> Node:
    return _demo_section(
        "Alert",
        "Informational messages and notifications",
        [
            div(class_="space-y-4")[
                alert(
                    title="Success! Your changes have been saved",
                    description="This is an alert with icon, title and description.",
                    variant="success",
                ),
                alert(
                    title="Custom icon example",
                    description="This alert injects a custom icon (download).",
                    icon=icon_download(class_="w-5 h-5 shrink-0 mt-0.5"),
                    variant="success",
                ),
                alert(
                    title="This is an alert with icon, description and no title.",
                    description=None,
                    variant="info",
                ),
                alert(
                    title=(
                        "This is a very long alert title that demonstrates how the component "
                        "handles extended text content and potentially wraps across multiple lines"
                    ),
                    variant="info",
                    show_icon=False,
                ),
                alert(
                    title="Success! Your changes have been saved",
                    description="This is an alert with icon, title and description.",
                    variant="default",
                    show_icon=False,
                ),
                alert(
                    title="Warning: Check this out",
                    description="This one uses a warning variant.",
                    variant="warning",
                ),
                alert(
                    title="Destructive: Action failed",
                    description="Please verify the operation and retry.",
                    variant="destructive",
                ),
            ]
        ],
    )
