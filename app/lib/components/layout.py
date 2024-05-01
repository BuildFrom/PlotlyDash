from dash import html, dcc


def Layout(children=None):
    return html.Div(
        [
            html.Div(
                [
                    html.Nav(
                        [
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.Div(
                                                [
                                                    html.Div(
                                                        [
                                                            html.Div(
                                                                [
                                                                    html.Img(
                                                                        src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500",
                                                                        className="h-8 w-8",
                                                                    )
                                                                ],
                                                                className="flex-shrink-0",
                                                            ),
                                                            html.Div(
                                                                [
                                                                    html.Nav(
                                                                        [
                                                                            dcc.Link(
                                                                                html.A(
                                                                                    "Home",
                                                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                                                ),
                                                                                href="/",
                                                                            ),
                                                                            dcc.Link(
                                                                                html.A(
                                                                                    "Analytics",
                                                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                                                ),
                                                                                href="/analytics",
                                                                            ),
                                                                            dcc.Link(
                                                                                html.A(
                                                                                    "Dashboard",
                                                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                                                ),
                                                                                href="/dashboard",
                                                                            ),
                                                                        ],
                                                                        className="ml-10 flex items-baseline space-x-4",
                                                                    ),
                                                                ],
                                                                className="hidden md:block",
                                                            ),
                                                        ],
                                                        className="flex items-center",
                                                    ),
                                                    # TODO: Attempted to create Menu button 💀
                                                    # html.Button([
                                                    #     html.Img(
                                                    #         src="assets/icons/menu.svg",
                                                    #         className="h-8 w-8"
                                                    #     ),
                                                    # ], id="menu-btn", className="md:hidden")
                                                ],
                                                className="flex h-16 items-center justify-between px-4 sm:px-0",
                                            )
                                        ],
                                        className="",
                                    )  # border-b border-primary
                                ],
                                className="mx-auto max-w-7xl sm:px-6 lg:px-8",
                            ),
                            html.Div(
                                [
                                    html.Nav(
                                        [
                                            dcc.Link(
                                                html.A(
                                                    "Home",
                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                ),
                                                href="/",
                                            ),
                                            dcc.Link(
                                                html.A(
                                                    "Analytics",
                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                ),
                                                href="/analytics",
                                            ),
                                            dcc.Link(
                                                html.A(
                                                    "Dashboard",
                                                    className="bg-secondary text-primary rounded-md px-3 py-2 text-sm font-medium",
                                                ),
                                                href="/dashboard",
                                            ),
                                        ],
                                        className="space-y-1 space-x-4 px-2 py-3 sm:px-3 md:hidden",
                                    ),
                                ],
                                className="bg-primary",
                            ),
                        ],
                        className="bg-primary",  # border-b border-primary
                    ),
                    html.Header(
                        [
                            html.Div(
                                [
                                    html.H1(
                                        ["Plotly Dash"],
                                        className="text-3xl font-bold tracking-tight text-secondary",
                                    )
                                ],
                                className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8",
                            )
                        ],
                        className="py-10",
                    ),
                ],
                className="bg-primary pb-32",
            ),
            html.Main(
                [
                    html.Div(
                        children=children,
                        className="bg-accent rounded-xl mx-auto max-w-7xl pb-12 p-2",
                    )
                ],
                className="-mt-32 m-3.5",
            ),
        ],
        className="min-h-full",
    )
