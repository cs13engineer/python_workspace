import mysql.connector

def ConnectDB():
    db = mysql.connector.connect(
        host ="localhost",
        user="amol",
        password="amol",
        database="Bank"
    )
    # print(db)
    return db