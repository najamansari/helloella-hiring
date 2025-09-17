from fastapi import FastAPI, HTTPException

from . import schemas

app = FastAPI()

@app.post("/payload", response_model=schemas.PayloadResponse)
async def create_payload(payload: schemas.PayloadCreate):
    if len(payload.list_1) != len(payload.list_2):
        raise HTTPException(status_code=400, detail="Lists must be of same length")

    return {"id": "temp", "payload": payload.list_1}


@app.get("/payload/{payload_id}", response_model=schemas.PayloadResponse)
async def get_payload(payload_id: str):
    return {"id": payload_id, "payload": ["testing", "one", "two", "three"]}
