from Database import connection
tableName = "canteen"
"""
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| canteenName      | varchar(40) | YES  |     | NULL    |       |
| canteenOwnerName | varchar(40) | YES  |     | NULL    |       |
| address          | varchar(50) | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Canteen")

def insertCanteen():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Canteen Details\n")
        
        canteenName = input("Enter canteenName: ")
        canteenOwnerName = input("Enter canteenOwnerName: ")
        address = input("Enter Canteen address: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s);"
        
        values = (canteenName,canteenOwnerName,address)
        print("Operational Query:=> ",query,values)
        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate NurseId::  {canteenName} is already present!\n")
        else:
            print("ERROR: ",e)
def displayCanteen():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printCanteen(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateCanteen():
    
    print("Update Nurses")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update canteenName.\n2. Update canteenOwnerName\n3. Update address\n4. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update canteenName:")
                canteenName = input("Enter canteenName:  ")
                toChange = input("Enter canteenName to be Upadated:  ")

                query = "update "+tableName+" set canteenName = \'"+toChange+"\' where canteenName = \'"+canteenName+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{canteenName} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update canteenOwnerName:")
                canteenName = input("Enter canteenName:  ")
                toChange = input("Enter canteenOwnerName to be Upadated:  ")

                query = "update "+tableName+" set canteenOwnerName = \'"+toChange+"\' where canteenName = \'"+canteenName+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{canteenName} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update address:")
                canteenName = input("Enter canteenName:  ")
                toChange = input("Enter address to be Upadated:  ")

                query = "update "+tableName+" set address = \'"+toChange+"\' where canteenName = \'"+canteenName+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{canteenName} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteCanteen():
    try:
        print("Deleting Canteen")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        canteenName = input("Enter canteenName to DELETE Canteen: ")
        query = "delete from "+tableName+" where canteenName = \'"+canteenName+"\';"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Canteen with canteenName {canteenName} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  canteenName = {canteenName} is refered by PatientDetails Table! Can't Delete.\n")
        else:
            print("ERROR: ",e)
def printCanteen(canteens):
    print("\n***** Canteen Details *****")
    print("+------------------+-----------------------+---------------+")
    print("|   canteenName    |   canteenOwnerName    |   address     |")
    print("+------------------+-----------------------+---------------+")
    for canteen in canteens:
        p = list(canteen)
        print("\t",p[0],"\t",p[1],"\t",p[2])
        
    print("\n")




