from backend.repositories.message import MessageRepository
from backend.schemas.message import MessageSchemaAdd
import datetime


class MessageService:
    def __init__(self, repo: MessageRepository):
        self.repo: MessageRepository = repo()

    async def add_message(self, message: MessageSchemaAdd):
        message_dict = message.model_dump()

        dt = datetime.datetime.now()

        message_dict['date'] = dt

        message_id = await self.repo.add_one(message_dict)
        return message_id

    async def get_messages(self):
        messages = await self.repo.find_all()
        return messages

    async def get_last_message(self, from_user_id: int, to_user_id: int, last_time: datetime):
        if last_time is None:
            messages = await self.repo.get_all_message(from_user_id, to_user_id)
        else:
            messages = await self.repo.get_last_message(from_user_id, to_user_id, last_time)

        return messages
