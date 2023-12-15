from sqlalchemy import Column, Integer, ForeignKey, Date, String
from sqlalchemy.orm import mapped_column, relationship
from backend.db.db import Base, User
from backend.models.event import Event


class Review(Base):
    __tablename__ = 'review'

    id = Column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey(User.id))
    event_id = mapped_column(ForeignKey(Event.id))
    message = mapped_column(String)
    time = mapped_column(Date)

    user = relationship(
        User, foreign_keys=[user_id], lazy='joined'
    )
    event = relationship(
        Event, foreign_keys=[event_id], lazy='joined'
    )