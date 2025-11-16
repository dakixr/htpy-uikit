import random
import string


def merge_classes(base_classes: str, class_: str | None = None) -> str:
    """Merge ``base_classes`` with optional ``class_`` string.

    Args:
        base_classes: Default Tailwind utility classes.
        class_: Optional user-supplied classes appended to the base.

    Returns:
        str: Combined class string without extra whitespace.
    """
    if class_:
        return f"{base_classes} {class_}"
    return base_classes


def random_string(n: int) -> str:
    """Return a pseudo-random alpha string of length ``n``.

    Args:
        n: Desired number of characters.

    Returns:
        str: Random uppercase/lowercase ASCII letters combined via ``random.choices``.
    """

    return "".join(random.choices(string.ascii_letters, k=n))
