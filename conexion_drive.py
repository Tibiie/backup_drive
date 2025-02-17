import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from conexion_vault import get_credentials_from_vault  

def get_drive_service():
    """Autenticación en Google Drive usando credenciales obtenidas de Vault"""
    credentials_dict = get_credentials_from_vault() 
    creds = service_account.Credentials.from_service_account_info(credentials_dict)
    return build("drive", "v3", credentials=creds)

def obtener_archivos_en_drive(drive_folder_id):
    """Obtiene los archivos almacenados en una carpeta específica de Google Drive."""
    try:
        service = get_drive_service()
        results = service.files().list(
            q=f"'{drive_folder_id}' in parents",
            pageSize=10,
            fields="nextPageToken, files(id, name)"
        ).execute()
        items = results.get('files', [])

        if not items:
            print("No se encontraron archivos en Google Drive.")
        else:
            print("Archivos en Google Drive:")
            for item in items:
                print(f"{item['name']} (ID: {item['id']})")
        return items

    except Exception as error:
        print(f"Error al obtener archivos desde Google Drive: {error}")
        return []
