from htpy import (
    Node,
    body,
    div,
    h1,
    head,
    html,
    link,
    meta,
    nav,
    p,
    script,
    title,
)
from markupsafe import Markup

from htpy_uikit.components.lucide import (
    lucide_auto_init_script,
    lucide_cdn_script,
    lucide_icon,
)
from htpy_uikit.components.navbar import navbar_simple
from htpy_uikit.components.theme_toggle import theme_toggle

from .accordion import accordion_section
from .alert import alert_section
from .alert_dialog import alert_dialog_section
from .avatar import avatar_section
from .badge import badge_section
from .breadcrumb import breadcrumb_section
from .button import button_section
from .card import card_section
from .checkbox import checkbox_section
from .combobox import combobox_section
from .dialog import dialog_section
from .dropdown_menu import dropdown_menu_section
from .form import form_section
from .input import input_section
from .label import label_section
from .pagination import pagination_section
from .popover import popover_section
from .radio_group import radio_group_section
from .select import select_section
from .skeleton import skeleton_section
from .slider import slider_section
from .switch import switch_section
from .table import table_section
from .tabs import tabs_section
from .textarea import textarea_section
from .toast import toast_section
from .tooltip import tooltip_section


def demo_page() -> str:
    doc = html(lang="en")[
        head()[
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
            title()["htpy-uikit demo"],
            link(rel="stylesheet", href="output.css"),
            script(defer=True, src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"),
            script(defer=True, src="https://unpkg.com/lucide@latest"),
            # Initialize theme inline to avoid FOUC
            script[
                Markup(
                    """
                    localStorage.getItem('color-theme') !== 'light' ?
                    document.documentElement.classList.add('dark') :
                    document.documentElement.classList.remove('dark');
                    """
                )
            ],
        ],
        body(class_="bg-background text-foreground", x_data="")[
            components_demo_page(),
            lucide_cdn_script(),
            lucide_auto_init_script(),
        ],
    ]
    return str(doc)


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
                    h1(class_="text-3xl font-bold tracking-tight text-foreground mb-2 inline-flex gap-3")[
                        "Kitchen Sink",
                        lucide_icon("rocket"),
                    ],
                    p(class_="text-base text-muted-foreground max-w-2xl")[
                        "A collection of all the components available."
                    ],
                ]
            ],
            # Main content
            div(class_="space-y-16")[
                accordion_section(),
                alert_section(),
                alert_dialog_section(),
                avatar_section(),
                badge_section(),
                breadcrumb_section(),
                button_section(),
                card_section(),
                checkbox_section(),
                combobox_section(),
                dialog_section(),
                dropdown_menu_section(),
                form_section(),
                input_section(),
                label_section(),
                pagination_section(),
                popover_section(),
                radio_group_section(),
                select_section(),
                skeleton_section(),
                slider_section(),
                switch_section(),
                table_section(),
                tabs_section(),
                textarea_section(),
                toast_section(),
                tooltip_section(),
            ],
        ],
    ]
