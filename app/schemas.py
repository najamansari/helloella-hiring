from typing import List

from pydantic import BaseModel


class CreatePayload(BaseModel):
    list_1: List[str]
    list_2: List[str]


class CreateResponse(BaseModel):
    id: str


class GetResponse(BaseModel):
    payload: List[str]
