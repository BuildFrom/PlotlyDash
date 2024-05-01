from fastapi import APIRouter, Depends, HTTPException, Request
from typing import List
from app.lib import response, error

router = APIRouter()


@router.get("/users")
async def get_users():
    users = "User"
    if not users:
        error(404, "No users found")
    return response(users, 200)
