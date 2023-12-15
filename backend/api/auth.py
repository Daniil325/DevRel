from typing import Annotated
from fastapi_users import FastAPIUsers
from fastapi import Depends, APIRouter
from backend.auth.auth import auth_backend
from backend.db.db import User
from backend.auth.manager import get_user_manager
from backend.api.dependencies import user_service
from backend.services.user import AuthService


router = APIRouter(prefix='/auth', tags=['auth'])


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


@router.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@router.get("/unprotected-route")
def unprotected_route():
    return f"Hello, anonym"
