from datetime import datetime,time, timedelta

def obtenerCampanias(jsonDatos):
    campanias=map(lambda elemento:
        {
            'idCampania':elemento['id'],
            'nombreCampania':elemento['Campaign_Name']
            
        }
        , jsonDatos['data'])
    return campanias



def obtenerCasas(jsonDatos):
     auxJson=jsonDatos["data"]
     casas=map(lambda elemento:
      
      {
        # 'id':elemento['id'],
        'nombrePropiedad':elemento['Product_Name'],
        # 'ID_propiedad':elemento['ID_Propiedad'],
        'precioPropiedad':elemento['Deed_Price'],
        ##
        'jardinPropiedad':elemento['Garden_Sq_Mts'],
        'orientacionPropiedad':elemento['Orientation'],
        'trasteroPropiedad':elemento['Related_TR'],
        'portalPropiedad':elemento['Portal'],
        'metrosUtilesPropiedad':elemento['Usable_Sq_Mts'],
        'bloquePropiedad':elemento['Bloque'],
        'plazaParking1':elemento['Related_PK'],
        'plazaParking2':elemento['Related_Parking_2'],
       
        
        
        
        ##
        'plantaPropiedad':elemento['Planta'],
        'puertaPropiedad':elemento['Puerta'],
        'habPropiedad': elemento['N_Bedroom'],
        'wcPropiedad': elemento['N_Bathroom'],
        'metrosPropiedad': elemento['Sq_Mts'],
        'metrosTerraza': elemento['Terrace_Sq_Mts'],
        
		
	    # 	campaniaPropiedad = propiedad.get("Promoci_n").get("id");
	    # 	campaniaNombre = propiedad.get("Promoci_n").get("name");
       }
      
      ,auxJson)
    
     return casas

    