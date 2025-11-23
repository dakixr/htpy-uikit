from htpy import Node

from htpy_uikit.components.accordion import accordion

from ._utils import _demo_section


def accordion_section() -> Node:
    return _demo_section(
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
    )
