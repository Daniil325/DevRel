from backend.schemas.social_media import SocialMediaSchemaAdd
from backend.utils.repository import AbstractRepository


class SocialMediaService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_event(self, event: SocialMediaSchemaAdd):
        social_media_dict = event.model_dump()
        social_media_id = await self.repo.add_one(social_media_dict)
        return social_media_id

    async def get_social_media(self):
        res = await self.repo.find_all()
        return res
