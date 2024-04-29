# type: ignore
import os
import flask
import dash
import numpy as np
import pandas as pd
import plotly.express as px

from dash import dcc, html, Input, Output
from app.components import Layout, Card

def plotly() -> dash.Dash:
    """
    Sample Dash application from Plotly: https://github.com/plotly/dash-hello-world/blob/master/app.py
    """
    server = flask.Flask(__name__)

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')
    
    tailwind = [{'src': 'https://cdn.tailwindcss.com'}]
    app = dash.Dash(__name__, server=server, external_scripts=tailwind)

    app.scripts.config.serve_locally = False
    dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

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
        ])
    ])

    @app.callback(Output('my-graph', 'figure'),
                  [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        dff = df[df['Stock'] == selected_dropdown_value]
        return {
            'data': [{
                'x': dff.Date,
                'y': dff.Close,
                'line': {
                    'width': 3,
                    'shape': 'spline'
                }
            }],
            'layout': {
                'margin': {
                    'l': 30,
                    'r': 20,
                    'b': 30,
                    't': 20
                }
            }
        }

    return app


# from dash.dependencies import Input, Output
# from dash import dcc, html
