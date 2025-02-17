import json
from googleapiclient.discovery import build
from google.oauth2 import service_account
from conexion_vault import get_credentials_from_vault
from googleapiclient.http import MediaFileUpload
import os

ZIP_FILE_PATH = "backup.zip"

def get_drive_service():
    """Autenticación en Google Drive usando credenciales obtenidas de Vault."""
    credentials_dict = get_credentials_from_vault()  
    creds = service_account.Credentials.from_service_account_info(credentials_dict)
    return build("drive", "v3", credentials=creds)

def subir_a_drive(file_path):
    """Sube el archivo ZIP a Google Drive."""
    drive_service = get_drive_service()
    
    file_metadata = {
        'name': os.path.basename(file_path),
        'mimeType': 'application/zip'
    }

    media = MediaFileUpload(file_path, mimetype='application/zip')

    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    
    print(f"Archivo subido con éxito a Google Drive, ID: {file.get('id')}")

if __name__ == "__main__":
    subir_a_drive(ZIP_FILE_PATH)
