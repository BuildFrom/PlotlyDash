import dash
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.lib import Layout, Footer

# ==============================

def create_app():
    app = FastAPI()
    app.mount("/", WSGIMiddleware(create_dash().server))
    return app

# ==============================

def create_dash() -> dash.Dash:
    app = dash.Dash(
        __name__,
        title="Dash App",
        assets_folder="lib/assets",
        pages_folder="routes",
        use_pages=True,
        external_stylesheets=[
            {
                "href": "assets/css/output.css",
                "rel": "stylesheet",
            }
        ],
    )
    app.layout = Layout(
        [
            dash.page_container,
            Footer(
                brand="Brand",
                docs_url="https://dash.plotly.com/dash-html-components",
            ),
        ]
    )
    return app


# ==============================

if __name__ == "__main__":
    create_app()
