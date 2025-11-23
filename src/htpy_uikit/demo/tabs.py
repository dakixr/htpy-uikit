from htpy import Node, div, form as form_, h2, p, span

from htpy_uikit.components.button import button_component
from htpy_uikit.components.icons import icon_credit_card, icon_double_chevron
from htpy_uikit.components.input import input_component
from htpy_uikit.components.label import label_component
from htpy_uikit.components.tabs import tabs

from ._utils import _demo_section


def tabs_section() -> Node:
    return _demo_section(
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
                                    p(class_="text-sm text-muted-foreground")[
                                        "Make changes to your account here. Click save when you're done."
                                    ],
                                ],
                                div(class_="p-4")[
                                    form_(class_="form grid gap-6")[
                                        div(class_="grid gap-3")[
                                            label_component(for_="demo-tabs-account-name")[
                                                "Name"
                                            ],
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
                                    button_component(variant="primary")["Save changes"]
                                ],
                            ],
                        },
                        {
                            "value": "password",
                            "label": "Password",
                            "content": div(class_="card")[
                                div(class_="px-4 py-4")[
                                    h2(class_="font-semibold")["Password"],
                                    p(class_="text-sm text-muted-foreground")[
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
                                            label_component(for_="demo-tabs-password-new")[
                                                "New password"
                                            ],
                                            input_component(
                                                type="password",
                                                id="demo-tabs-password-new",
                                            ),
                                        ],
                                    ],
                                ],
                                div(class_="px-4 py-3")[
                                    button_component(variant="primary")["Save Password"]
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
                            "label": div(class_="inline-flex items-center gap-2")[
                                icon_credit_card(class_="size-4"),
                                span["Preview"],
                            ],
                            "content": div[""],
                        },
                        {
                            "value": "code",
                            "label": div(class_="inline-flex items-center gap-2")[
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
    )
