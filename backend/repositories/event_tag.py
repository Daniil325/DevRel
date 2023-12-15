from backend.models.event_tag import EventTag
from backend.utils.repository import SQLAlchemyRepository


class EventTagRepository(SQLAlchemyRepository):
    model = EventTag
