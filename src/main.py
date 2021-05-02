
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from fastapi.middleware.cors import CORSMiddleware
import requests

# resp = requests.get('https://randomuser.me/api')
# print(resp.json())
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def routine():
    return {"msg": "sdf"}
