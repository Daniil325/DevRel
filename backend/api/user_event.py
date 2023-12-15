from typing import Annotated
from fastapi import APIRouter, Depends

from backend.api.auth import current_user
from backend.db.db import User
from backend.schemas.user_event import UserEventSchemaAdd
from backend.services.user_event import UserEventService
from backend.api.dependencies import user_event_service

router = APIRouter(prefix='/user_event', tags=['UserEvent'])


@router.get('/')
async def list_review(
        service: Annotated[UserEventService, Depends(user_event_service)],
        user: User = Depends(current_user)
):

    res = await service.get_by_user(user.id)
    return res


@router.post('/')
async def post_review(
        item: UserEventSchemaAdd,
        service: Annotated[UserEventService, Depends(user_event_service)],
        user: User = Depends(current_user)
):
    post_id = await service.add_item(item)
    return {"post_id": post_id}
