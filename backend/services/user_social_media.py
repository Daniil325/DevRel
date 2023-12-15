from backend.schemas.user_social_media import UserSocialMediaSchemaAdd
from backend.utils.repository import AbstractRepository


class UserSocialMediaService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_item(self, event: UserSocialMediaSchemaAdd):
        item_dict = event.model_dump()
        item_id = await self.repo.add_one(item_dict)
        return item_id

    async def get_list(self):
        res = await self.repo.find_all()
        return res
