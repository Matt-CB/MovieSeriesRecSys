from fastapi import FastAPI
import pandas as pd
from etl import etl


netflix=pd.read_csv("Datasets\\amazon_prime_titles.csv")
hulu=pd.read_csv("Datasets\\hulu_titles.csv")
disney_plus=pd.read_csv("Datasets\\disney_plus_titles.csv")
amazon_prime=pd.read_csv("Datasets\\amazon_prime_titles.csv")

DF_Proyect = etl(netflix, hulu, disney_plus, amazon_prime)

DF_Proyect

r1 = pd.read_parquet('1.gzip')
print(r1)
app = FastAPI()

@app.get("/")
async def index():
    return "Inicio"

@app.get("/get_max_duration/{year}/{platform}/{duration_type}")
async def get_max_duration(year:int, platform:str, duration_type:str):
    return r1

@app.get("/get_score_count")
async def get_score_count():
    return "cantidad_de_peliculas_puntaje"

@app.get("/get_count_platform")
async def get_count_platform():
    return "cantidad_de_peliculas_plataforma"

@app.get("/get_actor/{year}")
async def get_actor(year):
    return get_actor_r(2002)


'''Película con mayor duración con filtros 
opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))'''

def get_max_duration_r():
    