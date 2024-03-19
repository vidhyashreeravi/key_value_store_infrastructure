# main.py
from tasks import store_data, get_data
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()


class KeyValue(BaseModel):
    key: str
    value: str



@app.get("/{key}")
async def read_item(key: str):
    val = get_data(key)
    res = val
    print(res)
    print(type(res))
    return {key: res}


@app.post("/create")
async def write_item(data: KeyValue = Body(...)):
    result = store_data(data.key, data.value)
    result()
    return {"message": f"Successfully Stored {data.key}, {data.value} in Redis"}
