
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from fastapi.middleware.cors import CORSMiddleware
from .users import User, users
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


@app.get('/all')
async def routine():
    resp = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    return resp.json()


@app.get('/api/getStatedata')
def coroutine():
    resp = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    return resp.json()['data']['regional']


@app.get('/api/state/{state}')
def stateWiseDetails(state: str):
    resp = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
    stateData = resp.json()['data']['regional']
    for i in stateData:
        if i['loc'].lower() == state.lower():
            return i
    return {'msg': 'no data found', 'success': 'fail'}


@app.post('/api/register')
def registerNew(user: User):
    users.append(user)
    return {'msg': 'inserted'}


@app.get('/api/registered')
def getAll():
    return {'users': users}
