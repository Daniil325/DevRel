from typing import Annotated
from fastapi import APIRouter, Depends

from backend.schemas.tag import TagSchemaAdd, TagSchemaUpdate
from backend.services.tag import TagService
from backend.api.dependencies import tag_service

router = APIRouter(prefix='/tag', tags=['Tags'])


@router.get('/')
async def list_tag(
        service: Annotated[TagService, Depends(tag_service)],
):
    tags = await service.get_tags()
    return tags


@router.get('/{id}')
async def get_tag(
        service: Annotated[TagService, Depends(tag_service)],
        id: int
):
    tags = await service.get_by_id(id)
    return tags


@router.post('/')
async def post_tag(
        tag: TagSchemaAdd,
        service: Annotated[TagService, Depends(tag_service)],
):
    tag_id = await service.add_tag(tag)
    return {"tag_id": tag_id}


@router.put('/{id}')
async def post_tag(
        tag: TagSchemaUpdate,
        service: Annotated[TagService, Depends(tag_service)],
        id: int
):
    tag_id = await service.update_tag(tag, id)
    return {"tag_id": tag_id}

