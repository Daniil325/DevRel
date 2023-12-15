from pydantic import BaseModel


class TagSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TagSchemaAdd(BaseModel):
    name: str


class TagSchemaUpdate(BaseModel):
    name: str


class TagSchemaDelete(BaseModel):
    id: int
    name: str
