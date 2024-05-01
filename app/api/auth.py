from fastapi import APIRouter, Request
from app.lib import response, error, BCRYPT_CONTEXT

router = APIRouter()

# async def func(
#     request: Request,
#     db=Depends(get_db),
#     secure=Depends(protected_route)
# ):

@router.post("/register")
async def register_user():
    data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "test_password"
    }
    return response(data, 200)



@router.post("/login")
async def login_user():
    data = "await request.json()"
    form_data = "User(**data)"
    user = "User(**result)"

    if not user:
        error(404, "User not found")

    if not BCRYPT_CONTEXT.verify(form_data.password, user.password):
        error(401, "Unauthorized")

    return response("Login User", 200)


@router.post("/logout")
async def logout_user():
    return response("Logout User", 200)
