from backend.repositories.event import EventRepository
from backend.schemas.event import EventSchemaAdd
from backend.utils.repository import AbstractRepository


class EventService:
    def __init__(self, repo: EventRepository):
        self.repo: EventRepository = repo()

    async def add_event(self, event: EventSchemaAdd):
        event_dict = event.model_dump()
        event_id = await self.repo.add_one(event_dict)
        return event_id

    async def get_all(self):
        events = await self.repo.get_events_ordered_date()
        return events

    async def get_all_ordered(self):
        events = await self.repo.get_events_ordered_date('DESC')
        return events

    async def get_event(self, id: int):
        event = await self.repo.get_by_id(id)
        return event