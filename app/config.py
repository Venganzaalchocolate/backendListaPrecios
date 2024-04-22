from dotenv import load_dotenv
import os
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


header = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def headerApi(token):
    return { 'Authorization': 'Zoho-oauthtoken '+token }
