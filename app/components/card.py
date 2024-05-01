from dash import html


def Card(title, description, content, width="w-full"):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H1(
                                title,
                                className="text-4xl font-bold tracking-tight text-primary sm:text-5xl",
                            ),
                            html.H2(
                                description,
                                className="mt-6 text-base text-muted-foreground",
                            ),
                            html.Div(
                                [
                                    html.P(
                                        content,
                                        className="text-secondary-foreground mt-5",
                                    ),
                                ],
                                className="bg-secondary p-2 rounded-xl",
                            ),
                        ],
                        className="lg:order-first lg:row-span-2",
                    ),
                ],
                className="bg-card rounded-xl p-2",
            ),
        ],
        className=f"p-2 inline-block {width}",
    )
