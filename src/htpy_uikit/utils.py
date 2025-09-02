import random
import string


def merge_classes(base_classes: str, class_: str | None = None) -> str:
    """Merge base classes with optional additional classes."""
    if class_:
        return f"{base_classes} {class_}"
    return base_classes


def random_string(n: int) -> str:
    return "".join(random.choices(string.ascii_letters, k=n))
