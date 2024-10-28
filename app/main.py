from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
def info():
    return {"name": "ob-sample-fast-api", "version": "1.0.0"}


@app.get("/operation/area/{length_in_mtr}")
def read_item(length_in_mtr: int):
    
    area_in_mtr = length_in_mtr * length_in_mtr
    
    return {"cal_area": area_in_mtr, "len_in_mtr": length_in_mtr}
