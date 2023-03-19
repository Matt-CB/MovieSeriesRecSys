from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return "Inicio"

@app.get("/get_max_duration")
async def max_duration():
    return "duracion"

@app.get("/get_score_count")
async def get_score_count():
    return "cantidad_de_peliculas_puntaje"

@app.get("/get_count_platform")
async def get_count_platform():
    return "cantidad_de_peliculas_plataforma"

@app.get("/get_actor")
async def get_actor():
    return "Actor que mas repite"



