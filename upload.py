from conexion_drive import get_drive_service
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import os
import time

MAX_RETRIES = 5 
RETRY_WAIT = 10  

def subir_archivo_a_drive(zip_path):
    """Sube un archivo ZIP a Google Drive con reintentos y subida resumible."""
    start_time = time.time()
    drive_service = get_drive_service()

    file_metadata = {
        'name': os.path.basename(zip_path),
        'parents': ['1qNiS0eHrAp-9b5SWqexh0HErxAEL5Gmq'],
    }

    media = MediaFileUpload(zip_path, mimetype='application/zip', resumable=True) 
    request = drive_service.files().create(body=file_metadata, media_body=media, fields='id')

    response = None
    for intento in range(MAX_RETRIES):
        try:
            print(f"Iniciando subida (Intento {intento + 1})...")
            
            while response is None:
                status, response = request.next_chunk()
                if status:
                    print(f"Progreso: {int(status.progress() * 100)}%")  
            
            print(f"Archivo subido con éxito: {response.get('id')}")

            elapsed_time = time.time() - start_time
            print(f"Tiempo de subida: {elapsed_time:.2f} segundos")
            return response.get('id')  

        except HttpError as error:
            print(f"Error en intento {intento + 1}: {error}")
            time.sleep(RETRY_WAIT)  

    print("No se pudo subir el archivo después de varios intentos.")

if __name__ == "__main__":
    subir_archivo_a_drive("backup.zip")
