from typing import Annotated
from fastapi import APIRouter, Depends

from backend.api.auth import current_user
from backend.db.db import User
from backend.schemas.user_event import UserEventSchemaAdd
from backend.services.user_event import UserEventService
from backend.api.dependencies import user_event_service

router = APIRouter(prefix='/user_event', tags=['UserEvent'])


@router.post('/')
async def post_review(
        item: UserEventSchemaAdd,
        service: Annotated[UserEventService, Depends(user_event_service)],
        user: User = Depends(current_user)
):
    post_id = await service.add_item(item)
    return {"post_id": post_id}


@router.get('/user/{user_id}')
async def list_review(
        user_id: int,
        service: Annotated[UserEventService, Depends(user_event_service)],
):
    res = await service.get_by_user(user_id)
    return res


@router.get('/event/{event_id}')
async def list_review(
        event_id: int,
        service: Annotated[UserEventService, Depends(user_event_service)],
):
    res = await service.get_by_event(event_id)
    return res
