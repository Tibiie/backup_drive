import requests
import json

VAULT_URL = "http://192.168.1.171:8200/v1/kv/data/credential"
VAULT_TOKEN = "hvs.DrjomI38eiLeY3cWcsm0AVcF"

def get_credentials_from_vault():
    headers = {"X-Vault-Token": VAULT_TOKEN}
    response = requests.get(VAULT_URL, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Error obteniendo credenciales desde Vault: {response.text}")
    
    secret_data = response.json()
    
    if "data" not in secret_data or "data" not in secret_data["data"]:
        raise Exception("Estructura inesperada del secreto en Vault")

    return secret_data["data"]["data"] 

if __name__ == "__main__":
    try:
        credentials = get_credentials_from_vault()
        print("Conexión exitosa con Vault")
        print(json.dumps(credentials, indent=2))  
    except Exception as e:
        print(f"Error: {str(e)}")
