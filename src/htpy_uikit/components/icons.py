from htpy import Renderable
from htpy import circle
from htpy import div
from htpy import g
from htpy import line
from htpy import path
from htpy import span
from htpy import svg


def icon_send(class_: str = "size-4", **attrs) -> Renderable:
    """Paper-plane / send icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(
            d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"
        ),
        path(d="m21.854 2.147-10.94 10.939"),
    ]


def icon_chevron_right(class_: str = "size-4", **attrs) -> Renderable:
    """Chevron/right arrow icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[path(d="m9 18 6-6-6-6"),]


def icon_chevron_left(class_: str = "size-4", **attrs) -> Renderable:
    """Chevron/left arrow icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[path(d="m15 18-6-6 6-6")]


def icon_arrow_right(class_: str = "size-4", **attrs) -> Renderable:
    """Arrow pointing right: a straight shaft with an arrowhead.

    SVG paths match the provided reference:
    <path d="M5 12h14" />
    <path d="m12 5 7 7-7 7" />
    """
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M5 12h14"),
        path(d="m12 5 7 7-7 7"),
    ]


def icon_spinner(class_: str = "animate-spin size-4", **attrs) -> Renderable:
    """Simple spinner icon (circle + arc) rendered for loading states."""
    # Use the reference spinner made of short stroke segments around the circle.
    return svg(
        class_=f"animate-spin {class_}",
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M12 2v4"),
        path(d="m16.2 7.8 2.9-2.9"),
        path(d="M18 12h4"),
        path(d="m16.2 16.2 2.9 2.9"),
        path(d="M12 18v4"),
        path(d="m4.9 19.1 2.9-2.9"),
        path(d="M2 12h4"),
        path(d="m4.9 4.9 2.9 2.9"),
    ]


def icon_trash(class_: str = "size-4", **attrs) -> Renderable:
    """Trash / delete icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M3 6h18"),
        path(d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6"),
        path(d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2"),
        line(x1="10", x2="10", y1="11", y2="17"),
        line(x1="14", x2="14", y1="11", y2="17"),
    ]


def icon_download(class_: str = "size-4", **attrs) -> Renderable:
    """Download icon (arrow into box)."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"),
        path(d="M7 10l5 5 5-5"),
        path(d="M12 15V3"),
    ]


def icon_upload(class_: str = "size-4", **attrs) -> Renderable:
    """Upload icon (arrow out of box)."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"),
        path(d="M7 10l5-5 5 5"),
        path(d="M12 5v10"),
    ]


def icon_more(class_: str = "size-4", **attrs) -> Renderable:
    """Three dots / more icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        circle(cx="12", cy="12", r="1"),
        circle(cx="19", cy="12", r="1"),
        circle(cx="5", cy="12", r="1"),
    ]


def icon_menu(class_: str = "size-5", **attrs) -> Renderable:
    """Hamburger/menu icon used in mobile nav triggers.

    Matches the previous inline SVG paths: three horizontal lines.
    """
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 17 14",
        fill="none",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_linecap="round",
            stroke_linejoin="round",
            stroke_width="2",
            d="M1 1h15M1 7h15M1 13h15",
        )
    ]


def icon_check(class_: str = "size-4", **attrs) -> Renderable:
    """Checkmark icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[path(d="M20 6L9 17l-5-5"),]


def icon_pencil(class_: str = "size-4", **attrs) -> Renderable:
    """Pencil/edit icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(
            d="m14.304 4.844 2.852 2.852M7 7H4a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1v-4.5m2.409-9.91a2.017 2.017 0 0 1 0 2.853l-6.844 6.844L8 14l.713-3.565 6.844-6.844a2.015 2.015 0 0 1 2.852 0Z",
        )
    ]


def icon_headset(class_: str = "size-4", **attrs) -> Renderable:
    """Headset/support icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="currentColor",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M12 2a7 7 0 0 0-7 7 3 3 0 0 0-3 3v2a3 3 0 0 0 3 3h1a1 1 0 0 0 1-1V9a5 5 0 1 1 10 0v7.083A2.919 2.919 0 0 1 14.083 19H14a2 2 0 0 0-2-2h-1a2 2 0 0 0-2 2v1a2 2 0 0 0 2 2h1a2 2 0 0 0 1.732-1h.351a4.917 4.917 0 0 0 4.83-4H19a3 3 0 0 0 3-3v-2a3 3 0 0 0-3-3 7 7 0 0 0-7-7Zm1.45 3.275a4 4 0 0 0-4.352.976 1 1 0 0 0 1.452 1.376 2.001 2.001 0 0 1 2.836-.067 1 1 0 1 0 1.386-1.442 4 4 0 0 0-1.321-.843Z",
            clip_rule="evenodd",
        )
    ]


def icon_close(class_: str = "size-4", **attrs) -> Renderable:
    """Close/X icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M18 6L6 18"),
        path(d="M6 6l12 12"),
    ]


def icon_search(class_: str = "size-4", **attrs) -> Renderable:
    """Search/magnifying glass icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        circle(cx="11", cy="11", r="8"),
        path(d="m21 21-4.3-4.3"),
    ]


def icon_settings(class_: str = "size-4", **attrs) -> Renderable:
    """Settings/gear icon with text and shortcut indicator."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(
            d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"
        ),
        circle(cx="12", cy="12", r="3"),
    ]


def icon_user(class_: str = "size-4", **attrs) -> Renderable:
    """User/profile icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"),
        path(d="M12 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z"),
    ]


def icon_info(class_: str = "size-4", **attrs) -> Renderable:
    """Info / circled i icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"),
        path(d="M12 16v-4"),
        path(d="M12 8h.01"),
    ]


def icon_circle_check(class_: str = "size-4", **attrs) -> Renderable:
    """Circle with a check mark (success)."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"),
        path(d="m9 12 2 2 4-4"),
    ]


def toast_icon_success(class_: str = "size-4", **attrs) -> Renderable:
    """Success variant icon for toast notifications."""
    return icon_circle_check(class_=class_, **attrs)


def toast_icon_error(class_: str = "size-4", **attrs) -> Renderable:
    """Error variant icon for toast notifications."""
    return icon_circle_alert(class_=class_, **attrs)


def toast_icon_info(class_: str = "size-4", **attrs) -> Renderable:
    """Info variant icon for toast notifications."""
    return icon_info(class_=class_, **attrs)


def icon_circle_alert(class_: str = "size-4", **attrs) -> Renderable:
    """Circle with alert (exclamation) for destructive/error."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"),
        path(d="M12 8v4"),
        path(d="M12 16h.01"),
    ]


def icon_chevron_down(class_: str = "size-4", **attrs) -> Renderable:
    """Chevron/down icon used in accordions (rotates when open)."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[path(d="m6 9 6 6 6-6")]


def icon_chevrons_up_down(class_: str = "size-4", **attrs) -> Renderable:
    """Chevrons up and down icon used in comboboxes/dropdowns."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="m7 15 5 5 5-5"),
        path(d="m7 9 5-5 5 5"),
    ]


def icon_credit_card(class_: str = "size-4", **attrs) -> Renderable:
    """Credit card icon for Billing items."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M2 7h20v10a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2z"),
        path(d="M2 10h20"),
        path(d="M6 15h4"),
    ]


def icon_bar(class_: str = "size-4", **attrs) -> Renderable:
    """Bar chart / histogram icon used in the select demo."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M3 3v16a2 2 0 0 0 2 2h16"),
        path(d="M7 16h8"),
        path(d="M7 11h12"),
        path(d="M7 6h3"),
    ]


def icon_line(class_: str = "size-4", **attrs) -> Renderable:
    """Line chart / sparkline icon used in the select demo."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M3 3v16a2 2 0 0 0 2 2h16"),
        path(d="m19 9-5 5-4-4-3 3"),
    ]


def icon_pie(class_: str = "size-4", **attrs) -> Renderable:
    """Pie chart icon used in the select demo."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(
            d="M21 12c.552 0 1.005-.449.95-.998a10 10 0 0 0-8.953-8.951c-.55-.055-.998.398-.998.95v8a1 1 0 0 0 1 1z"
        ),
        path(d="M21.21 15.89A10 10 0 1 1 8 2.83"),
    ]


def icon_logout(class_: str = "size-4", **attrs) -> Renderable:
    """Logout/exit icon."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"),
        path(d="m16 17 5-5-5-5"),
        path(d="M21 12H9"),
    ]


def icon_double_chevron(class_: str = "size-4", **attrs) -> Renderable:
    """Double chevron icon showing arrows pointing both left and right."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        viewBox="0 0 24 24",
        fill="none",
        stroke="currentColor",
        stroke_width="2",
        stroke_linecap="round",
        stroke_linejoin="round",
        **attrs,
    )[
        path(d="M16 18l6-6-6-6"),
        path(d="M8 6l-6 6 6 6"),
    ]


def icon_moon(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Moon icon for dark mode toggle (dark mode off state)."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewBox="0 0 20 20",
        xmlns="http://www.w3.org/2000/svg",
        **attrs,
    )[path(d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z")]


def icon_sun(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Sun icon for dark mode toggle (dark mode on state)."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewBox="0 0 20 20",
        xmlns="http://www.w3.org/2000/svg",
        **attrs,
    )[
        path(
            d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z",
            fill_rule="evenodd",
            clip_rule="evenodd",
        )
    ]


def icon_eye(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """
    Eye (show password) icon.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG eye icon.
    """
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        fill="none",
        viewBox="0 0 24 24",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_width="2",
            d="M21 12c0 1.2-4.03 6-9 6s-9-4.8-9-6c0-1.2 4.03-6 9-6s9 4.8 9 6Z",
        ),
        path(
            stroke="currentColor",
            stroke_width="2",
            d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z",
        ),
    ]


def icon_eye_off(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """
    Eye-off (hide password) icon.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG eye-off icon.
    """
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        fill="none",
        viewBox="0 0 24 24",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_linecap="round",
            stroke_linejoin="round",
            stroke_width="2",
            d="M3.933 13.909A4.357 4.357 0 0 1 3 12c0-1 4-6 9-6m7.6 3.8A5.068 5.068 0 0 1 21 12c0 1-3 6-9 6-.314 0-.62-.014-.918-.04M5 19 19 5m-4 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z",
        )
    ]


def icon_tag(class_: str = "size-4", **attrs) -> Renderable:
    """
    Tag/flag icon for active data sources.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG tag icon.
    """
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        fill="currentColor",
        viewBox="0 0 24 24",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M3 4a1 1 0 0 0-.822 1.57L6.632 12l-4.454 6.43A1 1 0 0 0 3 20h13.153a1 1 0 0 0 .822-.43l4.847-7a1 1 0 0 0 0-1.14l-4.847-7a1 1 0 0 0-.822-.43H3Z",
            clip_rule="evenodd",
        )
    ]


def icon_plus(class_: str = "size-4", **attrs) -> Renderable:
    """
    Plus/add icon.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG plus icon.
    """
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        fill="none",
        viewBox="0 0 24 24",
        stroke_width="1.5",
        stroke="currentColor",
        **attrs,
    )[
        path(
            stroke_linecap="round",
            stroke_linejoin="round",
            d="M12 4.5v15m7.5-7.5h-15",
        )
    ]


def icon_sort_asc(class_: str = "w-3 h-3", **attrs) -> Renderable:
    """
    Sort ascending arrow icon.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG sort ascending arrow icon.
    """
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        fill="none",
        viewBox="0 0 10 14",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_linecap="round",
            stroke_linejoin="round",
            stroke_width="2",
            d="M5 13V1m0 0L1 5m4-4 4 4",
        )
    ]


def icon_sort_desc(class_: str = "w-3 h-3", **attrs) -> Renderable:
    """
    Sort descending arrow icon.

    Args:
        class_: CSS classes for the SVG element.
        **attrs: Additional SVG attributes.

    Returns:
        Renderable: SVG sort descending arrow icon.
    """
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        fill="none",
        viewBox="0 0 10 14",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_linecap="round",
            stroke_linejoin="round",
            stroke_width="2",
            d="M5 1v12m0 0 4-4m-4 4L1 9",
        )
    ]


def icon_pdf_file(class_: str = "size-4", **attrs) -> Renderable:
    """Small PDF/file icon used in dropzones and file lists."""
    return svg(
        class_=class_,
        aria_hidden="true",
        xmlns="http://www.w3.org/2000/svg",
        width="24",
        height="24",
        fill="none",
        viewBox="0 0 24 24",
        **attrs,
    )[
        path(
            stroke="currentColor",
            stroke_linecap="round",
            stroke_linejoin="round",
            stroke_width="1.2",
            d=(
                "M5 17v-5h1.5a1.5 1.5 0 1 1 0 3H5m12 2v-5h2m-2 3h2M5 10V7.914a1 1 0 0 1 .293-.707"
                "l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1v6M5 19v1a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1v-1M10 3v4a1 1 0 0 1-1 1H5m6 4v5h1.375A1.627 1.627 0 0 0 14 15.375v-1.75A1.627 1.627 0 0 0 12.375 12H11Z"
            ),
        )
    ]


def icon_under_construction(class_: str = "w-10 h-10", **attrs) -> Renderable:
    """Under construction / wrench icon for maintenance pages."""
    return svg(
        class_=class_,
        xmlns="http://www.w3.org/2000/svg",
        viewbox="0 0 512 512",
        **attrs,
    )[
        path(
            fill="currentColor",
            d="M331.8 224.1c28.29 0 54.88 10.99 74.86 30.97l19.59 19.59c40.01-17.74 71.25-53.3 81.62-96.65c5.725-23.92 5.34-47.08 .2148-68.4c-2.613-10.88-16.43-14.51-24.34-6.604l-68.9 68.9h-75.6V97.2l68.9-68.9c7.912-7.912 4.275-21.73-6.604-24.34c-21.32-5.125-44.48-5.51-68.4 .2148c-55.3 13.23-98.39 60.22-107.2 116.4C224.5 128.9 224.2 137 224.3 145l82.78 82.86C315.2 225.1 323.5 224.1 331.8 224.1zM384 278.6c-23.16-23.16-57.57-27.57-85.39-13.9L191.1 158L191.1 95.99l-127.1-95.99L0 63.1l96 127.1l62.04 .0077l106.7 106.6c-13.67 27.82-9.251 62.23 13.91 85.39l117 117.1c14.62 14.5 38.21 14.5 52.71-.0016l52.75-52.75c14.5-14.5 14.5-38.08-.0016-52.71L384 278.6zM227.9 307L168.7 247.9l-148.9 148.9c-26.37 26.37-26.37 69.08 0 95.45C32.96 505.4 50.21 512 67.5 512s34.54-6.592 47.72-19.78l119.1-119.1C225.5 352.3 222.6 329.4 227.9 307zM64 472c-13.25 0-24-10.75-24-24c0-13.26 10.75-24 24-24S88 434.7 88 448C88 461.3 77.25 472 64 472z",
        )
    ]


def icon_flag_en(
    class_: str = "h-3.5 w-3.5 rounded-full me-2", label: str = "English", **attrs
) -> Renderable:
    """US flag icon for English language selection."""
    return div(class_="inline-flex items-center")[
        svg(
            aria_hidden="true",
            class_=class_,
            xmlns="http://www.w3.org/2000/svg",
            id="flag-icon-css-us",
            viewbox="0 0 512 512",
            **attrs,
        )[
            g(fill_rule="evenodd")[
                g(stroke_width="1pt")[
                    path(
                        fill="#bd3d44",
                        d="M0 0h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z",
                        transform="scale(3.9385)",
                    ),
                    path(
                        fill="#fff",
                        d="M0 10h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0zm0 20h247v10H0z",
                        transform="scale(3.9385)",
                    ),
                ],
                path(fill="#192f5d", d="M0 0h98.8v70H0z", transform="scale(3.9385)"),
                path(
                    fill="#fff",
                    d="M8.2 3l1 2.8H12L9.7 7.5l.9 2.7-2.4-1.7L6 10.2l.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7L74 8.5l-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 7.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 24.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 21.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 38.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 35.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 52.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 49.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm-74.1 7l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7H65zm16.4 0l1 2.8H86l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm-74 7l.8 2.8h3l-2.4 1.7.9 2.7-2.4-1.7L6 66.2l.9-2.7-2.4-1.7h3zm16.4 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8H45l-2.4 1.7 1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9zm16.4 0l1 2.8h2.8l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h3zm16.5 0l.9 2.8h2.9l-2.3 1.7.9 2.7-2.4-1.7-2.3 1.7.9-2.7-2.4-1.7h2.9zm16.5 0l.9 2.8h2.9L92 63.5l1 2.7-2.4-1.7-2.4 1.7 1-2.7-2.4-1.7h2.9z",
                    transform="scale(3.9385)",
                ),
            ]
        ],
        span[label],
    ]


def icon_flag_es(
    class_: str = "h-3.5 w-3.5 rounded-full me-2", label: str = "Spanish", **attrs
) -> Renderable:
    """Spanish flag icon for Spanish language selection."""
    return div(class_="inline-flex items-center")[
        svg(
            class_=class_,
            enable_background="new 0 0 512 512",
            viewbox="0 0 512 512",
            xmlns="http://www.w3.org/2000/svg",
            **attrs,
        )[
            path(
                d="m0 256c0 31.314 5.633 61.31 15.923 89.043l240.077 22.261 240.077-22.261c10.29-27.733 15.923-57.729 15.923-89.043s-5.633-61.31-15.923-89.043l-240.077-22.261-240.077 22.261c-10.29 27.733-15.923 57.729-15.923 89.043z",
                fill="#ffda44",
            ),
            g(fill="#d80027")[
                path(
                    d="m496.077 166.957c-36.171-97.484-130.006-166.957-240.077-166.957s-203.906 69.473-240.077 166.957z"
                ),
                path(
                    d="m15.923 345.043c36.171 97.484 130.006 166.957 240.077 166.957s203.906-69.473 240.077-166.957z"
                ),
            ],
        ],
        span[label],
    ]


def icon_social_facebook(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Facebook social media icon."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewbox="0 0 24 24",
        aria_hidden="true",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z",
            clip_rule="evenodd",
        )
    ]


def icon_social_instagram(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Instagram social media icon."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewbox="0 0 24 24",
        aria_hidden="true",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z",
            clip_rule="evenodd",
        )
    ]


def icon_social_twitter(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Twitter social media icon."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewbox="0 0 24 24",
        aria_hidden="true",
        **attrs,
    )[
        path(
            d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84"
        )
    ]


def icon_social_github(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """GitHub social media icon."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewbox="0 0 24 24",
        aria_hidden="true",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z",
            clip_rule="evenodd",
        )
    ]


def icon_social_dribbble(class_: str = "w-5 h-5", **attrs) -> Renderable:
    """Dribbble social media icon."""
    return svg(
        class_=class_,
        fill="currentColor",
        viewbox="0 0 24 24",
        aria_hidden="true",
        **attrs,
    )[
        path(
            fill_rule="evenodd",
            d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z",
            clip_rule="evenodd",
        )
    ]
