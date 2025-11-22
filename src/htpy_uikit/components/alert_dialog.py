from typing import Literal
from typing import Optional
from typing import TypedDict

from htpy import Node
from htpy import Renderable
from htpy import article
from htpy import dialog as dialog_tag
from htpy import div
from htpy import h2
from htpy import header
from htpy import p
from htpy import section
from htpy import with_children

from ._types import ButtonVariant
from ._utils import random_string
from .button import button_component

# Type definitions for alert dialog component
AlertDialogActionVariant = Literal["default", "destructive"]


class AlertDialogTriggerAttrs(TypedDict):
    """Attributes applied to buttons that toggle the native dialog."""

    type: Literal["button"]
    onclick: str


@with_children
def alert_dialog(
    children: Node,
    *,
    title: str,
    description: Optional[str] = None,
    cancel_text: str = "Cancel",
    action_text: str = "Continue",
    action_variant: AlertDialogActionVariant = "default",
    show_cancel: bool = True,
    **attrs,
) -> Renderable:
    """Render a self-contained alert dialog element.

    The function renders a native `<dialog>` with an inner `<article>` that
    contains a header, optional body content, and a footer with action
    buttons. Triggers for opening/closing the dialog are intentionally kept
    separate; use `attrs_btn_open_alert_dialog(dialog_id)` and
    `attrs_btn_close_alert_dialog(dialog_id)` to build trigger/close button
    attributes (they call `showModal()` / `close()` respectively).

    Args:
        children: Dialog content (body) or nodes to render inside the dialog
        title: Dialog title
        description: Optional dialog description text
        cancel_text: Text for the cancel button (default: "Cancel")
        action_text: Text for the primary action button (default: "Continue")
        action_variant: Action button styling; one of "default" or "destructive"
        show_cancel: Whether to render a cancel button next to the action
        **attrs: Additional HTML attributes applied to the dialog container

    Returns:
        htpy.div: A wrapper containing the native `<dialog>` node. Triggers
        should be rendered separately using the helper functions provided.
    """

    # Action button variant classes (kept for reference if needed later)

    # Map retained for backwards compatibility; not used in the inline version

    # Create an id for the dialog so trigger buttons can reference it.
    # Keep dialog_id available for external hooks if needed
    dialog_id = attrs.get("id") or f"alert-dialog-{abs(hash(title))}"
    # expose id on attrs too so external code can reference it
    attrs["id"] = dialog_id

    # Note: trigger handling removed from this function to keep dialog
    # rendering separate. Use attrs_btn_open_alert_dialog(dialog_id) to
    # create external trigger buttons.

    # Build the native <dialog> with Basecoat-like classes applied inline
    dialog_attrs = {
        "id": dialog_id,
        "aria-labelledby": "alert-dialog-title",
        "aria-describedby": "alert-dialog-description",
    }

    # Inner article adopts sizing and layout; use card background and theme tokens
    article_classes = (
        "bg-card text-card-foreground fixed top-[50%] left-[50%] z-50 flex flex-col w-full "
        "max-w-lg -translate-x-1/2 -translate-y-1/2 gap-4 rounded-lg border border-border p-6 shadow-lg "
        "max-h-[calc(100%-2rem)] transition-all scale-95"
    )

    dialog_header = header(class_="flex flex-col gap-2 text-center sm:text-left")[
        h2(
            class_="text-lg font-semibold text-card-foreground",
            **{"id": "alert-dialog-title"},
        )[title],
        p(class_="text-sm text-muted-foreground", **{"id": "alert-dialog-description"})[
            description or ""
        ],
    ]

    # Body uses standard padding so content aligns with header/footer
    body_section = section(class_="flex-1 px-0")[children] if children else None

    # Footer with actions
    footer_children = []
    if show_cancel:
        footer_children.append(
            # use project button component for consistent styling
            button_component(
                variant="outline",
                **attrs_btn_close_alert_dialog(dialog_id),
            )[cancel_text]
        )

    footer_children.append(
        button_component(
            variant="destructive" if action_variant == "destructive" else "primary",
            **attrs_btn_close_alert_dialog(dialog_id),
        )[action_text]
    )

    dialog_footer = div(
        class_="flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2 pt-4"
    )[*footer_children]

    dialog_node = dialog_tag(**dialog_attrs)[
        # Inline overlay since we don't rely on external .dialog ::backdrop
        div(class_="fixed inset-0 bg-black/50"),
        article(class_=article_classes)[
            dialog_header,
            body_section,
            dialog_footer,
        ],
    ]

    # Return the dialog node only; triggers are separate and should use the
    # attrs_btn_open_alert_dialog helper to open the dialog.
    return div()[dialog_node]


def attrs_btn_open_alert_dialog(dialog_id: str) -> AlertDialogTriggerAttrs:
    """Return attributes for a button to open a native alert dialog.

    Args:
        dialog_id: The id of the <dialog> to open.

    Returns:
        dict: Attributes including an onclick handler calling showModal().
    """
    return {
        "type": "button",
        "onclick": f"document.getElementById('{dialog_id}').showModal()",
    }


def attrs_btn_close_alert_dialog(dialog_id: str) -> AlertDialogTriggerAttrs:
    """Return attributes for a button to close a native alert dialog.

    Args:
        dialog_id: The id of the <dialog> to close.

    Returns:
        dict: Attributes including an onclick handler calling close().
    """
    return {
        "type": "button",
        "onclick": f"document.getElementById('{dialog_id}').close()",
    }


# Convenience function for destructive actions
def alert_dialog_destructive(
    children: Node,
    *,
    title: str,
    description: Optional[str] = None,
    with_trigger: bool = False,
    trigger_label: str = "Open dialog",
    trigger_attrs: dict | None = None,
    trigger_btn_variant: ButtonVariant = "outline",
    **kwargs,
) -> Node:
    """Render a destructive alert dialog and optional trigger button.

    Args:
        children: Dialog body content.
        title: Dialog title.
        description: Optional description text.
        with_trigger: Whether to render an accompanying trigger button.
        trigger_label: Label for the trigger button.
        trigger_attrs: Extra attributes applied to the trigger button.
        trigger_btn_variant: Variant passed to ``button_component`` for the trigger.
        **kwargs: Additional keyword arguments forwarded to ``alert_dialog``.

    Returns:
        Node: Dialog renderable, optionally paired with a trigger button.
    """
    # ensure an id is present so trigger can open the dialog
    dialog_id = kwargs.get("id") or f"alert-dialog-{random_string(6)}"
    kwargs["id"] = dialog_id

    dialog_node = alert_dialog(
        title=title,
        description=description,
        action_variant="destructive",
        **kwargs,
    )[children]

    if not with_trigger:
        return dialog_node

    trigger_button = button_component(
        variant=trigger_btn_variant,
        **(trigger_attrs or {}),
        **attrs_btn_open_alert_dialog(dialog_id),
    )[trigger_label]
    return [dialog_node, trigger_button]


# Convenience function for confirmation dialogs
def confirm_dialog(
    message: str,
    *,
    title: str = "Are you sure?",
    confirm_text: str = "Yes",
    cancel_text: str = "No",
    with_trigger: bool = True,
    trigger_label: str = "Open dialog",
    trigger_attrs: dict | None = None,
    trigger_btn_variant: ButtonVariant = "outline",
    **kwargs,
) -> Node:
    """Render a confirmation dialog with optional trigger button.

    Args:
        message: Dialog body text.
        title: Dialog title.
        confirm_text: Label for the confirm action button.
        cancel_text: Label for the cancel button.
        with_trigger: Whether to render an accompanying trigger button.
        trigger_label: Label for the trigger button.
        trigger_attrs: Extra attributes applied to the trigger button.
        trigger_btn_variant: Button variant for the trigger.
        **kwargs: Additional keyword arguments forwarded to ``alert_dialog``.

    Returns:
        Node: Dialog renderable (and trigger button when requested).
    """
    dialog_id = kwargs.get("id") or f"alert-dialog-{random_string(6)}"
    kwargs["id"] = dialog_id

    dialog_node = alert_dialog(
        title=title, action_text=confirm_text, cancel_text=cancel_text, **kwargs
    )[message]

    if not with_trigger:
        return dialog_node

    trigger_button = button_component(
        variant=trigger_btn_variant,
        **(trigger_attrs or {}),
        **attrs_btn_open_alert_dialog(dialog_id),
    )[trigger_label]
    return [dialog_node, trigger_button]
