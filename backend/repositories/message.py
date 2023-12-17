from backend.models.message import Message
from backend.utils.repository import SQLAlchemyRepository


class MessageRepository(SQLAlchemyRepository):
    model = Message
