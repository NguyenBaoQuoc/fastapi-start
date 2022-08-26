from fastapi import HTTPException, status, Header, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from typing import Union
from database.db import get_db
import os

from exceptions.user import token_exception


async def is_autheticated(token: str = Header()):
    token: str = token.split()[-1]
    # print(token)
    SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM = "HS256"
    try:
        # payload = jwt.decode(
        #     token,
        #     os.environ.get("SECRET_KEY"),
        #     algorithms=os.environ.get("ALGORITHM")
        # )
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
        )
        # print(payload)
        return payload.get("id")
    except JWTError:
        raise token_exception
        # return 0
