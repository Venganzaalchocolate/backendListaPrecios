from fastapi import FastAPI
from apizoho import obtenerCampaniasActivas, obtenerCasasDisponibles
from renovador import renovarToken


app= FastAPI()

@app.get('/api/token')
async def token():
    return( await renovarToken())

@app.get('/api/obtenercampaniasactivas')
async def obtener_campanias_disponibles():
    return( await obtenerCampaniasActivas())

@app.get('/api/obtenercasasdisponibles/{idcampania:int}')
async def obtener_casas_disponibles(idcampania: int):
    return( await obtenerCasasDisponibles(idcampania))