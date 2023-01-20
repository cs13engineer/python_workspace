from Database import connection

def Login(userData):
    db = connection.ConnectDB()
    dbCursor = db.cursor()
    tableName = 'bankLogin'
    # print("data and sql Connection Checking",type(data))
    # query = "select * from "+tableName+" where userName = '"+data['userName']+"' and password = '"+data['password']+"';"
    query = "select * from "+tableName+" where userName = '"+userData['userName']+"';"
    print(query)
    dbCursor.execute(query)
    result = dbCursor.fetchall()
    print(result)
    dbCursor.close()
    if result:
        resp = list(result[0])
        if(resp[1]==userData['password']):
            print('Logged In')
            return {
                'response':'loggedIn'
            }
        else:
            print('Password is incorrect')
            return {
                'response':'incorrectPassword'
            }
    else:
        print('User not Found')
        return {
            'response':'userNotFound'
        }

def UserLogin(myData):
    db = connection.ConnectDB()
    dbCusror = db.cursor()
    tableName = "log"
    query = "select * from "+tableName+" where userName ='"+myData['userName']+"';"

    dbCusror.execute(query)
    result = dbCusror.fetchall()
    # arrayOfTupple [(),()]--> result
    # print('Query: ',query)
    # print('result is here:',result)

    if result:
        user = list(result[0])
        if user[1] == myData['password']:
            return {
                "response":"Logged In successfully"
            }
        else:
            return {
                "response":"Password is incorrect"
            }

    else:
        return {
            "response":"User Not Found, Kindly register first"
        }
    
    # return {
    #     "response":"success",
    #     "message":"well done",
    #     "data":myData
    # }