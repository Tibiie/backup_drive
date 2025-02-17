from upload import subir_archivo_a_drive
from conexion_database import obtener_archivos_desde_bd
from backup import agregar_archivos_nuevos_a_zip 

def main():
    archivos = obtener_archivos_desde_bd()
    if archivos:
        agregar_archivos_nuevos_a_zip(archivos, "backup.zip")
        subir_archivo_a_drive("backup.zip")
    else:
        print("No hay archivos para comprimir y subir.")

if __name__ == "__main__":
    main()
