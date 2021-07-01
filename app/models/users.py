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

    # relations
    group_user = relationship('GroupUser', back_populates='user')


class Group(Base):
    __tablename__ = 'Group'  # noqa

    # columns
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)
    name = Column(String(64))
    subdomain = Column(String(64))
    created_at = Column(DateTime, default=datetime.datetime.now)

    # relations
    group_user = relationship('GroupUser', back_populates='group')
    service = relationship('Service', back_populates='group')
    group_sensor = relationship('GroupSensor', back_populates='group')


class GroupUser(Base):
    __tablename__ = 'GroupUser'  # noqa

    # columns
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4)

    # foreign key
    group_id = Column(UUIDType(binary=False), ForeignKey('Group.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('User.id'))

    # relations
    group = relationship('Group', back_populates='group_user')
    user = relationship('User', back_populates='group_user')
    role = relationship('Role', back_populates='group_user')
