from backend.schemas.tag import TagSchemaAdd, TagSchemaUpdate, TagSchemaDelete
from backend.utils.repository import AbstractRepository


class TagService:
    def __init__(self, tag_repo: AbstractRepository):
        self.tag_repo: AbstractRepository = tag_repo()

    async def get_tags(self):
        tags = await self.tag_repo.find_all()
        return tags

    async def get_by_id(self, id):
        tag = await self.tag_repo.get_by_id(id)
        return tag

    async def add_tag(self, tag: TagSchemaAdd):
        tag_dict = tag.model_dump()
        tag_id = await self.tag_repo.add_one(tag_dict)
        return tag_id

    async def update_tag(self, tag: TagSchemaUpdate, id: int):
        tag_dict = tag.model_dump()
        tag_id = await self.tag_repo.update_item(tag_dict, id)
        return tag_id

    async def delete_tag(self, tag: TagSchemaDelete):
        tag_dict = tag.model_dump()
        tag_id = await self.tag_repo.delete_item(tag_dict)
        return tag_id
