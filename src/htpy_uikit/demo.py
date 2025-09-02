from typing import cast

from htpy import Node
from htpy import a
from htpy import div
from htpy import form as form_
from htpy import h1
from htpy import h2
from htpy import h4
from htpy import h5
from htpy import header
from htpy import img
from htpy import li
from htpy import nav
from htpy import ol
from htpy import p
from htpy import span

from htpy_uikit.components._types import TAlign
from htpy_uikit.components._types import TSide
from htpy_uikit.components.accordion import accordion
from htpy_uikit.components.alert import alert
from htpy_uikit.components.alert_dialog import alert_dialog
from htpy_uikit.components.alert_dialog import alert_dialog_destructive
from htpy_uikit.components.alert_dialog import attrs_btn_open_alert_dialog
from htpy_uikit.components.alert_dialog import confirm_dialog
from htpy_uikit.components.avatar import avatar
from htpy_uikit.components.avatar import avatar_group
from htpy_uikit.components.avatar import avatar_text
from htpy_uikit.components.badge import badge
from htpy_uikit.components.badge import badge_count
from htpy_uikit.components.badge import badge_link
from htpy_uikit.components.badge import badge_status
from htpy_uikit.components.breadcrumb import breadcrumb
from htpy_uikit.components.button import button_component
from htpy_uikit.components.card import card
from htpy_uikit.components.checkbox import checkbox_card_component
from htpy_uikit.components.checkbox import checkbox_component
from htpy_uikit.components.combobox import combobox
from htpy_uikit.components.dropdown_menu import dropdown_menu
from htpy_uikit.components.dropdown_menu import dropdown_menu_group
from htpy_uikit.components.dropdown_menu import dropdown_menu_item
from htpy_uikit.components.dropdown_menu import dropdown_menu_item_checkbox
from htpy_uikit.components.dropdown_menu import dropdown_menu_item_radio
from htpy_uikit.components.dropdown_menu import dropdown_menu_separator
from htpy_uikit.components.form import form_component
from htpy_uikit.components.icons import icon_arrow_right
from htpy_uikit.components.icons import icon_bar
from htpy_uikit.components.icons import icon_check
from htpy_uikit.components.icons import icon_chevron_right
from htpy_uikit.components.icons import icon_credit_card
from htpy_uikit.components.icons import icon_double_chevron
from htpy_uikit.components.icons import icon_download
from htpy_uikit.components.icons import icon_info
from htpy_uikit.components.icons import icon_line
from htpy_uikit.components.icons import icon_logout
from htpy_uikit.components.icons import icon_more
from htpy_uikit.components.icons import icon_pie
from htpy_uikit.components.icons import icon_send
from htpy_uikit.components.icons import icon_settings
from htpy_uikit.components.icons import icon_spinner
from htpy_uikit.components.icons import icon_trash
from htpy_uikit.components.icons import icon_upload
from htpy_uikit.components.icons import icon_user
from htpy_uikit.components.input import input_component
from htpy_uikit.components.label import label_component
from htpy_uikit.components.modal import attrs_btn_open_modal
from htpy_uikit.components.modal import modal
from htpy_uikit.components.navbar import navbar_simple
from htpy_uikit.components.pagination import pagination
from htpy_uikit.components.popover import popover
from htpy_uikit.components.popover import popover_trigger_button
from htpy_uikit.components.radio_group import radio_group
from htpy_uikit.components.radio_group import radio_group_cards
from htpy_uikit.components.select import native_select
from htpy_uikit.components.select import select_component
from htpy_uikit.components.skeleton import skeleton_avatar
from htpy_uikit.components.skeleton import skeleton_button
from htpy_uikit.components.skeleton import skeleton_card
from htpy_uikit.components.skeleton import skeleton_media_row
from htpy_uikit.components.skeleton import skeleton_table
from htpy_uikit.components.skeleton import skeleton_text
from htpy_uikit.components.skeleton import skeleton_title
from htpy_uikit.components.slider import slider
from htpy_uikit.components.switch import switch
from htpy_uikit.components.switch import switch_card
from htpy_uikit.components.table import table_component
from htpy_uikit.components.tabs import tabs
from htpy_uikit.components.textarea import textarea_component
from htpy_uikit.components.theme_toggle import theme_toggle
from htpy_uikit.components.toast import toast_trigger
from htpy_uikit.components.toast import toaster
from htpy_uikit.components.tooltip import tooltip


def components_demo_page() -> Node:
    """
    Comprehensive demo page showcasing all Basecoat UI components.

    Returns:
        htpy.div: Demo page with all components
    """

    return div(class_="min-h-screen bg-background")[
        # Navbar with theme toggle (reusable component)
        navbar_simple(right=nav(class_="flex items-center")[theme_toggle()]),
        div(class_="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12")[
            # Header
            div(class_="relative overflow-hidden bg-background mt-6 w-full")[
                div(class_="relative max-w-7xl py-4")[
                    h1(class_="text-3xl font-bold tracking-tight text-foreground mb-2")[
                        "Kitchen Sink"
                    ],
                    p(class_="text-base text-muted-foreground max-w-2xl")[
                        "A collection of all the components available."
                    ],
                ]
            ],
            # Main content
            div(class_="space-y-16")[
                # Accordion
                _demo_section(
                    "Accordion",
                    "Collapsible content panels",
                    [
                        accordion(
                            [
                                {
                                    "title": "What is Basecoat UI?",
                                    "content": "Basecoat UI is a collection of reusable UI components built with htpy and Tailwind CSS.",
                                },
                                {
                                    "title": "How do I use it?",
                                    "content": "Simply import the components you need and use them in your templates.",
                                },
                                {
                                    "title": "Is it customizable?",
                                    "content": "Yes! All components accept class overrides and additional attributes.",
                                },
                            ]
                        )
                    ],
                ),
                # Alert
                _demo_section(
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
                ),
                # Alert Dialog
                _demo_section(
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
                ),
                # Avatar
                _demo_section(
                    "Avatar",
                    "User profile pictures and placeholders",
                    [
                        div(class_="flex items-center space-x-4")[
                            avatar(src="https://github.com/dakixr.png", size="sm"),
                            avatar_text("CN", size="md"),
                            avatar(src="https://github.com/hunvreus.png", size="md"),
                            avatar(src="https://github.com/hunvreus.png", size="lg"),
                        ],
                        div(class_="mt-6")[
                            avatar_group(
                                [
                                    {
                                        "src": "https://github.com/dakixr.png",
                                        "alt": "@dakixr",
                                    },
                                    {
                                        "src": "https://github.com/shadcn.png",
                                        "alt": "@shadcn",
                                    },
                                    {
                                        "src": "https://github.com/adamwathan.png",
                                        "alt": "@adamwathan",
                                    },
                                ],
                                size="lg",
                                ring=True,
                            ),
                        ],
                        div(class_="mt-4")[
                            avatar_group(
                                [
                                    {
                                        "src": "https://github.com/dakixr.png",
                                        "alt": "@dakixr",
                                    },
                                    {
                                        "src": "https://github.com/shadcn.png",
                                        "alt": "@shadcn",
                                    },
                                    {
                                        "src": "https://github.com/adamwathan.png",
                                        "alt": "@adamwathan",
                                    },
                                ],
                                size="xl",
                                ring=True,
                                hover_expand=True,
                            ),
                        ],
                    ],
                ),
                # Badge
                _demo_section(
                    "Badge",
                    "Status indicators and labels",
                    [
                        div(class_="flex flex-wrap items-center gap-2")[
                            badge(variant="primary")["Primary"],
                            badge(variant="secondary")["Secondary"],
                            badge(variant="destructive")["Destructive"],
                            badge(variant="outline")["Outline"],
                            # With icons
                            badge(variant="primary", left_icon=icon_check())["Badge"],
                            badge(variant="destructive", left_icon=icon_info())[
                                "Alert"
                            ],
                            badge(variant="outline", right_icon=icon_chevron_right())[
                                "With icon"
                            ],
                            # Counters (compact)
                            badge_count(8, variant="primary"),
                            badge_count(99, variant="destructive"),
                            badge_count(27, variant="outline"),
                            # Small pill examples
                            badge(class_="ml-2 px-2 py-0.5")["20+"],
                            # With link
                            badge_link(
                                "Link to GitHub",
                                href="https://github.com/dakixr",
                                new_tab=True,
                            ),
                        ]
                    ],
                ),
                # Breadcrumb
                _demo_section(
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
                ),
                # Button
                _demo_section(
                    "Button",
                    "Interactive buttons with various styles and states",
                    [
                        div(class_="space-y-6")[
                            # Row 1: main variants and a primary action
                            div(class_="flex flex-wrap items-center gap-3")[
                                button_component(variant="primary")["Primary"],
                                button_component(variant="outline")["Outline"],
                                button_component(variant="ghost")["Ghost"],
                                button_component(variant="destructive")["Destructive"],
                                button_component(variant="danger")["Danger"],
                                button_component(variant="secondary")["Secondary"],
                                button_component(variant="link")["Link"],
                                button_component(variant="primary")[
                                    icon_send(), "Send email"
                                ],
                            ],
                            # Row 2: call-to-action + small controls
                            div(class_="flex flex-wrap items-center gap-3")[
                                button_component(
                                    variant="primary", class_="rounded-full px-4"
                                )["Learn more", icon_arrow_right()],
                                button_component(variant="outline", loading=True)[
                                    "Loading"
                                ],
                                button_component(disabled=True)["Disabled"],
                            ],
                            # Row 3: a second variation row to match reference spacing
                            div(class_="flex flex-wrap items-center gap-3")[
                                button_component(variant="primary")["Primary"],
                                button_component(variant="outline")["Outline"],
                                button_component(variant="ghost")["Ghost"],
                                button_component(variant="danger")["Danger"],
                                button_component(variant="secondary")["Secondary"],
                                button_component(variant="link")["Link"],
                                button_component(variant="primary")[
                                    icon_send(), "Send"
                                ],
                                button_component(variant="outline", class_="ml-2")[
                                    icon_download(), "Download"
                                ],
                            ],
                            # Row 4: sizes and icon-only compact group
                            div(class_="flex flex-wrap items-center gap-3")[
                                button_component(variant="primary", size="sm")[
                                    "Primary sm"
                                ],
                                button_component(variant="primary")["Primary md"],
                                button_component(variant="primary", size="lg")[
                                    "Primary lg"
                                ],
                                button_component(icon_only=True)[icon_download()],
                                button_component(variant="outline", icon_only=True)[
                                    icon_upload()
                                ],
                                button_component(variant="destructive", icon_only=True)[
                                    icon_trash()
                                ],
                                button_component(icon_only=True)[icon_arrow_right()],
                            ],
                            # Row 5: mixed compact controls and separators (icon-only set)
                            div(class_="flex items-center gap-2")[
                                button_component(icon_only=True)[icon_download()],
                                button_component(variant="secondary", icon_only=True)[
                                    icon_upload()
                                ],
                                button_component(variant="outline", icon_only=True)[
                                    icon_arrow_right()
                                ],
                                button_component(variant="ghost", icon_only=True)[
                                    icon_more()
                                ],
                                button_component(variant="destructive", icon_only=True)[
                                    icon_trash()
                                ],
                                button_component(variant="outline", icon_only=True)[
                                    icon_spinner()
                                ],
                            ],
                        ]
                    ],
                ),
                # Card
                _demo_section(
                    "Card",
                    "Content containers with headers and padding",
                    [
                        div(class_="grid grid-cols-1 gap-6")[
                            # Meeting notes (full content + footer avatars)
                            card(
                                title="Meeting Notes",
                                description="Transcript from the meeting with the client.",
                                footer_content=div(class_="flex -space-x-2")[
                                    avatar_group(
                                        [
                                            {
                                                "src": "https://github.com/dakixr.png",
                                                "alt": "Avatar",
                                            },
                                            {
                                                "src": "https://github.com/shadcn.png",
                                                "alt": "Avatar",
                                            },
                                            {
                                                "src": "https://github.com/adamwathan.png",
                                                "alt": "Avatar",
                                            },
                                        ],
                                        size="sm",
                                        hover_expand=True,
                                    ),
                                ],
                            )[
                                div[
                                    p[
                                        "Client requested dashboard redesign with focus on mobile responsiveness."
                                    ],
                                    ol(
                                        class_="mt-4 flex list-decimal flex-col gap-2 pl-6"
                                    )[
                                        li[
                                            "New analytics widgets for daily/weekly metrics"
                                        ],
                                        li["Simplified navigation menu"],
                                        li["Dark mode support"],
                                        li["Timeline: 6 weeks"],
                                        li[
                                            "Follow-up meeting scheduled for next Tuesday"
                                        ],
                                    ],
                                ]
                            ],
                            # Image card (image in section + footer badges/price)
                            card(
                                title="Is this an image?",
                                description="This is a card with an image.",
                                footer_content=div(class_="flex items-center gap-2")[
                                    badge(variant="outline")["1"],
                                    badge(variant="outline")["2"],
                                    span(class_="ml-auto font-medium tabular-nums")[
                                        "$135,000"
                                    ],
                                ],
                            )[
                                div(class_="px-0")[
                                    img(
                                        src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800&q=75",
                                        alt="Photo",
                                        loading="lazy",
                                        class_="aspect-video object-cover w-full rounded-md",
                                    )
                                ]
                            ],
                            # Simple text-only card
                            card()[
                                p[
                                    "This is a simple card containing only text to demonstrate content-only cards."
                                ]
                            ],
                            # Login form card (form in section + full width footer buttons)
                            card(
                                title="Login to your account",
                                description="Enter your details below to login to your account",
                                footer_content=div(
                                    class_="flex flex-col items-center gap-2 w-full"
                                )[
                                    button_component(
                                        variant="primary", class_="w-full"
                                    )["Login"],
                                    button_component(
                                        variant="outline", class_="w-full"
                                    )["Login with Google"],
                                    p(class_="mt-4 text-center text-sm")[
                                        "Don't have an account? ",
                                        a(href="#", hx_boost=True)[
                                            button_component(variant="link")["Sign up"]
                                        ],
                                    ],
                                ],
                            )[
                                form_component(
                                    method="post", action="/login", class_="grid gap-6"
                                )[
                                    div(class_="grid gap-2")[
                                        label_component(for_="demo-card-form-email")[
                                            "Email"
                                        ],
                                        input_component(
                                            type="email",
                                            id="demo-card-form-email",
                                            name="email",
                                        ),
                                    ],
                                    div(class_="grid gap-2")[
                                        div(class_="flex items-center gap-2")[
                                            label_component(
                                                for_="demo-card-form-password"
                                            )["Password"],
                                            a(
                                                href="#",
                                                class_="ml-auto inline-block text-sm underline-offset-4 hover:underline",
                                            )["Forgot your password?"],
                                        ],
                                        input_component(
                                            type="password",
                                            id="demo-card-form-password",
                                            name="password",
                                        ),
                                    ],
                                ]
                            ],
                        ]
                    ],
                ),
                # Checkbox
                _demo_section(
                    "Checkbox",
                    "Boolean input controls",
                    [
                        div(class_="space-y-4")[
                            checkbox_component(
                                id="demo-cb-1",
                                label_text="Accept terms and conditions",
                            ),
                            checkbox_component(
                                id="demo-cb-2",
                                label_text="Accept terms and conditions",
                                description=(
                                    "By clicking this checkbox, you agree to the terms and conditions."
                                ),
                            ),
                            checkbox_component(
                                id="demo-cb-3",
                                label_text="Enable notifications",
                                disabled=True,
                            ),
                            checkbox_card_component(
                                id="demo-cb-card",
                                label_text="Enable notifications",
                                description="You can enable or disable notifications at any time.",
                                card_color="blue",
                            ),
                            checkbox_card_component(
                                id="demo-cb-card-2",
                                label_text="Enable notifications",
                                description="You can enable or disable notifications at any time.",
                                card_color="red",
                            ),
                            checkbox_card_component(
                                id="demo-cb-card-3",
                                label_text="Enable notifications",
                                description="You can enable or disable notifications at any time.",
                                card_color="green",
                            ),
                        ]
                    ],
                ),
                # Combobox
                _demo_section(
                    "Combobox",
                    "Searchable dropdown selections",
                    [
                        div(class_="grid grid-cols-1 md:grid-cols-2 gap-4")[
                            # Simple combobox
                            combobox(
                                name="fruit",
                                options=[
                                    {"value": "apple", "label": "Apple"},
                                    {"value": "banana", "label": "Banana"},
                                    {"value": "orange", "label": "Orange"},
                                    {"value": "grape", "label": "Grape"},
                                ],
                                placeholder="Select a fruit...",
                                width_class="w-[220px]",
                            ),
                            # Combobox with initial value and wider popover
                            combobox(
                                name="framework",
                                options=[
                                    {"value": "next", "label": "Next.js"},
                                    {"value": "svelte", "label": "SvelteKit"},
                                    {"value": "nuxt", "label": "Nuxt.js"},
                                    {"value": "remix", "label": "Remix"},
                                    {"value": "astro", "label": "Astro"},
                                ],
                                value="svelte",
                                placeholder="Search framework...",
                                width_class="w-[220px]",
                                popover_width_class="w-72",
                            ),
                        ]
                    ],
                ),
                # Dialog
                _demo_section(
                    "Dialog",
                    "Modal dialogs for user interactions",
                    [
                        div(class_="flex gap-4")[
                            button_component(**attrs_btn_open_modal("demo-modal"))[
                                "Open Modal"
                            ],
                            modal(id="demo-modal", title="Demo Modal")[
                                div[
                                    p["This is a modal dialog with custom content."],
                                    p[
                                        "You can put any content here, including forms, images, or other components."
                                    ],
                                    div(class_="mt-4 flex gap-2 justify-end")[
                                        button_component(variant="outline")["Cancel"],
                                        button_component(variant="primary")[
                                            "Save Changes"
                                        ],
                                    ],
                                ]
                            ],
                        ]
                    ],
                ),
                # Dropdown Menu
                _demo_section(
                    "Dropdown Menu",
                    "Contextual menus and actions",
                    [
                        # Row 1: reference-style trigger buttons
                        div(class_="flex items-center gap-4 mb-6")[
                            dropdown_menu(
                                trigger=button_component(variant="outline")["Open"]
                            )[
                                div[
                                    dropdown_menu_group(
                                        div[
                                            dropdown_menu_item(
                                                "Profile", left_icon=icon_user()
                                            ),
                                            dropdown_menu_item(
                                                "Billing", left_icon=icon_credit_card()
                                            ),
                                            dropdown_menu_item(
                                                "Settings", left_icon=icon_settings()
                                            ),
                                            dropdown_menu_item(
                                                "Keyboard shortcuts", shortcut="⌘K"
                                            ),
                                        ],
                                        label="My Account",
                                    ),
                                    dropdown_menu_separator(),
                                    dropdown_menu_item("GitHub"),
                                    dropdown_menu_item("Support"),
                                    dropdown_menu_item("API", disabled=True),
                                    dropdown_menu_separator(),
                                    dropdown_menu_item(
                                        "Logout",
                                        shortcut="⇧⌘P",
                                        left_icon=icon_logout(),
                                    ),
                                ]
                            ],
                            dropdown_menu(
                                trigger=button_component(variant="outline")[
                                    "Checkboxes"
                                ]
                            )[
                                div[
                                    dropdown_menu_group(
                                        div[
                                            dropdown_menu_item(
                                                "Profile",
                                                shortcut="⇧⌘P",
                                                left_icon=icon_user(),
                                            ),
                                            dropdown_menu_item(
                                                "Billing",
                                                shortcut="⌘B",
                                                left_icon=icon_credit_card(),
                                            ),
                                            dropdown_menu_item(
                                                "Settings",
                                                shortcut="⌘S",
                                                left_icon=icon_settings(),
                                            ),
                                        ],
                                        label="Account Options",
                                    ),
                                    dropdown_menu_separator(),
                                    dropdown_menu_group(
                                        div[
                                            dropdown_menu_item_checkbox(
                                                label="Status Bar", checked=True
                                            ),
                                            dropdown_menu_item_checkbox(
                                                label="Activity Bar", disabled=True
                                            ),
                                            dropdown_menu_item_checkbox(label="Panel"),
                                        ],
                                        label="Appearance",
                                    ),
                                    dropdown_menu_separator(),
                                    dropdown_menu_item(
                                        "Logout",
                                        shortcut="⇧⌘P",
                                        left_icon=icon_logout(),
                                    ),
                                ]
                            ],
                            dropdown_menu(
                                trigger=button_component(variant="outline")[
                                    "Radio Group"
                                ]
                            )[
                                div[
                                    dropdown_menu_group(
                                        div[
                                            dropdown_menu_separator(),
                                            dropdown_menu_item_radio(
                                                label="Status Bar", group="panel-pos"
                                            ),
                                            dropdown_menu_item_radio(
                                                label="Activity Bar",
                                                group="panel-pos",
                                                checked=True,
                                            ),
                                            dropdown_menu_item_radio(
                                                label="Panel", group="panel-pos"
                                            ),
                                        ],
                                        label="Panel Position",
                                    ),
                                ]
                            ],
                        ],
                        # Row 2: custom trigger examples (icon-only, icon+label, avatar)
                        div(class_="flex items-center gap-4")[
                            dropdown_menu(
                                trigger=button_component(
                                    variant="ghost", class_="p-2 rounded-md"
                                )[icon_more()]
                            )[
                                div[
                                    dropdown_menu_item("Item A"),
                                    dropdown_menu_item("Item B"),
                                ]
                            ],
                            dropdown_menu(
                                trigger=button_component(variant="outline")[
                                    icon_more(), "More"
                                ]
                            )[
                                div[
                                    dropdown_menu_item("Action 1"),
                                    dropdown_menu_item("Action 2"),
                                ]
                            ],
                            dropdown_menu(
                                trigger=button_component(variant="ghost")[
                                    avatar(
                                        src="https://github.com/dakixr.png", size="sm"
                                    )
                                ]
                            )[
                                div[
                                    dropdown_menu_item(
                                        "Profile", left_icon=icon_user()
                                    ),
                                    dropdown_menu_item(
                                        "Sign out", left_icon=icon_logout()
                                    ),
                                ]
                            ],
                        ],
                    ],
                ),
                # Form
                _demo_section(
                    "Form",
                    "Structured form layouts and validation",
                    [
                        form_component(
                            method="post",
                            action="/submit",
                        )[
                            div(class_="space-y-4")[
                                input_component(
                                    name="name",
                                    placeholder="Enter your name",
                                    label_text="Full Name",
                                    required=True,
                                ),
                                input_component(
                                    name="email",
                                    type="email",
                                    placeholder="john@example.com",
                                    label_text="Email Address",
                                    required=True,
                                ),
                                button_component(variant="primary", type="submit")[
                                    "Submit"
                                ],
                            ]
                        ]
                    ],
                ),
                # Input
                _demo_section(
                    "Input",
                    "Text input fields with labels",
                    [
                        div(class_="space-y-3")[
                            input_component(type="text", placeholder="Text"),
                            input_component(
                                type="text", placeholder="Disabled", disabled=True
                            ),
                            input_component(
                                type="text", placeholder="Error", invalid=True
                            ),
                            input_component(type="email", placeholder="Email"),
                            input_component(type="password", placeholder="Password"),
                            input_component(type="number", placeholder="Number"),
                            input_component(type="file"),
                            input_component(type="tel", placeholder="Tel"),
                            input_component(type="url", placeholder="URL"),
                            input_component(type="search", placeholder="Search"),
                            input_component(type="date"),
                            input_component(type="datetime-local"),
                            input_component(type="time"),
                        ]
                    ],
                ),
                # Label
                _demo_section(
                    "Label",
                    "Form field labels and descriptions",
                    [
                        div(class_="space-y-4")[
                            # Label wrapping a control (checkbox inline label example)
                            div[
                                label_component(
                                    for_="demo-accept",
                                    class_="flex items-center gap-2",
                                )[
                                    checkbox_component(id="demo-accept"),
                                    p["Accept terms and conditions"],
                                ]
                            ],
                            # Label with description
                            input_component(
                                placeholder="Enter your name",
                                label_text="Full Name",
                                description="This is your legal name",
                            ),
                            input_component(
                                placeholder="Disabled",
                                label_text="Disabled",
                                description="This is a disabled input",
                                disabled=True,
                            ),
                            input_component(
                                type="email",
                                placeholder="john@example.com",
                                label_text="Email Address",
                                description="We'll never share your email with anyone",
                            ),
                        ]
                    ],
                ),
                # Pagination
                _demo_section(
                    "Pagination",
                    "Navigation for multi-page content",
                    [
                        pagination(
                            current_page=1, total_pages=20, show_pages=5, size="md"
                        ),
                        pagination(
                            current_page=5, total_pages=20, show_pages=5, size="sm"
                        ),
                        pagination(
                            current_page=20, total_pages=20, show_pages=5, size="lg"
                        ),
                    ],
                ),
                # Popover
                _demo_section(
                    "Popover",
                    "Floating content overlays",
                    [
                        popover(
                            id="demo-popover",
                            trigger=popover_trigger_button(popover_id="demo-popover")[
                                "Open popover"
                            ],
                            width_class="w-80",
                        )[
                            div(class_="grid gap-4")[
                                header(class_="grid gap-1.5")[
                                    h4(class_="leading-none font-medium")["Dimensions"],
                                    p(class_="text-muted-foreground text-sm")[
                                        "Set the dimensions for the layer."
                                    ],
                                ],
                                form_(class_="form grid gap-2")[
                                    div(class_="grid grid-cols-3 items-center gap-4")[
                                        label_component(for_="demo-popover-width")[
                                            "Width"
                                        ],
                                        input_component(
                                            type="text",
                                            id="demo-popover-width",
                                            value="100%",
                                            class_="col-span-2 h-8",
                                            autofocus="true",
                                        ),
                                    ],
                                    div(class_="grid grid-cols-3 items-center gap-4")[
                                        label_component(for_="demo-popover-max-width")[
                                            "Max. width"
                                        ],
                                        input_component(
                                            type="text",
                                            id="demo-popover-max-width",
                                            value="300px",
                                            class_="col-span-2 h-8",
                                        ),
                                    ],
                                    div(class_="grid grid-cols-3 items-center gap-4")[
                                        label_component(for_="demo-popover-height")[
                                            "Height"
                                        ],
                                        input_component(
                                            type="text",
                                            id="demo-popover-height",
                                            value="25px",
                                            class_="col-span-2 h-8",
                                        ),
                                    ],
                                    div(class_="grid grid-cols-3 items-center gap-4")[
                                        label_component(for_="demo-popover-max-height")[
                                            "Max. height"
                                        ],
                                        input_component(
                                            type="text",
                                            id="demo-popover-max-height",
                                            value="none",
                                            class_="col-span-2 h-8",
                                        ),
                                    ],
                                ],
                            ]
                        ]
                    ],
                ),
                # Radio Group
                _demo_section(
                    "Radio Group",
                    "Single selection from multiple options",
                    [
                        radio_group(
                            name="demo-radio",
                            options=[
                                {"value": "default", "label": "Default"},
                                {"value": "comfortable", "label": "Comfortable"},
                                {"value": "compact", "label": "Compact"},
                            ],
                            label_text="Choose an option",
                        ),
                        div(class_="mt-6 max-w-sm")[
                            radio_group_cards(
                                name="demo-radio-card",
                                options=[
                                    {
                                        "value": "starter",
                                        "title": "Starter Plan",
                                        "description": "Perfect for small businesses getting started with our platform",
                                    },
                                    {
                                        "value": "pro",
                                        "title": "Pro Plan",
                                        "description": "Advanced features for growing businesses with higher demands",
                                    },
                                ],
                                card_color="green",
                            )
                        ],
                    ],
                ),
                # Select
                _demo_section(
                    "Select",
                    "Dropdown selection menus",
                    [
                        div(class_="flex flex-wrap items-center gap-2 md:flex-row")[
                            native_select(
                                class_="w-[180px]",
                                options=[
                                    {"value": "apple", "label": "Apple"},
                                    {"value": "banana", "label": "Banana"},
                                    {"value": "blueberry", "label": "Blueberry"},
                                ],
                                placeholder="Fruits",
                            ),
                            native_select(
                                class_="w-[180px]",
                                options=[{"value": "disabled", "label": "Disabled"}],
                                value="disabled",
                                disabled=True,
                            ),
                        ],
                        div(class_="flex flex-wrap items-center gap-4 mt-4")[
                            # Default popover select with groups-like data
                            select_component(
                                id="select-default",
                                width_class="w-[180px]",
                                options=[
                                    {
                                        "type": "group",
                                        "label": "Fruits",
                                        "items": [
                                            {
                                                "type": "item",
                                                "value": "apple",
                                                "label": "Apple",
                                            },
                                            {
                                                "type": "item",
                                                "value": "banana",
                                                "label": "Banana",
                                            },
                                            {
                                                "type": "item",
                                                "value": "blueberry",
                                                "label": "Blueberry",
                                            },
                                        ],
                                    },
                                    {
                                        "type": "group",
                                        "label": "Grapes",
                                        "items": [
                                            {
                                                "type": "item",
                                                "value": "pineapple",
                                                "label": "Pineapple",
                                            },
                                        ],
                                    },
                                ],
                                value="apple",
                            ),
                            # Scrollable long list
                            select_component(
                                id="select-scrollbar",
                                width_class="w-[180px]",
                                scrollable=True,
                                options=[
                                    *(
                                        {"value": f"item-{i}", "label": f"Item {i}"}
                                        for i in range(0, 99)
                                    )
                                ],
                                value="item-0",
                            ),
                            # Disabled
                            select_component(
                                id="select-disabled",
                                width_class="w-[180px]",
                                options=[{"value": "disabled", "label": "Disabled"}],
                                value="disabled",
                                disabled=True,
                            ),
                            # With icon in options
                            select_component(
                                id="select-with-icon",
                                width_class="w-[180px]",
                                options=[
                                    {
                                        "type": "group",
                                        "label": "Charts",
                                        "items": [
                                            {
                                                "type": "item",
                                                "value": "bar",
                                                "label": "Bar",
                                                "icon": icon_bar(
                                                    class_="text-muted-foreground"
                                                ),
                                            },
                                            {
                                                "type": "item",
                                                "value": "line",
                                                "label": "Line",
                                                "icon": icon_line(
                                                    class_="text-muted-foreground"
                                                ),
                                            },
                                            {
                                                "type": "item",
                                                "value": "pie",
                                                "label": "Pie",
                                                "icon": icon_pie(
                                                    class_="text-muted-foreground"
                                                ),
                                            },
                                        ],
                                    }
                                ],
                                value="bar",
                            ),
                        ],
                    ],
                ),
                # Skeleton
                _demo_section(
                    "Skeleton",
                    "Loading state placeholders",
                    [
                        div(class_="space-y-6")[
                            # Individual skeleton components
                            div[
                                h5(
                                    class_="text-xs font-medium text-muted-foreground mb-2"
                                )["Basic Skeletons"],
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
                                h5(
                                    class_="text-xs font-medium text-muted-foreground mb-2"
                                )["Media rows"],
                                div(class_="space-y-2")[
                                    skeleton_media_row(),
                                    skeleton_media_row(),
                                ],
                            ],
                            # Complex skeletons
                            div[
                                h5(
                                    class_="text-xs font-medium text-muted-foreground mb-2"
                                )["Complex Skeletons"],
                                div(class_="flex max-sm:flex-col gap-4 w-full")[
                                    skeleton_card(),
                                    skeleton_card(),
                                ],
                                div(class_="mt-4")[skeleton_table(rows=3, columns=3)],
                            ],
                        ]
                    ],
                ),
                # Slider
                _demo_section(
                    "Slider",
                    "Range input controls",
                    [
                        div(class_="grid gap-4 max-w-xl")[
                            # Simple slider (reference-style)
                            slider(min=0, max=100, value=25, show_value=True),
                            # Show value beside
                            slider(min=0, max=10, value=3, show_value=True),
                            # Different min/max/step
                            slider(min=-50, max=50, step=5, value=10),
                            # Disabled (muted visuals)
                            slider(min=140, max=200, value=30, disabled=True),
                            # Disabled with value display
                            slider(
                                min=30,
                                max=300,
                                value=75,
                                disabled=True,
                                show_value=True,
                            ),
                            # Form-styled wrapper
                            div(class_="form")[
                                slider(min=10, max=450, value=60, show_value=True)
                            ],
                        ]
                    ],
                ),
                # Switch
                _demo_section(
                    "Switch",
                    "Toggle switches for boolean values",
                    [
                        div(class_="space-y-6 max-w-2xl")[
                            # Simple inline switches
                            div(class_="space-y-3")[
                                switch(label_text="Airplane Mode"),
                                switch(label_text="Bluetooth", checked=True),
                                switch(
                                    label_text="Bluetooth", checked=True, color="blue"
                                ),
                                switch(
                                    label_text="Bluetooth", checked=True, color="green"
                                ),
                                switch(
                                    label_text="Bluetooth", checked=True, color="red"
                                ),
                            ],
                            # Form-style rows
                            div(class_="form grid gap-4 mt-4")[
                                switch_card(
                                    id="share-across-devices",
                                    label_text="Share across devices",
                                    description=(
                                        "Focus is shared across devices, and turns off when you leave the app."
                                    ),
                                ),
                                switch_card(
                                    id="share-across-devices-blue",
                                    label_text="Share across devices",
                                    description=(
                                        "Focus is shared across devices, and turns off when you leave the app."
                                    ),
                                    color="blue",
                                ),
                                switch_card(
                                    id="share-across-devices-green",
                                    label_text="Share across devices",
                                    description=(
                                        "Focus is shared across devices, and turns off when you leave the app."
                                    ),
                                    color="green",
                                ),
                            ],
                        ],
                    ],
                ),
                # Table
                _demo_section(
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
                ),
                # Tabs
                _demo_section(
                    "Tabs",
                    "Organized content panels",
                    [
                        # 1) Tabs with panels (2 panels like reference)
                        div(class_="max-w-[300px]")[
                            tabs(
                                [
                                    {
                                        "value": "account",
                                        "label": "Account",
                                        "content": div(class_="card")[
                                            div(class_="px-4 py-4")[
                                                h2(class_="font-semibold")["Account"],
                                                p(
                                                    class_="text-sm text-muted-foreground"
                                                )[
                                                    "Make changes to your account here. Click save when you're done."
                                                ],
                                            ],
                                            div(class_="p-4")[
                                                form_(class_="form grid gap-6")[
                                                    div(class_="grid gap-3")[
                                                        label_component(
                                                            for_="demo-tabs-account-name"
                                                        )["Name"],
                                                        input_component(
                                                            type="text",
                                                            id="demo-tabs-account-name",
                                                            value="Pedro Duarte",
                                                        ),
                                                    ],
                                                    div(class_="grid gap-3")[
                                                        label_component(
                                                            for_="demo-tabs-account-username"
                                                        )["Username"],
                                                        input_component(
                                                            type="text",
                                                            id="demo-tabs-account-username",
                                                            value="@peduarte",
                                                        ),
                                                    ],
                                                ],
                                            ],
                                            div(class_="px-4 py-3")[
                                                button_component(variant="primary")[
                                                    "Save changes"
                                                ]
                                            ],
                                        ],
                                    },
                                    {
                                        "value": "password",
                                        "label": "Password",
                                        "content": div(class_="card")[
                                            div(class_="px-4 py-4")[
                                                h2(class_="font-semibold")["Password"],
                                                p(
                                                    class_="text-sm text-muted-foreground"
                                                )[
                                                    "Change your password here. After saving, you'll be logged out."
                                                ],
                                            ],
                                            div(class_="p-4")[
                                                form_(class_="form grid gap-6")[
                                                    div(class_="grid gap-3")[
                                                        label_component(
                                                            for_="demo-tabs-password-current"
                                                        )["Current password"],
                                                        input_component(
                                                            type="password",
                                                            id="demo-tabs-password-current",
                                                        ),
                                                    ],
                                                    div(class_="grid gap-3")[
                                                        label_component(
                                                            for_="demo-tabs-password-new"
                                                        )["New password"],
                                                        input_component(
                                                            type="password",
                                                            id="demo-tabs-password-new",
                                                        ),
                                                    ],
                                                ],
                                            ],
                                            div(class_="px-4 py-3")[
                                                button_component(variant="primary")[
                                                    "Save Password"
                                                ]
                                            ],
                                        ],
                                    },
                                ],
                                "account",
                                class_="w-full",
                            )
                        ],
                        # 2) Tabs without panels
                        div(class_="mt-6")[
                            tabs(
                                [
                                    {
                                        "value": "home",
                                        "label": "Home",
                                        "content": div[""],
                                    },
                                    {
                                        "value": "settings",
                                        "label": "Settings",
                                        "content": div[""],
                                    },
                                ],
                                "home",
                            )
                        ],
                        # 3) Tabs with a disabled tab
                        div(class_="mt-6")[
                            tabs(
                                [
                                    {
                                        "value": "home",
                                        "label": "Home",
                                        "content": div[""],
                                    },
                                    {
                                        "value": "disabled",
                                        "label": "Disabled",
                                        "content": div[""],
                                        "disabled": True,
                                    },
                                ],
                                "home",
                                disabled_values={"disabled"},
                            )
                        ],
                        # 4) Tabs with icons
                        div(class_="mt-6")[
                            tabs(
                                [
                                    {
                                        "value": "preview",
                                        "label": div(
                                            class_="inline-flex items-center gap-2"
                                        )[
                                            icon_credit_card(class_="size-4"),
                                            span["Preview"],
                                        ],
                                        "content": div[""],
                                    },
                                    {
                                        "value": "code",
                                        "label": div(
                                            class_="inline-flex items-center gap-2"
                                        )[
                                            icon_double_chevron(class_="size-4"),
                                            span["Code"],
                                        ],
                                        "content": div[""],
                                    },
                                ],
                                "preview",
                            )
                        ],
                    ],
                ),
                # Textarea
                _demo_section(
                    "Textarea",
                    "Multi-line text input fields",
                    [
                        div(class_="space-y-6")[
                            # Default textarea
                            textarea_component(
                                id="demo-textarea",
                                placeholder="Type your message here",
                            ),
                            # With explicit label
                            textarea_component(
                                id="demo-textarea-with-label",
                                placeholder="Type your message here",
                                rows=3,
                                label_text="Label",
                            ),
                            # With label and helper/description
                            textarea_component(
                                id="demo-textarea-with-label-and-description",
                                placeholder="Type your message here",
                                rows=3,
                                label_text="With label and description",
                                required=True,
                                error="This is an error message",
                            ),
                            # Disabled
                            textarea_component(
                                id="demo-textarea-disabled",
                                placeholder="Type your message here",
                                rows=3,
                                disabled=True,
                            ),
                        ]
                    ],
                ),
                # Toast
                _demo_section(
                    "Toast",
                    "Non-intrusive notifications",
                    [
                        # Toaster container
                        div()[
                            toaster(id="toaster", align="end"),
                            div(class_="grid grid-cols-4 gap-3")[
                                toast_trigger(
                                    category="success",
                                    title="Success",
                                    description="A success toast called from the front-end.",
                                )[button_component(variant="outline")["Success"]],
                                toast_trigger(
                                    category="error",
                                    title="Error",
                                    description="An error occurred while saving your changes.",
                                )[button_component(variant="outline")["Error"]],
                                toast_trigger(
                                    category="info",
                                    title="Info",
                                    description="This is some informational message.",
                                )[button_component(variant="outline")["Info"]],
                                toast_trigger(
                                    category="warning",
                                    title="Warning",
                                    description="Be careful with this action.",
                                )[button_component(variant="outline")["Warning"]],
                                # HTMX backend-driven toast (event-only; swap none)
                                button_component(
                                    variant="outline",
                                    hx_trigger="click",
                                    hx_get="/en/events/toast/success",
                                    hx_swap="none",
                                )["Toast from backend (HTMX)"],
                            ],
                        ],
                    ],
                ),
                # Tooltip
                _demo_section(
                    "Tooltip",
                    "Contextual help and information",
                    [
                        div(class_="grid grid-cols-3 gap-4 justify-items-center-safe")[
                            # Generate tooltips for all sides and alignments
                            [
                                tooltip(
                                    content=f"{side.capitalize()} tooltip",
                                    side=side,
                                    align=align,
                                )[
                                    button_component(variant="outline")[
                                        f"{side.capitalize()} - {align}"
                                    ]
                                ]
                                for side in cast(
                                    list[TSide],
                                    ["top", "bottom", "left", "right"],
                                )
                                for align in cast(
                                    list[TAlign],
                                    ["start", "center", "end"],
                                )
                            ]
                        ]
                    ],
                ),
            ],
        ],
    ]


def _demo_section(
    title: str, description: str | None = None, content: list[Node] = []
) -> Node:
    """Helper function to create demo sections."""
    # Render a compact section with a header bar and tighter content area so the
    # demo matches the reference layout more closely.
    return div(class_="rounded-lg shadow-sm border border-border overflow-visible")[
        # header bar
        div(
            class_="px-4 py-3 border-b border-border flex items-center justify-between"
        )[
            h2(class_="font-semibold text-card-foreground")[title],
            span(class_="text-muted-foreground text-sm"),
        ],
        # content area
        div(class_="p-6")[
            (
                p(class_="text-sm text-muted-foreground mb-4")[description]
                if description
                else None
            ),
            div[*content],
        ],
    ]
