from fastapi import FastAPI, HTTPException

from . import database, schemas

database.init_db()

app = FastAPI()


@app.post("/payload", response_model=schemas.CreateResponse)
async def create_payload(payload: schemas.CreatePayload):
    if len(payload.list_1) != len(payload.list_2):
        raise HTTPException(status_code=400, detail="Lists must be of same length")

    return {"id": "temp"}


@app.get("/payload/{payload_id}", response_model=schemas.GetResponse)
async def get_payload(payload_id: str):
    return {"payload": ["testing", "one", "two", "three"]}
