from dash import html

def Layout(children=None):
    return html.Div([
        html.Div([
            html.Nav([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Div([
                                html.Div([
                                    html.Img(
                                        src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500",
                                        className="h-8 w-8"
                                    )
                                ], className="flex-shrink-0"),
                                html.Div([
                                    html.Div([
                                        html.A(
                                            "Home",
                                            href="/",
                                            className="bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium"
                                        )
                                    ], className="ml-10 flex items-baseline space-x-4")

                                ], className="hidden md:block")
                            ], className="flex items-center"),
                            # TODO: Add Open/Close Menu
                        ], className="flex h-16 items-center justify-between px-4 sm:px-0")
                    ], className="border-b border-gray-700")
                ], className="mx-auto max-w-7xl sm:px-6 lg:px-8"),
                html.Div([
                    html.Div([
                        html.A(
                            "Home",
                            href="/",
                            className="bg-gray-900 text-white rounded-md px-3 py-2 text-sm font-medium"
                        )
                    ], className="space-y-1 px-2 py-3 sm:px-3")
                ], className="border-b border-gray-700 md:hidden"),
            ], className="bg-gray-800"),
            html.Header([
                html.Div([
                    html.H1([
                        "Plotly Dash"
                    ], className="text-3xl font-bold tracking-tight text-white")
                ], className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8")
            ], className="py-10")
        ], className="bg-gray-800 pb-32"),
        html.Main([
            html.Div(
                children=children,
                className="bg-orange-50 rounded-xl mx-auto max-w-7xl pb-12 p-2")
        ], className="-mt-32 m-3.5")
    ], className="min-h-full")

        # html.H1('Stock Tickers'),
        # dcc.Dropdown(
        #     id='my-dropdown',
        #     options=[
        #         {'label': 'Tesla', 'value': 'TSLA'},
        #         {'label': 'Apple', 'value': 'AAPL'},
        #         {'label': 'Coke', 'value': 'COKE'}
        #     ],
        #     value='TSLA'
        # ),
        # dcc.Graph(id='my-graph')

# def Layout():
#     return html.Div([
        # html.H1('Stock Tickers'),
        # dcc.Dropdown(
        #     id='my-dropdown',
        #     options=[
        #         {'label': 'Tesla', 'value': 'TSLA'},
        #         {'label': 'Apple', 'value': 'AAPL'},
        #         {'label': 'Coke', 'value': 'COKE'}
        #     ],
        #     value='TSLA'
        # ),
        # dcc.Graph(id='my-graph')
#     ], className="container")