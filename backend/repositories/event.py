from datetime import datetime

from sqlalchemy import select, desc
from backend.db.db import async_session_maker
from backend.models.event import Event
from backend.utils.repository import SQLAlchemyRepository


class EventRepository(SQLAlchemyRepository):
    model = Event

    async def get_events(self, order: str, filter_date: list, event_id: list, search: str):
        async with async_session_maker() as session:

            stmt = select(self.model)

            if filter_date:
                stmt = stmt.where(self.model.date >= datetime.strptime(filter_date[0], "%Y-%m-%d"))

            if filter_date and len(filter_date) == 2:
                stmt = stmt.where(self.model.date <= datetime.strptime(filter_date[1], "%Y-%m-%d"))

            if event_id:
                stmt = stmt.where(self.model.id.in_(event_id))

            if order == 'ASC':
                stmt = stmt.order_by(self.model.date)
            else:
                stmt = stmt.order_by(desc(self.model.date))

            result = await session.execute(stmt)

            result = result.scalars().all()

            if search:
                delete = []

                for item in result:
                    if search.lower() not in item.title.lower():
                        delete.append(item)

                if len(delete) > 0:
                    for item in delete:
                        result.remove(item)

            return result
