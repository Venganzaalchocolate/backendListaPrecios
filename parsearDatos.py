from datetime import datetime,time, timedelta

def obtenerCampanias(jsonDatos):
    campanias=map(lambda elemento:
        {
            'idCampania':elemento['id'],
            'nombreCampania':elemento['Campaign_Name']
            
        }
        , jsonDatos['data'])
    return campanias

    