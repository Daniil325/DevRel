from pydantic import BaseModel


class StatusSchema(BaseModel):
    id: int
    name: str


class StatusSchemaAdd(BaseModel):
    name: str
