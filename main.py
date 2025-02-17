from backup import agregar_archivos_nuevos_a_zip
from upload import subir_archivo_a_drive
from conexion_database import obtener_archivos_desde_bd

def main():
    archivos = obtener_archivos_desde_bd()
    if archivos:
        print(f"Archivos a comprimir: {archivos}") 
        if agregar_archivos_nuevos_a_zip(archivos, "backup.zip"):
            print("Archivos nuevos encontrados, subiendo el backup.")
            subir_archivo_a_drive("backup.zip")
        else:
            print("No hay archivos nuevos, no se crea ni sube el backup.")
    else:
        print("No hay archivos para comprimir y subir.")

if __name__ == "__main__":
    main()
