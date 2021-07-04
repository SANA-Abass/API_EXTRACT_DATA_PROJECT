import mysql.connector
host = "localhost"
port = "3306"
user = "root"
password = ""
database = "api_extract_data_db"

def select_all(query) :
    conn = mysql.connector.connect(
        host=host,
        port=port, user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def insert_into_tble (sql, val) :
    conn = mysql.connector.connect(
        host=host,
        port=port, user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()

