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
        'plantaPropiedad':elemento['Planta'],
        'habPropiedad': elemento['N_Bedroom'],
        'wcPropiedad': elemento['N_Bathroom'],
        'metrosPropiedad': elemento['Sq_Mts'],
        'metrosTerraza': elemento['Terrace_Sq_Mts'],
        'campaniaPropiedad': elemento['Terrace_Sq_Mts'],
        'metrosPropiedad': elemento['Sq_Mts'],
		
	# 	campaniaPropiedad = propiedad.get("Promoci_n").get("id");
	# 	campaniaNombre = propiedad.get("Promoci_n").get("name");
       }
      
      ,auxJson)
    
     return casas

    