Api-Rest Lista de precios Prime Invest
===
La API de Prime Invest proporciona una herramienta para obtener información actualizada sobre los precios de una amplia gama de instrumentos financieros. Esta API utiliza una arquitectura RESTful, lo que permite una integración perfecta con diversas aplicaciones y lenguajes de programación.

## Requisitos
- Tener instalado python 3.12
- Tener instalado pip
- Tener instalado git

## Instalación
- Clona el repositorio
  ```
  git clone https://github.com/Venganzaalchocolate/backendListaPrecios.git
  ```
- Pos
  ```
  cd backendListaPrecios
  ```
- Crea un entorno virtual
  ```
  python3 venv <nombre entorno>
  ```
- Activar el entorno
  - Windows
  ```
  .\<nombre entorno>\Scripts\activate
  ```
  - Linux
  ```
  source /ruta/al/directorio/venv/bin/activate
  ```
- Instalar dependencias
  ```
  pip install -r requirements.txt
  ```
- Crear el archivo .env con:
```
  CLIENTE = "<cliente>"
  CLIENTE_CLAVE = "<clave-cliente>"
  RENOVADOR_TOKEN = "<token-renovador>"
```

## Despliegue
- Ejecutamos uvicorn 
    -  Uvicorn actua como el servidor de desarrollo para las aplicaciones FastAPI. Puedes iniciar tu aplicación FastAPI usando Uvicorn desde la línea de comandos:
  ```
  uvicorn app.app:app --reload  
  ```

## Despliegue con Dockerfile
- Construimos una imagen  
  - Este comando construirá una imagen llamada mi-imagen-app basada en el Dockerfile del directorio actual (.).
  ```
  docker build -t <mi-imagen-app> . 
  ```
- Ejecutar la imagen: 
  ```
  docker run -d -p 8000:80 --name <nombre que queremos asignar> <mi-imagen-app>
  ```
  -d: Esta opción indica que el contenedor debe ejecutarse en segundo plano, lo que significa que la terminal no se bloqueará y podrás seguir ejecutando otros comandos.

  -p 8000:80: Esta opción mapea el puerto 80 dentro del contenedor al puerto 8000 de tu máquina local. Esto significa que cualquier solicitud que llegue al puerto 8000 de tu máquina se redirigirá al puerto 80 del contenedor.

  --name <nombre que queremos asignar>: Esta opción permite asignar un nombre al contenedor. El nombre que elijas será útil para identificar y gestionar el contenedor más adelante.
  
  -mi-imagen-app: Este es el nombre de la imagen Docker que deseas ejecutar. Reemplaza mi-imagen-app con el nombre real de tu imagen.


## End-Points
- Obtener canpañas disponibles
  ```
  GET /api/obtenercampaniasactivas
  ```
  - Devuelve un json son una lista de campañas activas
    ```
    {
    "idCampania": "<id>",
    "nombreCampania": "<nombre>"
    }
    ```
- Obtener casas disponibles según id de campaña 
  ```
  GET /api/obtenercasasdisponibles/{idcampania:int}
  ```
  - Devuelve un json son una lista de pisos
    ```
    {
    "nombrePropiedad": "<nombre de la propiedad> o null",
    "precioPropiedad": "<precio de la propiedad> o null",
    "jardinPropiedad": "<jardin de la propiedad> o null",
    "orientacionPropiedad": "<orientación de la propiedad> o null",
    "trasteroPropiedad": "<trastero de la propiedad> o null",
    "portalPropiedad": "<portal de la propiedad> o null",
    "metrosUtilesPropiedad": "<metros de la propiedad> o null",
    "bloquePropiedad": "<bloque de la propiedad> o null",
    "plazaParking1": "<Parking1 de la propiedad> o null",
    "plazaParking2": "<Parking2 de la propiedad> o null",
    "plantaPropiedad": "<planta de la propiedad> o null",
    "puertaPropiedad": "<puerta de la propiedad> o null",
    "habPropiedad": "<nº de habitaciones de la propiedad> o null",
    "wcPropiedad": "<nº de baños de la propiedad> o null",
    "metrosPropiedad": "<m2 de la propiedad> o null",
    "metrosTerraza": "<m2 de la terraza de la propiedad> o null"
    }
    ```

## Estructura de directorios
```
|—— backendListaPrecios
|    |—— .env
|    |—— .gitignore
|    |—— app
|        |—— app.py
|        |—— models
|            |—— models.py
|        |—— service
|            |—— config.py
|            |—— services.py
|        |—— __init__.py
|    |—— dockerfile
|    |—— package-lock.json
|    |—— requirements.txt

```


## Collaboradores
- [Victoria Sampalo](https://github.com/Victoria-Sampalo)
- [Elisabet D'Acosta ](https://github.com/Venganzaalchocolate/)
  

