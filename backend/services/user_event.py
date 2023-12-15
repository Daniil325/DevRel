from backend.repositories.user_event import UserEventRepository
from backend.schemas.user_event import UserEventSchemaAdd


class UserEventService:
    def __init__(self, repo: UserEventRepository):
        self.repo: UserEventRepository = repo()

    async def add_item(self, item: UserEventSchemaAdd):
        item_dict = item.model_dump()
        item_id = await self.repo.add_one(item_dict)
        return item_id

    async def get_list(self):
        res = await self.repo.find_all()
        return res

    async def get_by_user(self, user_id):
        res = await self.repo.get_events_by_user(user_id)
        return res

