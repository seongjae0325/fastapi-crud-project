from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone:str

@app.post("/cities")
def create_city(city : City):
    db.append(city.dict())

    return db[-1]

@app.get("/cities")
def get_cities():
    print(db)
    results = []
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs) 
        cur_time = r.json()["datetime"]
        results.append({"name": city["name"], "timezone": city["timezone"], "current_time": cur_time})
    return results