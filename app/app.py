from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from datetime import datetime,time, timedelta
from .service.services import obtenerEnlaceLogo, renovarToken, obtenerCampaniasActivas, obtenerCasasDisponibles, obtenerCampanias, obtenerCasas

app= FastAPI()

# Configuración del middleware CORS para permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Métodos HTTP permitidos
    allow_headers=["*"],  # Encabezados permitidos
)

# Variables globales
tiempo = datetime(2023, 4, 16)  # Fecha y hora de la última actualización de campañas
campaniasactivas = ''  # Almacena la información de las campañas activas
pisos = dict()  # Diccionario para almacenar información de casas por campaña

# Ruta para obtener las campañas activas
@app.get('/api/obtenercampaniasactivas')
async def obtener_campanias_disponibles():
    """ Obtiene las campañas activas de Zoho y las almacena en la variable 'campaniasactivas'.
    Si las campañas activas no se han actualizado en los últimos 50 minutos, se recuperan nuevas campañas.
    Devuelve la información de las campañas activas al cliente.
    """
    global tiempo
    global campaniasactivas
    if campaniasactivas == '' or datetime.now() > tiempo + timedelta(minutes=50):
        campaniasactivas = await obtenerCampaniasActivas()
        tiempo = datetime.now()
    return campaniasactivas

# Ruta para obtener las casas disponibles para una campaña específica
    
@app.get('/api/obtenercasasdisponibles/{idcampania:int}')
async def obtener_casas_disponibles(idcampania: int):
    """ Obtiene las casas disponibles para una campaña específica.
    Si la información de las casas para la campaña ya está almacenada en el diccionario 'pisos' y no ha pasado más de 50 minutos desde la última actualización, se devuelve la información almacenada.
    Si las casas no están almacenadas o ha pasado más de 50 minutos desde la última actualización, se recuperan las casas de Zoho.
    La información de las casas se almacena en el diccionario 'pisos'.
    Devuelve la información de las casas disponibles al cliente.
    """
    global pisos
    global tiempo

    if idcampania in pisos and datetime.now() < tiempo + timedelta(minutes=50):
        return pisos[idcampania]
    elif datetime.now() > tiempo + timedelta(minutes=50):
        tiempo = datetime.now()
        pisos[idcampania] = await obtenerCasasDisponibles(idcampania)
    else:
        pisos[idcampania] = await obtenerCasasDisponibles(idcampania)
    return pisos[idcampania]

@app.get('/api/obtenerlogo/{idcampania:int}')
def obtenerLogo(idcampania: int):
    url= obtenerEnlaceLogo(idcampania)
    return url
