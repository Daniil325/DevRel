from sqlalchemy import select, desc
from backend.db.db import async_session_maker
from backend.models.event import Event
from backend.utils.repository import SQLAlchemyRepository


class EventRepository(SQLAlchemyRepository):
    model = Event

    async def get_events_ordered_date(self, order: str = 'ASC'):
        async with async_session_maker() as session:
            if order == 'ASC':
                stmt = select(self.model).order_by(self.model.date)
            else:
                stmt = select(self.model).order_by(desc(self.model.date))

            res = await session.execute(stmt)
            return res.scalars().all()
