from htpy import Node, div

from htpy_uikit.components.avatar import avatar, avatar_group, avatar_text

from ._utils import _demo_section


def avatar_section() -> Node:
    return _demo_section(
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
    )
