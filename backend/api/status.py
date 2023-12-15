from typing import Annotated
from fastapi import APIRouter, Depends
from backend.schemas.status import StatusSchemaAdd
from backend.services.status import StatusService
from backend.api.dependencies import status_service

router = APIRouter(prefix='/status', tags=['Status'])


@router.get('/')
async def list_status(
        service: Annotated[StatusService, Depends(status_service)],
):
    events = await service.get_status()
    return events


@router.post('/')
async def post_tag(
        event: StatusSchemaAdd,
        service: Annotated[StatusService, Depends(status_service)],
):
    event_id = await service.add_status(event)
    return {"event_id": event_id}
