from backend.schemas.event_tag import EventTagSchemaAdd
from backend.utils.repository import AbstractRepository


class EventTagService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_event(self, event: EventTagSchemaAdd):
        event_dict = event.model_dump()
        event_id = await self.repo.add_one(event_dict)
        return event_id

    async def get_event_tags(self):
        res = await self.repo.find_all()
        return res
