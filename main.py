import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from mangum import Mangum


class Id(BaseModel):
    company_id: int
    user_id: int

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Test backend for web2 <> web3"}

@app.put("/check-status/{nfrid}")
async def check_status(nfrid: int, id: Id):
    if id.company_id % 2 == 1 and id.user_id % 2 == 1:
        results = {"nfrstatus": True}
    else:
        results = {"nfrstatus": False}
    return results