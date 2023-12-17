from typing import Annotated
from fastapi import APIRouter, Depends, Query

from backend.schemas.event import EventSchemaAdd
from backend.services.event import EventService
from backend.api.dependencies import event_service

router = APIRouter(prefix='/event', tags=['Events'])


@router.get('/')
async def list_events(
        event_service: Annotated[EventService, Depends(event_service)],
        order: str = 'ASC',
        filter_tag: list = Query(None),
        filter_date: list = Query(None),
        search: str = None
):
    events = await event_service.get_all(order, filter_tag, filter_date, search)
    return events


@router.post('/')
async def post_tag(
        event: EventSchemaAdd,
        event_service: Annotated[EventService, Depends(event_service)],
):
    event_id = await event_service.add_event(event)
    return {"event_id": event_id}


@router.get('/{event_id}')
async def list_event(
        event_id: int,
        event_service: Annotated[EventService, Depends(event_service)]
):
    event = await event_service.get_event(event_id)
    return event
