import dash
from dash import html
from app.lib import Card, tweak_alta as snowFigure

dash.register_page(__name__)

layout = html.Div(
    [
        Card(
            title="First Title",
            badge=["badge"],
            description="First Description",
            content=html.P("First content component"),
            width="w-full lg:w-3/4",
        ),
        Card(
            title="Second Title",
            badge=["alpha"],
            description="Second Description",
            content=html.P("Second paragraph component"),
            width="w-full lg:w-1/4",
        ),
        Card(
            title="2011 Season Snow Depth",
            badge="",
            description="Third Description",
            content=snowFigure(),
            width="w-full",
        ),
    ]
)
