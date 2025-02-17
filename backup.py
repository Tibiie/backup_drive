import os
import zipfile
from conexion_database import obtener_archivos_desde_bd
from conexion_drive import obtener_archivos_en_drive

ZIP_FILE_PATH = "backup.zip"
DRIVE_FOLDER_ID = '1qNiS0eHrAp-9b5SWqexh0HErxAEL5Gmq'  

def comprimir_archivos(archivos, zip_path):
    """Comprime los archivos en un ZIP."""
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for archivo in archivos:
            if os.path.exists(archivo):
                arcname = os.path.basename(archivo)
                zipf.write(archivo, arcname)
                print(f"Archivo agregado: {arcname}")
            else:
                print(f"Advertencia: Archivo no encontrado -> {archivo}")
    print(f"Backup comprimido en {zip_path}")

def agregar_archivos_nuevos_a_zip(archivos, zip_path):
    """Verifica si hay archivos nuevos y los agrega al ZIP sin descomprimirlo."""
    archivos_drive = obtener_archivos_en_drive(DRIVE_FOLDER_ID)
    
    archivos_drive_nombres = {archivo['name']: archivo for archivo in archivos_drive}

    archivos_locales = {os.path.basename(file): file for file in archivos}
    
    print(f"Archivos locales a comparar: {archivos_locales}")
    print(f"Archivos en Google Drive: {archivos_drive_nombres}")
    
    archivos_nuevos = [
        file for file in archivos_locales
        if os.path.basename(file) not in archivos_drive_nombres
    ]
    
    if archivos_nuevos:
        print(f"Archivos nuevos a agregar: {archivos_nuevos}")
        comprimir_archivos([archivos_locales[file] for file in archivos_nuevos], zip_path)
    else:
        print("No hay archivos nuevos para agregar.")
