import datetime

import sqlalchemy

from sqlalchemy.orm import Mapped as SQLAlchemyMapped, mapped_column as SQLAlchemy_mapped_column
from sqlalchemy.sql import func as sqlalchemy_func
from src.repository.table import Base

class Account(Base):
    __tablename__ = "account"

    id: SQLAlchemyMapped[int] = SQLAlchemy_mapped_column(autoincrement=True, primary_key=True)
    username: SQLAlchemyMapped[str] = SQLAlchemy_mapped_column(sqlalchemy.String(length=64),nullable=False, unique=True)
    email: SQLAlchemyMapped[str] = SQLAlchemy_mapped_column(sqlalchemy.String(length=64),nullable=False, unique=True)
    email: SQLAlchemyMapped[str] = SQLAlchemy_mapped_column(sqlalchemy.String(length=64), nullable=False, unique=True)
    _hashed_password: SQLAlchemyMapped[str] = SQLAlchemy_mapped_column(sqlalchemy.String(length=1024), nullable=True)
    _hash_salt: SQLAlchemyMapped[str] = SQLAlchemy_mapped_column(sqlalchemy.String(length=1024), nullable=True)
    is_verified: SQLAlchemyMapped[bool] = SQLAlchemy_mapped_column(sqlalchemy.Boolean, nullable=False, default=False)
    is_active: SQLAlchemyMapped[bool] = SQLAlchemy_mapped_column(sqlalchemy.Boolean, nullable=False, default=False)
    is_logged_in: SQLAlchemyMapped[bool] = SQLAlchemy_mapped_column(sqlalchemy.Boolean, nullable=False, default=False)
    created_at: SQLAlchemyMapped[datetime.datetime] = SQLAlchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True), nullable=False, server_default=sqlalchemy_func.now()
    )
    updated_at: SQLAlchemyMapped[datetime.datetime] = SQLAlchemy_mapped_column(
        sqlalchemy.DateTime(timezone=True),
        nullable=True,
        server_onupdate=sqlalchemy.schema.FetchedValue(for_update=True),
    )

    __mapper_args__ = {"eager_defaults": True}

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    @property
    def hash_salt(self) -> str:
        return self._hash_salt
    
    def set_hashed_password(self, hashed_password: str) -> None:
        self._hashed_password = hashed_password

    def set_hash_salt(self, hash_salt: str) -> None:
        self._hash_salt = hash_salt

