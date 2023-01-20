from urllib import response
from Database import connection
def CreateAccount(acDetail):
    print('Im in Server: ',acDetail)
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()

        tableName = "Account"

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s)"
        values = (
            acDetail['accountNumber'],
            acDetail['ifscCode'],
            acDetail['bankId'],
            acDetail['custId'],
            acDetail['issuedOn']
        )

        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print(dbCursor.rowcount," is inserted!!!")
        
        return{
            "response":"success"
        }
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate Account Number::  {acDetail['accountNumber']} is already present!\n")
            return {
             'response':'fail'
            }
        else:
            print("ERROR: ",e)

def GetCustomer():
    db = connection.ConnectDB()
    dbCursor = db.cursor()
    query = "select * from bankCustomer;"
    dbCursor.execute(query)
    return dbCursor.fetchall()