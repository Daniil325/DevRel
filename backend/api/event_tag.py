from typing import Annotated
from fastapi import APIRouter, Depends
from backend.schemas.event_tag import EventTagSchemaAdd
from backend.services.event_tag import EventTagService
from backend.api.dependencies import event_tag_service

router = APIRouter(prefix='/event_tag', tags=['EventsTag'])


@router.get('/')
async def list_event_tags(
        service: Annotated[EventTagService, Depends(event_tag_service)],
):
    events = await service.get_event_tags()
    return events


@router.post('/')
async def post_tag(
        event: EventTagSchemaAdd,
        service: Annotated[EventTagService, Depends(event_tag_service)],
):
    event_id = await service.add_event(event)
    return {"event_id": event_id}
