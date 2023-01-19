import mysql.connector
'returns Database Cursor for DB Operations'
def ConnectDB():
    db = mysql.connector.connect(
        host ="localhost",
        user="amol",
        password="amol",
        database="Capstone"
    )
    # print(db.cursor())
    return db
