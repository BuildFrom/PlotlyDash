from dash import html, dcc

def Footer():
    return html.Div(
        [
            html.Div(
                [
                    html.Div("Data Collab", className="text-primary"),
                ],
                className="px-3 flex space-x-1.5 items-center",
            ),
            dcc.Link(
                [
                    html.Div("Source Code", className="text-primary"),
                ],
                href="https://github.com/BuildFrom/PlotlyDash",
                refresh=True,
                className="px-3 flex space-x-1.5 items-center",
            ),
        ],
        className="pt-40 flex items-center justify-between text-sm")
