import datetime
import uuid

from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship
from sqlalchemy import (Boolean, Column, DateTime, Float, ForeignKey, Integer, String)  # noqa

from app.db.base_class import Base


class User(Base):
    __tablename__ = 'User'  # noqa

    # columns
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
