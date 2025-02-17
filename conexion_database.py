import mysql.connector
from mysql.connector import Error
import os
from datetime import datetime

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

            fecha_actual = datetime.now()
            fecha_inicio = fecha_actual.replace(month=1, day=1)
            fecha_inicio_formateada = fecha_inicio.strftime('%Y-%m-%d')
            fecha_fin = fecha_actual.strftime('%Y-%m-%d')
            print(f"Fecha de inicio: {fecha_inicio_formateada}")
            print(f"Fecha de fin: {fecha_fin}")

            cursor = conn.cursor(dictionary=True)

            query = """
            SELECT ruta_archivo FROM comprobantes 
            WHERE fecha_creacion BETWEEN %s AND %s;
            """

            cursor.execute(query, (fecha_inicio_formateada, fecha_fin))
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
