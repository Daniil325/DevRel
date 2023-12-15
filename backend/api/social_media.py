from typing import Annotated
from fastapi import APIRouter, Depends
from backend.schemas.social_media import SocialMediaSchemaAdd
from backend.services.social_media import SocialMediaService
from backend.api.dependencies import social_media_service

router = APIRouter(prefix='/social_media', tags=['SocialMedia'])


@router.get('/')
async def list_social_medias(
        social_media_service: Annotated[SocialMediaService, Depends(social_media_service)],
):
    events = await social_media_service.get_social_media()
    return events


@router.post('/')
async def post_social_media(
        event: SocialMediaSchemaAdd,
        social_media_service: Annotated[SocialMediaService, Depends(social_media_service)],
):
    event_id = await social_media_service.add_event(event)
    return {"event_id": event_id}
