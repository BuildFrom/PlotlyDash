import os
import flask
import dash
import numpy as np
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output
from app.components import Layout, Card, Footer

def plotly() -> dash.Dash:
    
    app = dash.Dash(
        __name__, 
        title="Dash App",
        server=flask.Flask(__name__), 
        # make sure to change `assets_folder` if needed.
        # because my file is within notebooks folder, I had to change path to `../assets`
        external_stylesheets = [{
            'href': 'assets/css/output.css',
            'rel': 'stylesheet',
        }]
    )

    firstNewComponent = html.P(
        "First paragraph component",
    )

    secondNewComponent = html.P(
        "Second paragraph component",
    )

    app.layout = html.Div([
        Layout([
            Card(
                title="First Title",
                description="First Description",
                paragraph=firstNewComponent,
                width="w-full lg:w-3/4"
            ),
            Card(
                title="Second Title",
                description="Second Description",
                paragraph=secondNewComponent,
                width="w-full lg:w-1/4"
            ),
            Footer()
        ])
    ])

    return app