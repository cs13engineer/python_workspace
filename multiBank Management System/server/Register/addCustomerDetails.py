from Database import connection
def AddDetails(custDetails):
    try:
        print("user details: ", custDetails['detailId'],
            custDetails['custId'],
            custDetails['adharNumber'],
            custDetails['mobileNumber'],
            custDetails['panNumber'],
            custDetails['emailId'],
            custDetails['address'])
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        tableName = "customerDetails"
        query = "insert into "+tableName+" values (%s,%s,%s,%s,%s,%s,%s)"
        values = (
            custDetails['detailId'],
            custDetails['custId'],
            custDetails['adharNumber'],
            custDetails['mobileNumber'],
            custDetails['panNumber'],
            custDetails['emailId'],
            custDetails['address']
        )

        dbCursor.execute(query,values)

        db.commit()
        db.close()
        print(dbCursor.rowcount," row is inserted")

        if dbCursor.rowcount:
            return{
                "response":"success",
                "data":custDetails
            }
        else:
            return{
                "response":"fail"
            }
    except Exception as e:
        print("ERROR while adding details: ",e)
        return {
            "response":"fail"
        }
