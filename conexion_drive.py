import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from conexion_vault import get_credentials_from_vault  

def get_drive_service():
    """Autenticación en Google Drive usando credenciales obtenidas de Vault"""
    credentials_dict = get_credentials_from_vault() 

    creds = service_account.Credentials.from_service_account_info(credentials_dict)

    return build("drive", "v3", credentials=creds)

if __name__ == "__main__":
    try:
        drive_service = get_drive_service()
        print("Autenticacion con Google Drive exitosa")
    except Exception as e:
        print(f"Error en la autenticacion con Google Drive: {e}")
