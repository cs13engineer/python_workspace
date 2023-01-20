from Database import connection

def Bank(bankData):
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        tableName = 'Bank'
        query = "insert into "+tableName+" values(%s,%s,%s,%s)"
        values = (bankData['bankId'],bankData['bankName'],bankData['branchName'],bankData['IFSC'])
        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        return {
            'response':'success',
            'data':dbCursor.rowcount
        }
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate DoctId::  {bankData['bankId']} is already present!\n")
        return {
            'response':'fail'
        }
