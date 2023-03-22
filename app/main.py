from fastapi import FastAPI
import pandas as pd
from etl import df_r
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

@app.get("/")   
async def index():
    return "Inicio"

@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
async def get_max_duration(year:int, platform:str, duration_type:str):
    return get_max_duration_r()

@app.get("/get_score_count/{platform}/{scored}/{year}")  #get_score_count(platform, scored, year)
async def get_score_count():
    return get_score_count_r()

@app.get("/get_count_platform/{platform}")  #get_count_platform(platform))
async def get_count_platform(platform:str):
    return get_count_platform_r()

@app.get("/get_actor/{platform}/{year}") #get_actor(platform, year)
async def get_actor(year):
    return get_actor_r()



#1
def get_max_duration_r(year: Optional[int]=None, platform: Optional[str]=None, duration_type: Optional[str]='min'):

    return

#2

def get_score_count_r(platform : str, scored : float, release_year: int):

    return

#3

def get_count_platform_r(platform: str):

    return

#4

def get_actor_r(platform: str, year: int):

    return