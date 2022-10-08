from fastapi import FastAPI
from fastapi.response import HTMLresponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

origins = [
      "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



db = []

class City(BaseModel):
    name: str
    timezone:str

templates = Jinja2Templates(directory="templates")

@app.post("/cities")
def create_city(city : City):
    db.append(city.dict())

    return db[-1]

@app.get("/cities", response_class=HTMLresponse)
def get_cities():
    print(db)
    results = []
    for city in db:
        strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
        r = requests.get(strs) 
        cur_time = r.json()["datetime"]
        results.append({"name": city["name"], "timezone": city["timezone"], "current_time": cur_time})
    return results

@app.get("/cities/{city_id}")
def get_city(city_id: int):
    city = db[city_id-1]
    strs = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()["datetime"]

    return {"name": city["name"], "timezone": city["timezone"], "current_time": cur_time}

@app.delete("/cities/{city_id}")
def delete_city(city_id: int):
    db.pop(city_id-1)

    return {}