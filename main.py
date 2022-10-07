from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []

class City(BaseModel):
    name: str
    timezone:str

@app.post("/cities")
def create_city(city : City):
    db.append(city.dict())

    return db[-1]