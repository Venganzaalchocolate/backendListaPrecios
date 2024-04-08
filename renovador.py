import os
from dotenv import load_dotenv 
from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime,time, timedelta

load_dotenv()

CLIENTE = os.getenv('CLIENTE')
CLIENTE_CLAVE = os.getenv('CLIENTE_CLAVE')
RENOVADOR_TOKEN = os.getenv('RENOVADOR_TOKEN')

bodyData = {
    'refresh_token': RENOVADOR_TOKEN,
    'client_id': CLIENTE,
    'client_secret': CLIENTE_CLAVE,
    'grant_type': 'refresh_token'
}


headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

token=0
hora=0
async def renovarToken():
    global hora
    global token

    if  hora==0 or datetime.now() > hora + timedelta(minutes=50):
        try:
            # Hacer una solicitud GET a la API externa
            response = requests.post("https://accounts.zoho.com/oauth/v2/token", data=bodyData, headers=headers )
            # Verificar el código de estado de la respuesta
            if response.status_code == 200:
                    # Si la solicitud es exitosa, devolver los datos
                datos=response.json()
                hora=datetime.now()
                token=datos['access_token']
                return token
            else:
                    # Si la solicitud no es exitosa, lanzar una excepción HTTP
                raise HTTPException(status_code=response.status_code, detail="La solicitud a la API externa falló")
        except Exception as e:
                # Capturar cualquier error y devolver un mensaje de error genérico
                raise HTTPException(status_code=500, detail="Error al obtener datos de la API externa")
    else:
        return token
