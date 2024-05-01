from dash import html, dcc


def Footer(brand, docs_url):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(brand, className="text-primary"),
                ],
                className="px-3 flex space-x-1.5 items-center",
            ),
            dcc.Link(
                [
                    html.Div("Documentation", className="text-primary"),
                ],
                href=docs_url,
                refresh=True,
                className="px-3 flex space-x-1.5 items-center",
            ),
        ],
        className="pt-40 flex items-center justify-between text-sm",
    )
