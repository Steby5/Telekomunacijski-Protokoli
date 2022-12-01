from fastapi import FastAPI
from pydantic import BaseModel

global vsota

class Item(BaseModel):
    a: int
    b: int

app = FastAPI()


@app.get("/")
async def read_user_item():
    global vsota
    return "Vsota vnesenih stevil:",vsota

@app.post("/items/")
async def create_item(item: Item):
    c = item.a + item.b
    global vsota
    vsota=c
    return {"status":"ok"}