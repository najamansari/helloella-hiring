import json
import hashlib
from typing import List, Optional

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Transformation


async def get_or_create_transform_id(db: AsyncSession, list_1: List[str], list_2: List[str]) -> str:
    input_hash = hash_inputs(list_1, list_2)
    transformed = await get_transform(db, input_hash)

    if not transformed:
        transformed_list = apply_transform(list_1, list_2)
        await store_transform(db, transformed_list, input_hash)

    return input_hash


def apply_transform(list_1: List[str], list_2: List[str]) -> List[str]:
    return [element for tup in zip(list_1, list_2) for element in tup]


def hash_inputs(list_1: List[str], list_2: List[str]) -> str:
    string = "".join(["".join(list_1), "".join(list_2)])
    return hashlib.sha1(string.encode()).hexdigest()


async def get_transform(db:AsyncSession, input_hash: str) -> Optional[str]:
    stmt = (
        select(Transformation.transformed)
        .where(Transformation.input_hash == input_hash)
    )
    transformed_str = (await db.scalars(stmt)).first()

    return json.loads(transformed_str) if transformed_str else None


async def store_transform(db:AsyncSession, transformed: List[str], input_hash: str) -> None:
    stmt = insert(Transformation).values([{
        "input_hash": input_hash,
        "transformed": json.dumps(transformed),
    }])
    await db.execute(stmt)
    await db.commit()
