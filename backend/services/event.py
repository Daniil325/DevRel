from backend.repositories.event import EventRepository
from backend.repositories.event_tag import EventTagRepository
from backend.schemas.event import EventSchemaAdd


class EventService:
    def __init__(self, repo: EventRepository, event_tag_repo: EventTagRepository):
        self.repo: EventRepository = repo()
        self.event_tag: EventTagRepository = event_tag_repo()

    async def add_event(self, event: EventSchemaAdd):
        event_dict = event.model_dump()
        event_id = await self.repo.add_one(event_dict)
        return event_id

    async def get_all(self, order, filter_tag, filter_date, search):
        event_id = []

        if filter_tag:
            event_id = await self.event_tag.get_event_by_tag_id(filter_tag)

        events = await self.repo.get_events(order, filter_date, event_id, search)
        return events

    async def get_event(self, id: int):
        event = await self.repo.get_by_id(id)
        return event