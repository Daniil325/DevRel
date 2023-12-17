from fastapi import FastAPI

from backend.api.auth import fastapi_users
from backend.api.tag import router as tag_router
from backend.api.event import router as event_router
from backend.api.event_tag import router as event_tag_router
from backend.api.review import router as review_router
from backend.api.auth import router as auth_router
from backend.api.social_media import router as social_media_router
from backend.api.status import router as status_router
from backend.api.user_social_media import router as user_social_media_router
from backend.api.user_event import router as user_event_router
from backend.api.message import router as message_router
from backend.auth.auth import auth_backend
from backend.schemas.auth import UserRead, UserCreate

app = FastAPI()

app.include_router(tag_router)
app.include_router(event_router)
app.include_router(event_tag_router)
app.include_router(social_media_router)
app.include_router(status_router)
app.include_router(review_router)
app.include_router(user_social_media_router)
app.include_router(user_event_router)
app.include_router(auth_router)
app.include_router(message_router)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

