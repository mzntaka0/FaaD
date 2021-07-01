# -*- coding: utf-8 -*-
"""
"""
from typing import Optional

from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
from passlib.context import CryptContext
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from fastapi import Request, HTTPException, status
from fastapi.security import OAuth2
from fastapi.security.oauth2 import OAuthFlowsModel
from fastapi.security.utils import get_authorization_scheme_param

from app.core.config import settings

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(
    subject: Union[str, Any], expires_delta: timedelta = None
) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# TODO: add TypeError and valueError. See here: https://passlib.readthedocs.io/en/stable/lib/passlib.context.html#passlib.context.CryptContext.verify
def verify_password(plain_password: str, hashed_password: str) -> bool:
    # FIXME: Here would have a fatal error.
    iterations = hashed_password.split('$')[1]
    salt = hashed_password.split('$')[2]
    hasher = PBKDF2PasswordHasher()
    hashed_plain_password = hasher.encode(plain_password, salt, int(iterations))
    return hashed_plain_password == hashed_password
    #return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# NOTE: this is based on this issue: https://github.com/tiangolo/fastapi/issues/480#issuecomment-526149030
class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    # TODO: could imitate this code: https://github.com/tiangolo/fastapi/blob/d6b5bc940178c5c4a305a7564d66f220ba8ab6c1/fastapi/security/oauth2.py#L139
    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("access_token")

        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Not authenticated",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None

        return param
