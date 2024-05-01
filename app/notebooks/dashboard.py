import flask
import dash
from dash import html
from app.components import Layout, Card, Footer
from .figures import tweak_alta as snowFigure


def plotly() -> dash.Dash:
    app = create_dash()
    app.layout = provider()
    return app


def provider():
    return html.Div(
        [
            Layout(
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
                    Footer(
                        brand="Brand",
                        docs_url="https://dash.plotly.com/dash-html-components",
                    ),
                ]
            )
        ]
    )


def create_dash():
    app = dash.Dash(
        __name__,
        title="Dash App",
        server=flask.Flask(__name__),
        assets_folder="../assets",
        external_stylesheets=[
            {
                "href": "assets/css/output.css",
                "rel": "stylesheet",
            }
        ],
    )
    return app
