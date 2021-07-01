from fastapi import APIRouter, Body, Cookie, Depends, Header, Path, Query
from fastapi.responses import FileResponse

router = APIRouter()


@router.get('/')
def read_erd():
    return FileResponse('app/public/erd_from_sqlalchemy.png')
