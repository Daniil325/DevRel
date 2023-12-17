from backend.schemas.message import MessageSchemaAdd
from backend.utils.repository import AbstractRepository
import datetime


class MessageService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_message(self, message: MessageSchemaAdd):
        message_dict = message.model_dump()

        dt = datetime.datetime.now()

        message_dict['date'] = dt

        message_id = await self.repo.add_one(message_dict)
        return message_id

    async def get_messages(self):
        messages = await self.repo.find_all()
        return messages
