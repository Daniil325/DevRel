from typing import Annotated
from fastapi import APIRouter, Depends

from backend.api.auth import current_user
from backend.db.db import User
from backend.schemas.review import ReviewSchemaAdd
from backend.services.review import ReviewService
from backend.api.dependencies import review_service

router = APIRouter(prefix='/review', tags=['Review'])


@router.get('/')
async def list_review(
        service: Annotated[ReviewService, Depends(review_service)],
):
    res = await service.get_list()
    return res


@router.post('/')
async def post_review(
        item: ReviewSchemaAdd,
        service: Annotated[ReviewService, Depends(review_service)],
        user: User = Depends(current_user)
):
    post_id = await service.add_item(item)
    return {"post_id": post_id}
