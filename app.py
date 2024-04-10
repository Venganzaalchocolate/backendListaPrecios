from fastapi import FastAPI
from apizoho import obtenerCampaniasActivas, obtenerCasasDisponibles, camTienePisos
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

    return(await obtenerCampaniasActivas())

@app.get('/api/obtenercasasdisponibles/{idcampania:int}')
async def obtener_casas_disponibles(idcampania: int):
    return( await obtenerCasasDisponibles(idcampania))

@app.get('/api/camtienepisos/{idcampania:int}')
async def numero_casas_cam(idcampania: int):
    return(await camTienePisos(idcampania))


    """
    datos=await obtenerCampaniasActivas()
    lista=list()
    for item in datos:
        idCampania=item['idCampania']
        tiene=await camTienePisos(idCampania)
        if tiene['count']>0:
            lista.append(item)
    """