# -*- coding: utf-8 -*-
"""
"""
from typing import Optional
from datetime import datetime
from uuid import UUID
import uuid
from enum import Enum

from pydantic import BaseModel, Field, HttpUrl, EmailStr



# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str


class Group(BaseModel):
    id: UUID = Field(uuid.uuid4(), description='the group id')
    name: str = Field(..., max_length=64)
