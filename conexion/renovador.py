import os
from dotenv import load_dotenv 

load_dotenv()

CLIENTE = os.getenv('CLIENTE')
CLIENTE_CLAVE = os.getenv('CLIENTE_CLAVE')
RENOVADOR_TOKEN = os.getenv('RENOVADOR_TOKEN')