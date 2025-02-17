from conexion_drive import get_drive_service
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import os
import time

# Configuración de reintentos
MAX_RETRIES = 5  # Número máximo de intentos
RETRY_WAIT = 10  # Segundos de espera entre intentos

def subir_archivo_a_drive(zip_path):
    """Sube un archivo ZIP a Google Drive con reintentos y subida resumible."""
    drive_service = get_drive_service()

    file_metadata = {
        'name': os.path.basename(zip_path),
        'parents': ['1FSw1whLKX4ZAAjFsmmz644ZjsmqAb3E8'],  # Cambia al ID de la carpeta destino
    }

    media = MediaFileUpload(zip_path, mimetype='application/zip', resumable=True)  # Subida resumible
    request = drive_service.files().create(body=file_metadata, media_body=media, fields='id')

    response = None
    for intento in range(MAX_RETRIES):
        try:
            print(f"Iniciando subida (Intento {intento + 1})...")
            
            # Manejar subida por partes
            while response is None:
                status, response = request.next_chunk()
                if status:
                    print(f"Progreso: {int(status.progress() * 100)}%")  # Muestra el progreso
            
            print(f"Archivo subido con éxito: {response.get('id')}")
            return response.get('id')  # Retorna el ID del archivo subido

        except HttpError as error:
            print(f"Error en intento {intento + 1}: {error}")
            time.sleep(RETRY_WAIT)  # Espera antes de reintentar

    print("No se pudo subir el archivo después de varios intentos.")

if __name__ == "__main__":
    subir_archivo_a_drive("backup.zip")
