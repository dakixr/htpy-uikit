from typing import Sequence

from htpy import Node
from htpy import Renderable
from htpy import details
from htpy import h2
from htpy import p
from htpy import section
from htpy import summary

from ._types import AccordionItem
from .icons import icon_chevron_down


def accordion(
    items: Sequence[AccordionItem],
    *,
    default_value: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """Render a Basecoat-style accordion using native ``<details>`` elements.

    Args:
        items: Sequence of accordion item definitions containing ``title`` and ``content``.
        default_value: Title whose panel should be expanded initially.
        class_: Additional CSS classes appended to the wrapping section.
        **attrs: Extra HTML attributes forwarded to the section element.

    Returns:
        Renderable: Section element containing the accordion items.
    """

    # Add class to attrs
    attrs["class_"] = class_

    # Build accordion items using AccordionItem dictionaries
    accordion_items: list[Renderable] = []

    # Determine initial open index for Alpine state
    initial_active_index: int | None = None

    total = len(items)
    for idx, item in enumerate(items):
        title = item["title"]
        content = item["content"]
        expanded_flag = item.get("expanded", False)

        is_expanded = bool(expanded_flag) or (title == default_value)
        if is_expanded and initial_active_index is None:
            initial_active_index = idx

        if isinstance(content, str):
            content_node = p(class_="text-sm")[content]
        else:
            content_node = content

        section_attrs = {"class_": "pb-4"} if idx != total - 1 else {}

        item = details(
            {":open": f"active === {idx}"},
            class_="group border-b border-border last:border-b-0",
        )[
            summary(
                {"@click.prevent": f"active = active === {idx} ? null : {idx}"},
                class_=(
                    "w-full focus-visible:border-ring focus-visible:ring-ring/50 "
                    "focus-visible:ring-[3px] transition-all outline-none rounded-md list-none"
                ),
                style="list-style: none;",
            )[
                h2(
                    class_=(
                        "flex flex-1 items-start justify-between gap-4 py-4 text-left text-sm "
                        "font-medium hover:underline cursor-pointer"
                    ),
                )[
                    title,
                    icon_chevron_down(
                        class_=(
                            "text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 "
                            "transition-transform duration-200 group-open:rotate-180"
                        )
                    ),
                ]
            ],
            section(**section_attrs)[content_node],
        ]

        accordion_items.append(item)

    # Alpine x-data state for single-open behavior
    initial_js = "null" if initial_active_index is None else str(initial_active_index)
    alpine_attrs = {"x-data": f"{{active: {initial_js}}}"}

    return section(alpine_attrs, **attrs)[*accordion_items]


# Convenience function for single item accordion
def accordion_single(
    title: str, content: Node | str, expanded: bool = False, **kwargs
) -> Renderable:
    """Render a one-item accordion helper.

    Args:
        title: Accordion heading.
        content: Body content node or string.
        expanded: Whether the single item starts open.
        **kwargs: Additional keyword arguments forwarded to ``accordion``.

    Returns:
        Renderable: Section element wrapping the single accordion entry.
    """
    items: list[AccordionItem] = [{"title": title, "content": content, "expanded": expanded}]
    return accordion(items, default_value=title if expanded else None, **kwargs)


# Convenience function for FAQ accordion
def accordion_faq(questions_answers: list[tuple[str, str]], **kwargs) -> Renderable:
    """Render an FAQ-style accordion.

    Args:
        questions_answers: Sequence of (question, answer) tuples.
        **kwargs: Additional keyword arguments forwarded to ``accordion``.

    Returns:
        Renderable: Section element containing an accordion with FAQ entries.
    """
    items: list[AccordionItem] = [
        {"title": question, "content": p[answer], "expanded": False}
        for question, answer in questions_answers
    ]
    return accordion(items, **kwargs)
