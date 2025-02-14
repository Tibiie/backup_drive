import os
import zipfile
import datetime
from conexion_drive import get_drive_service

SERVER_FOLDER = "/ruta/del/servidor"  
ZIP_FILE_PATH = "backup.zip"
ONE_YEAR_AGO = datetime.datetime.now() - datetime.timedelta(days=365)

def get_old_files():
    """Busca archivos de más de un año en el servidor"""
    files_to_compress = []
    for root, _, files in os.walk(SERVER_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.getmtime(file_path) < ONE_YEAR_AGO.timestamp():
                files_to_compress.append(file_path)
    return files_to_compress

def compress_files(file_list, zip_path):
    """Comprime los archivos en un ZIP sin borrar los anteriores"""
    with zipfile.ZipFile(zip_path, 'a') as zipf:
        for file in file_list:
            arcname = os.path.relpath(file, SERVER_FOLDER)
            zipf.write(file, arcname)
    print(f"Archivos comprimidos en {zip_path}")

files = get_old_files()
if files:
    compress_files(files, ZIP_FILE_PATH)
else:
    print("No hay archivos para comprimir")
