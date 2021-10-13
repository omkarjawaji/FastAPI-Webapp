from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from models import Startups
from mongoengine import connect

app = FastAPI()
connect(db = "FastAPI", host="localhost", port=27017)

mongoDB = Startups.objects().to_json()
#mongoDB = []

class Startup(BaseModel):
    id : int
    name : str
    type : str
    is_listed : Optional[bool] = None


@app.get("/")
def read_root():
    return {"greetings":"This is my first FastAPI WebApp"}

@app.get("/startups")
def get_startups():
    #mongoDB = Startups.objects().to_json()
    return {"Startups":mongoDB}
    #return mongoDB

@app.get("/startups/{startup_id}")
def get_startup_name(startup_id: int):
    startup =  startup_id - 1
    return mongoDB[startup]

@app.post("/startup")
def add_startup(startup : Startup):
    mongoDB.append(startup.dict())
    return mongoDB[-1]

@app.delete("/startup/{startup_id}")
def delete_startup(startup_id : int):
    mongoDB.pop(startup_id-1)
    return {"Task":"Deletion successful"}
