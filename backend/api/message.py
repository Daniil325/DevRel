from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends

from backend.schemas.message import MessageSchemaAdd
from backend.services.message import MessageService
from backend.api.dependencies import message_service

router = APIRouter(prefix='/message', tags=['Messages'])


@router.get('/')
async def list_messages(
        messages_service: Annotated[MessageService, Depends(message_service)],
):
    messages = await messages_service.get_messages()
    return messages


@router.post('/')
async def post_message(
        message: MessageSchemaAdd,
        messages_service: Annotated[MessageService, Depends(message_service)],
):
    message_id = await messages_service.add_message(message)
    return {"message_id": message_id}


@router.get('/{from_user_id}/{to_user_id}')
async def get_last_message(
        messages_service: Annotated[MessageService, Depends(message_service)],
        from_user_id: int = None,
        to_user_id: int = None,
        last_time: datetime = None
):
    messages = await messages_service.get_last_message(from_user_id, to_user_id, last_time)
    return messages
