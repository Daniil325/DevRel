from typing import Annotated
from fastapi import APIRouter, Depends

from backend.schemas.event import EventSchemaAdd
from backend.services.event import EventService
from backend.api.dependencies import event_service

router = APIRouter(prefix='/event', tags=['Events'])


@router.get('/')
async def list_events(
        event_service: Annotated[EventService, Depends(event_service)],
):
    events = await event_service.get_tags()
    return events


@router.post('/')
async def post_tag(
        event: EventSchemaAdd,
        event_service: Annotated[EventService, Depends(event_service)],
):
    event_id = await event_service.add_event(event)
    return {"event_id": event_id}
