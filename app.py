from fastapi import FastAPI
from apizoho import obtenerCampaniasActivas, obtenerCasasDisponibles
from renovador import renovarToken
from fastapi.middleware.cors import CORSMiddleware


app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

@app.get('/api/token')
async def token():
    return( await renovarToken())

@app.get('/api/obtenercampaniasactivas')
async def obtener_campanias_disponibles():
    return( await obtenerCampaniasActivas())

@app.get('/api/obtenercasasdisponibles/{idcampania:int}')
async def obtener_casas_disponibles(idcampania: int):
    return( await obtenerCasasDisponibles(idcampania))