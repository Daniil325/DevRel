from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from backend.db.db import Base, User
from backend.models.event import Event
from backend.models.status import Status


class UserEvent(Base):
    __tablename__ = 'user_event'

    id = Column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey(User.id))
    event_id = mapped_column(ForeignKey(Event.id))
    status_id = mapped_column(ForeignKey(Status.id))

    user = relationship(
        User, foreign_keys=[user_id], lazy='joined'
    )
    event = relationship(
        Event, foreign_keys=[event_id], lazy='joined'
    )
    status = relationship(
        Status, foreign_keys=[status_id], lazy='joined'
    )
