from htpy import Node, a, div, form as form_, img, li, ol, p, span

from htpy_uikit.components.avatar import avatar_group
from htpy_uikit.components.badge import badge
from htpy_uikit.components.button import button_component
from htpy_uikit.components.card import card
from htpy_uikit.components.form import form_component
from htpy_uikit.components.input import input_component
from htpy_uikit.components.label import label_component

from ._utils import _demo_section


def card_section() -> Node:
    return _demo_section(
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
                        p["Client requested dashboard redesign with focus on mobile responsiveness."],
                        ol(class_="mt-4 flex list-decimal flex-col gap-2 pl-6")[
                            li["New analytics widgets for daily/weekly metrics"],
                            li["Simplified navigation menu"],
                            li["Dark mode support"],
                            li["Timeline: 6 weeks"],
                            li["Follow-up meeting scheduled for next Tuesday"],
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
                        span(class_="ml-auto font-medium tabular-nums")["$135,000"],
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
                    footer_content=div(class_="flex flex-col items-center gap-2 w-full")[
                        button_component(variant="primary", class_="w-full")["Login"],
                        button_component(variant="outline", class_="w-full")["Login with Google"],
                        p(class_="mt-4 text-center text-sm")[
                            "Don't have an account? ",
                            a(href="#", hx_boost=True)[
                                button_component(variant="link")["Sign up"]
                            ],
                        ],
                    ],
                )[
                    form_component(method="post", action="/login", class_="grid gap-6")[
                        div(class_="grid gap-2")[
                            label_component(for_="demo-card-form-email")["Email"],
                            input_component(
                                type="email",
                                id="demo-card-form-email",
                                name="email",
                            ),
                        ],
                        div(class_="grid gap-2")[
                            div(class_="flex items-center gap-2")[
                                label_component(for_="demo-card-form-password")["Password"],
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
    )
