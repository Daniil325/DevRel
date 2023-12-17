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
