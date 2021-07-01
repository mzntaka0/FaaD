from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Body, Cookie, Depends, Header, Path, Query
from pydantic import BaseModel, EmailStr, Field, HttpUrl


router = APIRouter()


@router.get('/me')
def read_users_me(
    skip: int = 0,
    limit: int = 100
) -> Any:
    items = {'hello': 'world'}
    return items


@router.post('/login')
def login(
) -> Any:
    items = {'hello': 'world'}
    return items


@router.post('/logout')
def logout(
) -> Any:
    items = {'hello': 'world'}
    return items
