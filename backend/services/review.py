from datetime import datetime

from backend.schemas.review import ReviewSchemaAdd
from backend.utils.repository import AbstractRepository


class ReviewService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_item(self, event: ReviewSchemaAdd):
        item_dict = event.model_dump()
        item_dict['time'] = datetime.now()
        item_id = await self.repo.add_one(item_dict)
        return item_id

    async def get_list(self):
        res = await self.repo.find_all()
        return res
