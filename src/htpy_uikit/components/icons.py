from htpy import Renderable
from htpy import circle
from htpy import line
from htpy import path
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
