from .config import header, bodyData, headerApi
import requests
from datetime import datetime, timedelta
from .models import obtenerCampanias, obtenerCasas
from fastapi import FastAPI, HTTPException

token=0
hora=0



async def renovarToken():
    global hora
    global token

    if  hora==0 or datetime.now() > hora + timedelta(minutes=50):
        try:
            # Hacer una solicitud GET a la API externa
            response = requests.post("https://accounts.zoho.com/oauth/v2/token", data=bodyData, headers=header )
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
                raise HTTPException(status_code=500, detail="Error al obtener datos de la API externa"+e)
    else:
        return token

async def obtenerCasasDisponibles(id):

    try:
      tokenRenovado= await renovarToken()
    except:
      raise HTTPException(status_code=response.status_code, detail="No se pudo renovar el token")
       
    urlCampaniasActivas=f"https://www.zohoapis.com/crm/v2/products/search?criteria=(Status:equals:Available)AND(Promoci_n.id:equals:{id})"
    
    try:
        # Hacer una solicitud GET a la API externa
        response = requests.get(urlCampaniasActivas, headers=headerApi(tokenRenovado) )
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # Si la solicitud es exitosa, devolver los datos
            d=response.json()
            # return d
            return list(obtenerCasas(d))
        else:

            # Si la solicitud no es exitosa, lanzar una excepción HTTP
            raise HTTPException(status_code=response.status_code, detail="No se pudo obtener las campañas activas")
    except Exception as e:
        # Capturar cualquier error y devolver un mensaje de error genérico
        if e.status_code==204:
          raise HTTPException(status_code=204, detail="La campaña no tiene pisos disponibles")
        else:
          raise HTTPException(status_code=500, detail="Error en el servidor de api de zoho al obtener las casas")
  
  
  
async def obtenerCampaniasActivas():
    try:
      tokenRenovado= await renovarToken()
    except:
      raise HTTPException(status_code=response.status_code, detail="No se pudo renovar el token")
        
    urlCampaniasActivas="https://www.zohoapis.com/crm/v2/campaigns/search?criteria=(Status:equals:Active)"
    try:
        # Hacer una solicitud GET a la API externa
        response = requests.get(urlCampaniasActivas, headers=headerApi(tokenRenovado) )
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # Si la solicitud es exitosa, devolver los datos
            
            d=response.json()
            return list(obtenerCampanias(d))
        else:
            # Si la solicitud no es exitosa, lanzar una excepción HTTP
            raise HTTPException(status_code=response.status_code, detail="No se pudo obtener las campañas activas")
    except Exception as e:
      
        # Capturar cualquier error y devolver un mensaje de error genérico
        raise HTTPException(status_code=500, detail="Error en el api al obtener las campañas activas")


