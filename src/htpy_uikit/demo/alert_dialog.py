from htpy import Node, div, p

from htpy_uikit.components.alert_dialog import (
    alert_dialog,
    alert_dialog_destructive,
    attrs_btn_open_alert_dialog,
    confirm_dialog,
)
from htpy_uikit.components.button import button_component

from ._utils import _demo_section


def alert_dialog_section() -> Node:
    return _demo_section(
        "Alert Dialog",
        "Modal dialogs for important actions",
        [
            div(class_="flex flex-col gap-4")[
                # Use convenience helpers that optionally render triggers
                alert_dialog_destructive(
                    p["This is a modal dialog with custom content."],
                    title="Are you sure?",
                    description=(
                        "This action cannot be undone. This will permanently delete your "
                        "account and remove your data from our servers."
                    ),
                    with_trigger=True,
                    trigger_label="Open dialog",
                ),
                confirm_dialog(
                    "Are you sure?",
                    title="Confirm",
                    with_trigger=True,
                    trigger_label="Open confirm",
                ),
                # Manual pattern: render dialog and a separate trigger without helpers
                alert_dialog(
                    id="manual-alert-dialog",
                    title="Manual dialog",
                    description=(
                        "This dialog is opened by a button that uses **attrs_btn_open_alert_dialog**"
                    ),
                    action_text="OK",
                    cancel_text="Cancel",
                )[div[p["Manual content inside the dialog."]]],
                button_component(
                    variant="outline",
                    **attrs_btn_open_alert_dialog("manual-alert-dialog"),
                )["Open manual dialog"],
            ]
        ],
    )
