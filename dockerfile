# Define la imagen base como Python 3.12
FROM python:3.12

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia todos los archivos y directorios del directorio actual a /app
COPY . /app

# Instala las dependencias desde requirements.txt
RUN pip install -r /app/requirements.txt

# Exporta el puerto 80 para el tráfico web
EXPOSE 80

# Inicia la aplicación Uvicorn
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
