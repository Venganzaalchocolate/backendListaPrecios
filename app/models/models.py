def obtenerCampanias(jsonDatos):
    campanias=map(lambda elemento:
        {
            'idCampania':elemento['id'],
            'nombreCampania':elemento['Campaign_Name'],
            'contenidotabla':{
                "FECHA APROBACIÓN PRECIOS": elemento['Fecha_aprobaci_n_precios'],
                "NOMBRE EMPRESA COMERCIALIZADORA":  elemento['Nombre_empresa_comercializadora'],
                "PROPIEDAD":  elemento['Propiedad'],
                "CÓDIGO PRINEX PROMOCIÓN":  elemento['C_digo_Prinex_Promoci_n'],
                "TIPO DE IMPUESTO":  elemento['Tipo_de_Impuesto'],
                "OBRA TERMINADA/EN CURSO":  elemento['Obra_Terminada_En_curso'],
                "DELEGACIÓN":  elemento['Delegaci_n']
            },
            'observaciones':{
                'linea1':elemento['Observaciones']
            },
            'comments':{
                'linea1':elemento['Comments']
            }

        }
        , jsonDatos['data'])
    return campanias

def obtenerCasas(jsonDatos):
     auxJson=jsonDatos["data"]
     casas=map(lambda elemento:
      {
        'nombrePropiedad':elemento['Product_Name'],
        'precioPropiedad':elemento['Deed_Price'],
        'jardinPropiedad':elemento['Garden_Sq_Mts'],
        'orientacionPropiedad':elemento['Orientation'],
        'trasteroPropiedad':elemento['Related_TR'],
        'portalPropiedad':elemento['Portal'],
        'metrosUtilesPropiedad':elemento['Usable_Sq_Mts'],
        'bloquePropiedad':elemento['Bloque'],
        'plazaParking1':elemento['Related_PK'],
        'plazaParking2':elemento['Related_Parking_2'],
        'plantaPropiedad':elemento['Planta'],
        'puertaPropiedad':elemento['Puerta'],
        'habPropiedad': elemento['N_Bedroom'],
        'wcPropiedad': elemento['N_Bathroom'],
        'metrosPropiedad': elemento['Sq_Mts'],
        'metrosTerraza': elemento['Terrace_Sq_Mts'],
       }
      
      ,auxJson)
    
     return casas

    