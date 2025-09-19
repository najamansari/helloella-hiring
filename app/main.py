from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from . import database, logic, schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/payload", response_model=schemas.CreateResponse)
async def create_payload(
    payload: schemas.CreatePayload, db: AsyncSession = Depends(database.get_db)
):
    (list_1, list_2) = (payload.list_1, payload.list_2)
    if len(list_1) != len(list_2):
        raise HTTPException(status_code=400, detail="Lists must be of same length")

    input_hash = await logic.get_or_create_transform_id(db, list_1, list_2)
    return { "id": input_hash }


@app.get("/payload/{payload_id}", response_model=schemas.GetResponse)
async def get_payload(payload_id: str):
    return {"payload": ["testing", "one", "two", "three"]}
