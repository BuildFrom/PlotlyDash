from dash import html

def Card(title, description, paragraph, width="w-full"):
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H1(
                                title,
                                className="text-4xl font-bold tracking-tight text-zinc-100 sm:text-5xl",
                            ),
                            html.H2(
                                description,
                                className="mt-6 text-base text-zinc-400",
                            ),
                            html.Div(
                                [
                                    html.P(
                                        paragraph,
                                        className="text-zinc-400 mt-5 p-2",
                                    ),
                                ],
                                className="bg-white rounded-xl",
                            ),
                        ],
                        className="lg:order-first lg:row-span-2",
                    ),
                ],
                className="bg-black rounded-xl p-2",
            ),
        ],
        className=f"p-2 inline-block {width}",
    )
