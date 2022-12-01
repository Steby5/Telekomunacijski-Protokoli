from fastapi import FastAPI
from pydantic import BaseModel

global knjiga

class Item(BaseModel):
    naslov: str
    cena: float
    stevilo_strani: int
    na_zalogi: bool

app = FastAPI()


@app.get("/")
async def read_user_item():
    global knjiga
    return knjiga

@app.post("/knjige/")
async def nova_knjiga(item: Item):

    return {"status":"ok"}