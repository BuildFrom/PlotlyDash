from fastapi import FastAPI
from .api import auth, user

def router(app: FastAPI) -> None:
    v1 = "/api/v1"
    app.include_router(auth.router, prefix=v1, tags=["auth"])
    app.include_router(user.router, prefix=v1, tags=["user"])

# http://localhost:9000/api/v1/{route}... WORKS

# Currently, investigating why tags do not work properly
# It could help to achieve this
# http://localhost:9000/api/v1/auth/{route}