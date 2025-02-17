from conexion_drive import get_drive_service
from googleapiclient.http import MediaFileUpload
import os

def subir_archivo_a_drive(zip_path):
    """Sube un archivo ZIP a Google Drive."""
    drive_service = get_drive_service()

    file_metadata = {
        'name': os.path.basename(zip_path),
        'parents': ['root'],  # Cambia 'root' por el ID de la carpeta si quieres subirlo a una carpeta específica
    }

    media = MediaFileUpload(zip_path, mimetype='application/zip')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print(f"Archivo subido a Google Drive con ID: {file['id']}")

if __name__ == "__main__":
    subir_archivo_a_drive("backup.zip")