from backend.models.event import Event
from backend.utils.repository import SQLAlchemyRepository


class EventRepository(SQLAlchemyRepository):
    model = Event
