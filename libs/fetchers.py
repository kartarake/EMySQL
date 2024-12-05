import mysql.connector

def fetchtable(database:str, user:str, password:str, host:str, table:str) -> list:
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    data = cursor.fetchall()

    db.close()
    return data

def fetchheadings(database:str, user:str, password:str, host:str, table:str) -> list:
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = db.cursor()
    cursor.execute(f"DESCRIBE {table}")
    data = cursor.fetchall()
    headings = [row[0] for row in data]

    db.close()
    return headings