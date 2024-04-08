import os
from fastapi import FastAPI, HTTPException
import requests
from parsearDatos import obtenerCampanias
from renovador import renovarToken



async def obtenerCasasDisponibles(id):

    try:
      tokenRenovado= await renovarToken()
    except:
      raise HTTPException(status_code=response.status_code, detail="No se pudo renovar el token")
    
    bodyData = {
    'ejemplo': 'ejemplo',
    }
    headers = {
    'Authorization': 'Zoho-oauthtoken '+tokenRenovado
    }
    
    urlCampaniasActivas=f"https://www.zohoapis.com/crm/v2/products/search?criteria=(Status:equals:Available)AND(Promoci_n.id:equals:{id})"
    
    try:
        # Hacer una solicitud GET a la API externa
        response = requests.get(urlCampaniasActivas, headers=headers )
        # Verificar el código de estado de la respuesta
        if response.status_code == 200:
            # Si la solicitud es exitosa, devolver los datos
            d=response.json()
            return d

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
    
    bodyData = {
    'ejemplo': 'ejemplo',
    }
    headers = {
    'Authorization': 'Zoho-oauthtoken '+tokenRenovado
    }
    
    urlCampaniasActivas="https://www.zohoapis.com/crm/v2/campaigns/search?criteria=(Status:equals:Active)"
    try:
        # Hacer una solicitud GET a la API externa
        response = requests.get(urlCampaniasActivas, headers=headers )
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

