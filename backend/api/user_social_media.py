from typing import Annotated
from fastapi import APIRouter, Depends

from backend.schemas.user_social_media import UserSocialMediaSchemaAdd
from backend.services.user_social_media import UserSocialMediaService
from backend.api.dependencies import user_social_media_service

router = APIRouter(prefix='/user_social_media', tags=['UserSocialMedia'])


@router.get('/')
async def list_tag(
        service: Annotated[UserSocialMediaService, Depends(user_social_media_service)],
):
    tags = await service.get_list()
    return tags


@router.post('/')
async def post_tag(
        tag: UserSocialMediaSchemaAdd,
        service: Annotated[UserSocialMediaService, Depends(user_social_media_service)],
):
    tag_id = await service.add_item(tag)
    return {"tag_id": tag_id}
