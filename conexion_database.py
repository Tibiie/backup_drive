import mysql.connector

DB_CONFIG = {
    "host": "192.168.1.171",  
    "port": 3306, 
    "user": "admin",  
    "password": "admin", 
    "database": "consignaciones-microservice", 
}

try:
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    print("Conexion exitosa")
    for table in tables:
        print(table[0])

    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"Error al conectar con MySQL: {err}")
