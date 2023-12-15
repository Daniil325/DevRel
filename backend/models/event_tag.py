from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, relationship
from backend.db.db import Base
from backend.models.event import Event
from backend.models.tag import Tag


class EventTag(Base):
    __tablename__ = 'event_tag'

    id = Column(Integer, primary_key=True)
    tag_id = mapped_column(ForeignKey(Tag.id))
    event_id = mapped_column(ForeignKey(Event.id))

    tag = relationship(
        Tag, foreign_keys=[tag_id], lazy='joined'
    )
    event = relationship(
        Event, foreign_keys=[event_id], lazy='joined'
    )
