from pydantic import BaseModel


class EventTagSchema(BaseModel):
    id: int
    tag_id: int
    event_id: int


class EventTagSchemaAdd(BaseModel):
    tag_id: int
    event_id: int
