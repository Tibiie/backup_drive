import mysql.connector 
from mysql.connector import Error

db_config = {
    'host': '192.168.1.171',
    'database': 'cartera-temporal',
    'user': 'admin',
    'password': 'admin',
    'connection_timeout': 20
}

try:
    print("Intentando conectar a MySQL...")
    conn = mysql.connector.connect(**db_config)
    print("Intentando conectar a MySQL...")
    if conn.is_connected():
        print("✅ Conexión exitosa con MySQL")
    else:
        raise Exception("❌ No se pudo conectar a MySQL.") 

except Error as err:
    print(f"🚨 Error conectando con MySQL: {err}")
    raise  

finally:
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Conexión cerrada correctamente")
