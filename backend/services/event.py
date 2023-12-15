from backend.schemas.event import EventSchemaAdd
from backend.utils.repository import AbstractRepository


class EventService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_event(self, event: EventSchemaAdd):
        event_dict = event.model_dump()
        event_id = await self.repo.add_one(event_dict)
        return event_id

    async def get_tags(self):
        events = await self.repo.find_all()
        return events
