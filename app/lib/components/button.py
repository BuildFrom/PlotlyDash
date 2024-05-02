# Design in progress

from dash import html


def Button(btn):
    return html.Button(
        [btn],
        className="bg-primary text-secondary rounded-md absolute left-1/2 top-1/2 size-[max(100%,2.75rem)] -translate-x-1/2 -translate-y-1/2 relative isolate inline-flex items-center justify-center gap-x-2 p-2 rounded-lg border text-base/6 font-semibold [@media(pointer:fine)]:hidden ",
    )
