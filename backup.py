import os
import zipfile
from conexion_database import obtener_archivos_desde_bd
from conexion_drive import obtener_archivos_en_drive

ZIP_FILE_PATH = "backup.zip"
DRIVE_FOLDER_ID = '1qNiS0eHrAp-9b5SWqexh0HErxAEL5Gmq'  

def obtener_archivos_en_zip(zip_path):
    """Obtiene la lista de archivos dentro del ZIP existente."""
    if not os.path.exists(zip_path):
        return set()  # Si el archivo ZIP no existe, retornamos un conjunto vacío.

    with zipfile.ZipFile(zip_path, 'r') as zipf:
        return set(zipf.namelist())  # Devuelve la lista de archivos dentro del ZIP.

def agregar_archivos_a_zip(archivos, zip_path):
    """Agrega archivos al ZIP sin sobrescribir los existentes."""
    
    archivos_en_zip = obtener_archivos_en_zip(zip_path)  # Archivos ya en el ZIP
    archivos_locales = {os.path.basename(file): file for file in archivos}
    
    archivos_nuevos = {
        nombre: path for nombre, path in archivos_locales.items() if nombre not in archivos_en_zip
    }

    if not archivos_nuevos:
        print("No hay archivos nuevos para agregar al ZIP.")
        return False  

    print(f"Agregando archivos nuevos: {list(archivos_nuevos.keys())}")

    with zipfile.ZipFile(zip_path, 'a') as zipf:  # 'a' para agregar sin sobrescribir
        for nombre, ruta in archivos_nuevos.items():
            if os.path.exists(ruta):
                zipf.write(ruta, nombre)
                print(f"Archivo agregado: {nombre}")
            else:
                print(f"Advertencia: Archivo no encontrado -> {ruta}")

    return True  

def agregar_archivos_nuevos_a_zip(archivos, zip_path):
    """Verifica si hay archivos nuevos y los agrega al ZIP sin sobrescribirlo."""
    archivos_drive = obtener_archivos_en_drive(DRIVE_FOLDER_ID)

    if not archivos_drive:
        print("No se encontraron archivos en Google Drive. Comprimir todos los archivos locales.")
        return agregar_archivos_a_zip(archivos, zip_path)  # Comprime todos los archivos locales.
    
    archivos_drive_nombres = {archivo['name'] for archivo in archivos_drive}
    archivos_locales = {os.path.basename(file): file for file in archivos}

    archivos_nuevos = [
        file for file in archivos_locales if file not in archivos_drive_nombres
    ]

    if archivos_nuevos:
        print(f"Archivos nuevos a agregar: {archivos_nuevos}")
        return agregar_archivos_a_zip([archivos_locales[file] for file in archivos_nuevos], zip_path)
    
    print("No hay archivos nuevos para agregar.")
    return False  
