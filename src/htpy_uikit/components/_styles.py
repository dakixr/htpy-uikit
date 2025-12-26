"""Shared Tailwind class constants for consistent styling across components.

This module provides semantic style tokens that components can import and use,
ensuring visual consistency and making it easier to maintain color/border/state
patterns across the entire component library.

All classes use shadcn-compatible theme tokens (e.g., bg-primary, text-foreground,
border-border) that map to CSS variables defined in tailwind-themes/theme.css.
"""

# ============================================================================
# Common state patterns
# ============================================================================

# Focus ring pattern used across interactive components
FOCUS_RING_CLASSES = (
    "focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] outline-none"
)

# Invalid/error state pattern
ARIA_INVALID_CLASSES = (
    "aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 "
    "aria-invalid:border-destructive"
)

# Disabled state pattern
DISABLED_STATE_CLASSES = "disabled:cursor-not-allowed disabled:opacity-50"

# Composite: All interactive state patterns combined (focus, invalid, disabled)
INTERACTIVE_STATE_CLASSES = f"{FOCUS_RING_CLASSES} {ARIA_INVALID_CLASSES} {DISABLED_STATE_CLASSES}"

# Hover accent pattern (used for interactive elements like buttons, menu items)
HOVER_ACCENT_CLASSES = "hover:bg-accent hover:text-accent-foreground"

# Focus accent pattern (for keyboard navigation)
FOCUS_ACCENT_CLASSES = "focus-visible:bg-accent focus-visible:text-accent-foreground"

# Icon inline styling patterns
ICON_INLINE_CLASSES = (
    "[&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0"
)
ICON_INLINE_SMALL_CLASSES = "[&>svg]:size-3 [&>svg]:pointer-events-none"

# ============================================================================
# Button styles
# ============================================================================

# Base button classes (shared across all variants)
BTN_BASE_CLASSES = (
    "inline-flex items-center justify-center whitespace-nowrap text-sm font-medium "
    "transition-all disabled:pointer-events-none disabled:opacity-50 "
    f"{ICON_INLINE_CLASSES} shrink-0 cursor-pointer rounded-md "
    f"{INTERACTIVE_STATE_CLASSES}"
)

# Button size classes
BTN_SIZE_MD_CLASSES = "gap-2 h-9 px-4 has-[>svg]:px-3"
BTN_SIZE_SM_CLASSES = "gap-1.5 h-8 px-3 text-xs has-[>svg]:px-2.5"
BTN_SIZE_LG_CLASSES = "gap-2 h-10 px-6 has-[>svg]:px-4"

# Button icon-only sizes
BTN_ICON_MD_CLASSES = "p-0 size-9 min-w-9"
BTN_ICON_SM_CLASSES = "p-0 size-8 min-w-8"
BTN_ICON_LG_CLASSES = "p-0 size-10 min-w-10"

# Button variant classes
BTN_VARIANT_PRIMARY_CLASSES = "bg-primary text-primary-foreground shadow-xs hover:bg-primary/90"

BTN_VARIANT_SECONDARY_CLASSES = (
    "bg-secondary text-secondary-foreground shadow-xs hover:bg-secondary/80"
)

BTN_VARIANT_DESTRUCTIVE_CLASSES = (
    "bg-destructive text-white shadow-xs "
    "focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 "
    "dark:bg-destructive/60 hover:bg-destructive/90 dark:hover:bg-destructive/50"
)

BTN_VARIANT_OUTLINE_CLASSES = (
    "border bg-input/40 shadow-xs dark:bg-input/30 dark:border-input "
    "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50"
)

BTN_VARIANT_GHOST_CLASSES = "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50"

BTN_VARIANT_LINK_CLASSES = "text-primary underline-offset-4 hover:underline"

# ============================================================================
# Field/Input styles
# ============================================================================

# Base field trigger (for select, combobox triggers - uses button outline variant)
FIELD_TRIGGER_BASE_CLASSES = (
    "border bg-input/40 shadow-xs dark:bg-input/30 dark:border-input "
    "hover:bg-accent hover:text-accent-foreground dark:hover:bg-accent/50 "
    f"{INTERACTIVE_STATE_CLASSES}"
)

# Native input/select base classes
INPUT_BASE_CLASSES = (
    "appearance-none file:text-foreground placeholder:text-muted-foreground "
    "selection:bg-primary selection:text-primary-foreground "
    "dark:bg-input/30 border-input flex h-9 w-full min-w-0 rounded-md border "
    "bg-input/40 px-3 py-1 text-base shadow-xs transition-[color,box-shadow] "
    f"{INTERACTIVE_STATE_CLASSES} md:text-sm "
    "file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium"
)

# Native select specific (includes chevron icon background)
SELECT_NATIVE_BASE_CLASSES = (
    "appearance-none border-input dark:bg-input/30 dark:hover:bg-input/50 "
    "flex w-fit items-center justify-between gap-2 rounded-md border bg-input/40 "
    "pl-3 pr-9 py-2 text-sm whitespace-nowrap shadow-xs transition-[color,box-shadow] "
    f"{INTERACTIVE_STATE_CLASSES} h-9 "
    "bg-(image:--chevron-down-icon-50) bg-no-repeat bg-position-[center_right_0.75rem] bg-size-[1rem]"
)

# ============================================================================
# Surface styles (elevated containers)
# ============================================================================

# Surface tokens for card and popover-like components
SURFACE_CARD_CLASSES = "bg-card text-card-foreground border border-border shadow-sm"
SURFACE_POPOVER_CLASSES = "bg-popover text-popover-foreground border border-border shadow-md"

# ============================================================================
# Popover/Dropdown styles
# ============================================================================

# Popover panel surface (used by select, combobox, dropdown-menu, tooltip, etc.)
POPOVER_PANEL_CLASSES = f"rounded-md z-50 {SURFACE_POPOVER_CLASSES}"

# Popover panel with padding (for content)
POPOVER_PANEL_PADDED_CLASSES = f"{POPOVER_PANEL_CLASSES} p-1"

# ============================================================================
# Menu/Dropdown item styles
# ============================================================================

# Menu item base (for dropdown menu items)
MENU_ITEM_BASE_CLASSES = (
    "relative flex cursor-default items-center gap-2 rounded-sm px-2 py-1.5 "
    "text-sm outline-hidden select-none w-full truncate "
    f"{ICON_INLINE_CLASSES} "
    f"{FOCUS_ACCENT_CLASSES} {HOVER_ACCENT_CLASSES}"
)

# ============================================================================
# Listbox/Option styles
# ============================================================================

# Listbox option base (for select, combobox, dropdown menu items)
LISTBOX_OPTION_BASE_CLASSES = (
    "relative flex cursor-pointer items-center gap-2 rounded-sm pl-2 py-1.5 pr-7.5 "
    "text-sm outline-hidden select-none w-full truncate "
    f"{ICON_INLINE_CLASSES} "
    f"{FOCUS_ACCENT_CLASSES} {HOVER_ACCENT_CLASSES}"
)

# Listbox option selected state (applied via Alpine/JS)
LISTBOX_OPTION_SELECTED_CLASSES = "bg-accent text-accent-foreground"

# Listbox section heading (for grouped options)
LISTBOX_SECTION_HEADING_CLASSES = "flex text-muted-foreground px-2 py-1.5 text-xs"

# Listbox empty state
LISTBOX_EMPTY_CLASSES = (
    "flex items-center justify-center p-2 text-muted-foreground opacity-50 "
    "pointer-events-none select-none gap-2"
)

# ============================================================================
# Badge styles
# ============================================================================

BADGE_BASE_CLASSES = (
    "inline-flex items-center justify-center rounded-full border px-2 py-0.5 "
    "text-xs font-medium h-6 whitespace-nowrap shrink-0 gap-1 "
    f"{ICON_INLINE_SMALL_CLASSES} "
    f"{FOCUS_RING_CLASSES} transition-[color,box-shadow] overflow-hidden"
)

BADGE_VARIANT_PRIMARY_CLASSES = (
    "border-transparent bg-primary text-primary-foreground [a&]:hover:bg-primary/90"
)

BADGE_VARIANT_SECONDARY_CLASSES = (
    "border-transparent bg-secondary text-secondary-foreground [a&]:hover:bg-secondary/90"
)

BADGE_VARIANT_DESTRUCTIVE_CLASSES = (
    "border-transparent bg-destructive text-white [a&]:hover:bg-destructive/90 "
    "focus-visible:ring-destructive/20 dark:focus-visible:ring-destructive/40 "
    "dark:bg-destructive/60 dark:[a&]:hover:bg-destructive/50"
)

BADGE_VARIANT_OUTLINE_CLASSES = (
    "bg-background border border-border text-foreground "
    "[a&]:hover:bg-accent [a&]:hover:text-accent-foreground"
)

# ============================================================================
# Alert styles
# ============================================================================

ALERT_BASE_CLASSES = (
    "relative w-full rounded-lg border px-4 py-3 text-sm grid "
    "grid-cols-[0_1fr] has-[>svg]:grid-cols-[calc(var(--spacing)*4)_1fr] "
    "has-[>svg]:gap-x-3 gap-y-0.5 items-start "
    "[&>svg]:size-4 [&>svg]:translate-y-0.5 [&>svg]:text-current "
    "bg-card shadow-sm border-border"
)

ALERT_DESTRUCTIVE_CLASSES = "text-destructive"

# ============================================================================
# Card styles
# ============================================================================

CARD_BASE_CLASSES = f"flex flex-col gap-6 rounded-xl {SURFACE_CARD_CLASSES}"

# ============================================================================
# Tab styles
# ============================================================================

TAB_BASE_CLASSES = (
    "focus-visible:outline-ring text-muted-foreground inline-flex h-[calc(100%-1px)] flex-1 "
    "items-center justify-center gap-1.5 rounded-md px-2 py-1 border border-transparent "
    "text-sm font-medium whitespace-nowrap transition-[color,box-shadow] "
    f"{INTERACTIVE_STATE_CLASSES} focus-visible:outline-1 cursor-pointer "
    f"{ICON_INLINE_CLASSES}"
)

TAB_SELECTED_CLASSES = (
    "bg-background text-foreground border border-border shadow-sm "
    "dark:text-foreground dark:border-input dark:bg-input/30"
)

TAB_LIST_CONTAINER_CLASSES = (
    "bg-muted text-muted-foreground inline-flex h-9 w-full items-center "
    "justify-center rounded-lg p-[3px] border border-border"
)
