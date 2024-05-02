from dash import html


def Badge(tags):
    return html.Div(
        [
            html.Span(
                tag,
                className="inline-flex bg-primary text-secondary rounded-md px-2 py-0.5 items-center",
            )
            for tag in tags
        ],
        className="space-x-1.5",
    )