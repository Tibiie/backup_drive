import mysql.connector
from mysql.connector import Error
import os

# Configuración de la base de datos
db_config = {
    'host': '192.168.1.171',
    'database': 'consignaciones-microservice',
    'user': 'admin',
    'password': 'admin',
}

BASE_PATH = "/root/uploadsApps/consignaciones"

def obtener_archivos_desde_bd():
    """Consulta la base de datos y obtiene las rutas completas de los archivos de comprobantes."""
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print("Conexión exitosa con MySQL")

            cursor = conn.cursor(dictionary=True)  

            query = """
            SELECT ruta_archivo FROM comprobantes 
            WHERE fecha_creacion BETWEEN %s AND CURDATE();
            """
            fecha_inicio = '2024-12-01'  

            cursor.execute(query, (fecha_inicio,))  
            resultados = cursor.fetchall()  

            archivos = [os.path.join(BASE_PATH, row['ruta_archivo'].lstrip('/')) for row in resultados if row['ruta_archivo']]

            print(f"Se encontraron {len(archivos)} archivos para comprimir.")
            return archivos

    except Error as err:
        print(f"Error conectando con MySQL: {err}")
        return []

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexión cerrada correctamente")

if __name__ == "__main__":
    archivos = obtener_archivos_desde_bd()
    print(archivos)