from pymx.elements import (
    a,
    b,
    button,
    div,
    i,
    input,
    label,
    p,
    table,
    tbody,
    td,
    th,
    thead,
    tr,
)
from pymx.elements.base import Safe
from pymx.elements.css import CSSProperties


def test_paragraph():
    paragraph = p(
        Safe(f"Hello, World! {b("Something bold")} and {i("Something italic")}")
    )
    assert paragraph.to_html() == (
        "<p>Hello, World! <b>Something bold</b> and <i>Something italic</i></p>"
    )


def test_html_link():
    link = a("A link!", href="https://example.com")
    assert link.to_html() == '<a href="https://example.com">A link!</a>'


def test_table():
    dom = table(
        thead(
            tr(
                th("Header 1"),
                th("Header 2"),
                th("Header 3"),
            )
        ),
        tbody(
            tr(
                td("Cell 1", style=CSSProperties(color="red", height="100px")),
                td("Cell 2"),
                td("Cell 3"),
            ),
        ),
    )

    assert dom.to_html() == (
        "<table>"
            "<thead>"
                "<tr>"
                    "<th>Header 1</th>"
                    "<th>Header 2</th>"
                    "<th>Header 3</th>"
                "</tr>"
            "</thead>"
            "<tbody>"
                "<tr>"
                    '<td style="color:red;height:100px">Cell 1</td>'
                    "<td>Cell 2</td>"
                    "<td>Cell 3</td>"
                "</tr>"
            "</tbody>"
        "</table>"
    )  # fmt: skip


def test_button_get():
    dom = div(
        div(label("First Name"), ": Joe"),
        div(label("Last Name"), ": Blow"),
        div(label("Email"), ": joe@blow.com"),
        button(
            "Click To Edit",
            class_="btn btn-primary",
            hx_get="/contact/1/edit",
        ),
        hx_target="this",
        hx_swap="outerHTML",
    )

    assert isinstance(dom.children[3], button)
    assert dom.children[3].attrs.get("hx_get") == "/contact/1/edit"
    assert dom.children[3].children[0] == "Click To Edit"
    assert dom.attrs.get("hx_target") == "this"
    assert dom.to_html() == (
        '<div hx-target="this" hx-swap="outerHTML">'
            "<div><label>First Name</label>: Joe</div>"
            "<div><label>Last Name</label>: Blow</div>"
            "<div><label>Email</label>: joe@blow.com</div>"
            '<button class="btn btn-primary" hx-get="/contact/1/edit">'
                "Click To Edit"
            "</button>"
        "</div>"
    )  # fmt: skip


def test_alternative_attributes():
    dom = div(
        label("First Name", **{"for": "first_name", "name": "first_name"}),
        input(**{"class": "form-control", "id": "first_name", "name": "first_name"}),
        button(
            "Click To Edit", **{"class": "btn btn-primary", "hx-get": "/contact/1/edit"}
        ),
        **{"hx-target": "this", "hx-swap": "outerHTML"},
    )

    assert dom.to_html() == (
        '<div hx-target="this" hx-swap="outerHTML">'
            '<label for="first_name" name="first_name">First Name</label>'
            '<input class="form-control" id="first_name" name="first_name" />'
            '<button class="btn btn-primary" hx-get="/contact/1/edit">'
                "Click To Edit"
            "</button>"
        "</div>"
    )  # fmt: skip
