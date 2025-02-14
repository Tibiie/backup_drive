import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Configuración de la base de datos
db_config = {
    'host': '192.168.1.171',
    'database': 'consignaciones-microservice',
    'user': 'admin',
    'password': 'admin',
}

try:
    conn = mysql.connector.connect(**db_config)
    if conn.is_connected():
        print("Conexión exitosa con MySQL")

        cursor = conn.cursor(dictionary=True)  

        query = """
        SELECT * FROM comprobantes 
        WHERE fecha_creacion BETWEEN %s AND CURDATE();
        """
        fecha_inicio = '2024-02-14' 

        cursor.execute(query, (fecha_inicio,)) 
        resultados = cursor.fetchall()  

        print(resultados)

except Error as err:
    print(f"Error conectando con MySQL: {err}")
    
finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexión cerrada correctamente")
