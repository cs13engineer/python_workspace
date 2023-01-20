from Database import connection

def getBankDetails():
    db = connection.ConnectDB()
    dbCursor = db.cursor()
    tableName = 'Bank'
    query = "select * from "+tableName+";"
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    db.close()
    if result:
        return {
            'response':'success',
            'data':result
        }
    else:
        return {
            'response':'fail'
        }

def RegisterCustomer(data):
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        tableName = 'bankCustomer'
        query = "insert into "+tableName+" values(%s,%s,%s)"
        values = (data['custId'],data['custName'],data['bankId'])

        dbCursor.execute(query,values)
        db.commit()
        db.close()

        print("\n",dbCursor.rowcount," row is inserted\n")
        if dbCursor.rowcount:
            return {
                'response':'success',
                'rowCount':dbCursor.rowcount,
                'data':data
            }
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate CustID::  {data['custId']} is already present!\n")
        return {
            'response':'fail'
        }