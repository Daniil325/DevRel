from datetime import datetime
from sqlalchemy import select, and_, or_
from backend.db.db import async_session_maker
from backend.models.message import Message
from backend.utils.repository import SQLAlchemyRepository


class MessageRepository(SQLAlchemyRepository):
    model = Message

    async def get_last_message(self, from_user_id: int, to_user_id: int, last_time: datetime):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                and_(
                    or_(
                        and_(self.model.from_user_id == from_user_id, self.model.to_user_id == to_user_id),
                        and_(self.model.from_user_id == to_user_id, self.model.to_user_id == from_user_id)
                    ),
                    self.model.date > last_time
                )
            )

            print(stmt)

            result = await session.execute(stmt)

            return result.scalars().all()

    async def get_all_message(self, from_user_id: int, to_user_id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                or_(
                    and_(self.model.from_user_id == from_user_id, self.model.to_user_id == to_user_id),
                    and_(self.model.from_user_id == to_user_id, self.model.to_user_id == from_user_id)
                )
            )

            result = await session.execute(stmt)

            return result.scalars().all()
