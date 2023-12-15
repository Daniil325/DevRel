from backend.schemas.status import StatusSchemaAdd
from backend.utils.repository import AbstractRepository


class StatusService:
    def __init__(self, repo: AbstractRepository):
        self.repo: AbstractRepository = repo()

    async def add_status(self, event: StatusSchemaAdd):
        status_dict = event.model_dump()
        status_id = await self.repo.add_one(status_dict)
        return status_id

    async def get_status(self):
        res = await self.repo.find_all()
        return res
