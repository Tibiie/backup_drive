import os
from googleapiclient.http import MediaFileUpload
from conexion_drive import get_drive_service

ZIP_FILE_PATH = "backup.zip"

def upload_to_drive(file_path):
    """Sube un archivo ZIP a Google Drive"""
    drive_service = get_drive_service()
    
    file_metadata = {"name": os.path.basename(file_path), "mimeType": "application/zip"}
    media = MediaFileUpload(file_path, mimetype="application/zip")

    file = drive_service.files().create(body=file_metadata, media_body=media, fields="id").execute()
    print(f"Archivo subido con ID: {file.get('id')}")
    return file.get("id")

drive_file_id = upload_to_drive(ZIP_FILE_PATH)


def update_drive_zip(file_path, drive_file_id):
    """Actualiza el ZIP en Google Drive sin necesidad de descomprimirlo"""
    drive_service = get_drive_service()
    
    media = MediaFileUpload(file_path, mimetype="application/zip", resumable=True)
    file = drive_service.files().update(fileId=drive_file_id, media_body=media).execute()

    print(f"Archivo actualizado en Drive: {file.get('id')}")

update_drive_zip(ZIP_FILE_PATH, drive_file_id)
