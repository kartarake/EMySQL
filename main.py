import pandas as pd
import mysql.connector
import time
import decimal
import karlib

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
    

def exporttable(data:list, headings:list, path:str) -> decimal.Decimal:
    start_time = decimal.Decimal(time.time())
    df = pd.DataFrame(data, columns=headings)
    df.to_excel(path, index=False)
    end_time = decimal.Decimal(time.time())
    return end_time - start_time

def main():
    pass

if __name__ == "__main__":
    main()