import dash
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.wsgi import WSGIMiddleware
from app.blueprint import router
from app.lib import Layout, Footer
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

# ==============================


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    router(app)

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(404)
    async def not_found_handler(request, exc):
        return JSONResponse(
            status_code=404,
            content={"message": "Not Found"},
        )

    app.mount("/", WSGIMiddleware(create_dash().server))
    
    return app


# ==============================


def create_dash() -> dash.Dash:
    app = dash.Dash(
        __name__,
        title="Dash App",
        assets_folder="lib/assets",
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
