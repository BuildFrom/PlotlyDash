import dash
from dash import html
from app.lib import Card, tweak_alta as snowFigure

dash.register_page(__name__)

layout = html.Div(
    [
        Card(
            title="First Title",
            description="First Description",
            content=html.P("First content component"),
            width="w-full lg:w-3/4",
        ),
        Card(
            title="Second Title",
            description="Second Description",
            content=html.P("Second paragraph component"),
            width="w-full lg:w-1/4",
        ),
        Card(
            title="2011 Season Snow Depth",
            description="Third Description",
            content=snowFigure(),
            width="w-full",
        ),
    ]
)
