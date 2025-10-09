"""
Centralized type definitions for all component library types.

This module contains all Literal types and TypedDict classes used throughout
the component library to ensure consistency and maintainability.
"""

from typing import Literal
from typing import NotRequired
from typing import TypedDict

from htpy import Node
from htpy import Renderable

# =============================================================================
# POSITIONING AND ALIGNMENT TYPES
# =============================================================================

TSide = Literal["top", "bottom", "left", "right"]
"""Positioning side for tooltips, popovers, etc."""

TAlign = Literal["start", "center", "end"]
"""Alignment for positioned elements."""

# =============================================================================
# COMPONENT VARIANT TYPES
# =============================================================================

# Button component types
ButtonVariant = Literal["primary", "secondary", "destructive", "outline", "ghost", "link", "danger"]
"""Button style variants."""

ButtonSize = Literal["sm", "md", "lg"]
"""Button size variants."""

ButtonType = Literal["button", "submit", "reset"]
"""HTML button type attribute values."""

# Badge component types
BadgeVariant = Literal["primary", "secondary", "destructive", "outline"]
"""Badge style variants."""

BadgeStatus = Literal[
    "active", "inactive", "pending", "error", "success", "failed", "processing", "completed"
]
"""Badge status variants for different states."""

# Alert component types
AlertVariant = Literal["default", "destructive", "success", "info", "warning"]
"""Alert style variants."""

# Toast component types
TCategory = Literal["success", "info", "warning", "error"]
"""Toast category variants."""

# Switch component types
TColor = Literal["primary", "blue", "green", "red"]
"""Switch color variants."""

BreadcrumbSeparator = Literal["chevron", "slash", "arrow"]
"""Breadcrumb separator variants."""

# =============================================================================
# INPUT AND FORM TYPES
# =============================================================================

# Input component types
InputType = Literal[
    "text",
    "email",
    "password",
    "number",
    "tel",
    "url",
    "search",
    "date",
    "datetime-local",
    "time",
    "file",
]
"""HTML input type attribute values."""

# Form component types
FormMethod = Literal["get", "post"]
"""HTTP form method values."""

FormAlign = Literal["left", "center", "right"]
"""Form alignment options."""

# =============================================================================
# STRUCTURED DATA TYPES
# =============================================================================


class SelectOption(TypedDict):
    """Option structure for select and combobox components."""

    value: str
    label: str


class RadioOption(TypedDict):
    """Option structure for radio group components."""

    value: str
    label: str


class RadioCardOption(TypedDict):
    """Option structure for radio group cards with descriptions."""

    value: str
    title: str
    description: str | None


# Radio group component types
RadioDirection = Literal["vertical", "horizontal"]
"""Radio group layout direction."""

RadioCardColor = Literal["blue", "green", "red"]
"""Radio card color variants."""

# Avatar component types
AvatarSize = Literal["xs", "sm", "md", "lg", "xl"]
"""Avatar size variants."""


class AvatarImage(TypedDict):
    """Avatar image structure."""

    src: str
    alt: str


class AccordionItem(TypedDict):
    """Option structure for accordion items."""

    title: str
    content: Node | str
    expanded: NotRequired[bool]


class BreadcrumbItem(TypedDict):
    """Option structure for breadcrumb items."""

    label: str
    url: str | None


class TabContentItem(TypedDict):
    """Tab item structure for tabs component."""

    value: str
    label: str | Node
    content: Node
    disabled: NotRequired[bool]


class SelectItem(TypedDict, total=False):
    """Selectable item for the popover Select component."""

    type: Literal["item"]
    value: str
    label: str
    icon: Renderable


class SelectGroup(TypedDict):
    """Group/section of items with a heading label."""

    type: Literal["group"]
    label: str
    items: list[SelectItem]


# Select component orientation types
SelectOrientation = Literal["vertical", "horizontal"]


# =============================================================================
# UTILITY TYPES
# =============================================================================

# Common HTML attributes that components might accept
HTMLClass = str | None
"""HTML class attribute type."""

HTMLEventHandler = str | None
"""HTML event handler attribute type (like onclick, onchange, etc.)."""

# Common component props
ComponentVariant = str
"""Generic variant type for components."""

ComponentSize = Literal["xs", "sm", "md", "lg", "xl"]
"""Generic size type for components."""

# =============================================================================
# EXPORT ALL TYPES
# =============================================================================

__all__ = [
    # Positioning
    "TSide",
    "TAlign",
    # Button types
    "ButtonVariant",
    "ButtonSize",
    "ButtonType",
    # Badge types
    "BadgeVariant",
    "BadgeStatus",
    # Alert types
    "AlertVariant",
    # Toast types
    "TCategory",
    # Switch types
    "TColor",
    # Input types
    "InputType",
    # Form types
    "FormMethod",
    "FormAlign",
    # Data structures
    "SelectOption",
    "RadioOption",
    "RadioCardOption",
    "RadioDirection",
    "RadioCardColor",
    "AvatarSize",
    "AvatarImage",
    "TabContentItem",
    "SelectItem",
    "SelectGroup",
    "SelectOrientation",
    # Utility types
    "HTMLClass",
    "HTMLEventHandler",
    "ComponentVariant",
    "ComponentSize",
]
