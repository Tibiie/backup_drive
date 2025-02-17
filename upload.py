import os
import zipfile

ZIP_FILE_PATH = "backup.zip"

def comprimir_archivos(archivos, zip_path):
    """Comprime los archivos en un ZIP."""
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for archivo in archivos:
            if os.path.exists(archivo):  
                arcname = os.path.basename(archivo)  
                zipf.write(archivo, arcname)
                print(f"Archivo agregado: {arcname}")
            else:
                print(f"⚠️ Advertencia: Archivo no encontrado -> {archivo}")

    print(f"✅ Backup comprimido en {zip_path}")
