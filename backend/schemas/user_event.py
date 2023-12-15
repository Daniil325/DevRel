from pydantic import BaseModel


class UserEventSchema(BaseModel):
    id: int
    user_id: int
    event_id: int
    status_id: int

    class Config:
        from_attributes = True


class UserEventSchemaAdd(BaseModel):
    user_id: int
    event_id: int
    status_id: int


