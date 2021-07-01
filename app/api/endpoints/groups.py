from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Body, Cookie, Depends, Header, Path, Query
from pydantic import BaseModel, EmailStr, Field, HttpUrl

from schemas.users import Group
from api.utils import example_response
from app.api.deps import get_db, get_current_user


router = APIRouter(
    tags=['groups'],
    dependencies=[Depends(get_current_user)]
)


@router.get(
    '/',
    response_model=List[Group]
)
def read_groups(
) -> List[Group]:
    response = example_response(Group)
    return [response]


@router.get(
    '/me',
    response_model=Group
)
def read_groups_me_WIP(
) -> Any:
    response = example_response(Group)
    return response
