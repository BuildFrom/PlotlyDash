from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from app.notebooks import plotly

def create_app():
    app = FastAPI()
    app.mount("/", WSGIMiddleware(plotly().server))
    return app

if __name__ == '__main__':
    create_app()