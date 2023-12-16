from sqlalchemy import select, or_
from backend.db.db import async_session_maker
from backend.models.event_tag import EventTag
from backend.utils.repository import SQLAlchemyRepository


class EventTagRepository(SQLAlchemyRepository):
    model = EventTag

    async def get_event_by_tag_id(self, tags_id: list):
        async with async_session_maker() as session:
            stmt = select(self.model.event_id)

            tags_id_int = list(map(int, tags_id))

            stmt = stmt.where(self.model.tag_id.in_(tags_id_int))

            res = await session.execute(stmt)
            return res.scalars().all()
