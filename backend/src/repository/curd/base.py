from sqlalchemy.ext.asyncio import AsyncSession as SQLAlchemyAsyncSession

class BaseCRUDRepository:
    def __init_(self, async_session: SQLAlchemyAsyncSession):
        self.async_session = async_session