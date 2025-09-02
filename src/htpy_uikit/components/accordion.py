from typing import NotRequired, Sequence, TypedDict

from htpy import Node, Renderable, details, h2, p, section, summary

from .icons import icon_chevron_down


class AccordionItem(TypedDict):
    """Option structure for accordion items."""

    title: str
    content: Node | str
    expanded: NotRequired[bool]


def accordion(
    items: Sequence[AccordionItem],
    *,
    default_value: str | None = None,
    class_: str | None = None,
    **attrs,
) -> Renderable:
    """
    Basecoat-style accordion component.

    Based on Basecoat UI accordion implementation.
    Note: Basecoat doesn't have a dedicated accordion component,
    this uses standard HTML details/summary elements with accordion styling.

    Args:
        items: List of AccordionItem dictionaries with title, content, and expanded flag
        default_value: Title of item to expand by default
        class_: Additional CSS classes
        **attrs: Additional HTML attributes

    Returns:
        htpy.section: Accordion component
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
    """Single item accordion."""
    items: list[AccordionItem] = [
        {"title": title, "content": content, "expanded": expanded}
    ]
    return accordion(items, default_value=title if expanded else None, **kwargs)


# Convenience function for FAQ accordion
def accordion_faq(questions_answers: list[tuple[str, str]], **kwargs) -> Renderable:
    """FAQ accordion with questions and answers."""
    items: list[AccordionItem] = [
        {"title": question, "content": p[answer], "expanded": False}
        for question, answer in questions_answers
    ]
    return accordion(items, **kwargs)
