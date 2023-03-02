from typing import Union

from typing import Optional

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title  : str
    body   : str
    published : Optional[bool]
@app.get("/")

def read_root():

    return {"Hello": "World"}

@app.get("/blog/{id}/comment")

def comment(id, limit=5):

    return {'data':{'1','2','3','4','5','6','7','8'}}
