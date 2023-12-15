from sqlalchemy import select
from backend.db.db import async_session_maker
from backend.models.user_event import UserEvent
from backend.utils.repository import SQLAlchemyRepository


class UserEventRepository(SQLAlchemyRepository):
    model = UserEvent

    async def get_events_by_user(self, user_id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.user_id == user_id)
            res = await session.execute(stmt)
            return res.scalars().all()
