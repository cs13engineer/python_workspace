from Database import connection
tableName = "Doctor"
"""
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| DoctId         | int         | NO   | PRI | NULL    |       |
| DoctName       | varchar(50) | NO   |     | NULL    |       |
| DoctSpeciality | varchar(50) | YES  |     | NULL    |       |
| DoctTelNo      | varchar(50) | YES  |     | NULL    |       |
| Doctemail      | varchar(50) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Doctor")

def insertDoctor():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Doctor Details\n")
        
        DoctId = int(input("Enter DoctId: "))
        DoctName = input("Enter DoctName: ")
        DoctSpeciality = input("Enter DoctSpeciality: ")
        DoctTelNo = input("Enter DoctTelNo: ")
        Doctemail = input("Enter Doctemail: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s);"
        
        values = (DoctId,DoctName,DoctSpeciality,DoctTelNo,Doctemail)
        print("Operational Query:=> ",query,values)
        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate DoctId::  {DoctId} is already present!\n")
def displayDoctor():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printDoctor(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateDoctor():
    
    print("Update Doctors")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update DoctId.\n2. Update DoctName\n3. Update DoctSpeciality\n4. Update DoctTelNo\n5. Update Doctemail\n6. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update DoctId:")
                DoctId = int(input("Enter DoctId:  "))
                toChange = int(input("Enter DoctId to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set DoctId = "+str(toChange)+" where DoctId = "+str(DoctId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{DoctId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update DoctName:")
                DoctId = int(input("Enter DoctId:  "))
                toChange = input("Enter FeedbackOn to be Upadated:  ")

                query = "update "+tableName+" set DoctName = \'"+toChange+"\' where DoctId = "+str(DoctId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{DoctId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update DoctSpeciality:")
                DoctId = int(input("Enter DoctId:  "))
                toChange = input("Enter DoctSpeciality to be Upadated:  ")

                query = "update "+tableName+" set DoctSpeciality = \'"+toChange+"\' where DoctId = "+str(DoctId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{DoctId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update DoctTelNo:")
                DoctId = int(input("Enter DoctId:  "))
                toChange = input("Enter DoctTelNo to be Upadated:  ")

                query = "update "+tableName+" set DoctTelNo = \'"+toChange+"\' where DoctId = "+str(DoctId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{DoctId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Doctemail:")
                DoctId = int(input("Enter DoctId:  "))
                toChange = input("Enter Doctemail to be Upadated:  ")

                query = "update "+tableName+" set Doctemail = \'"+toChange+"\' where DoctId = "+str(DoctId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{DoctId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()          
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteDoctor():
    try:
        print("Deleting Doctor")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        DoctId = input("Enter DoctId to DELETE Doctor: ")
        query = "delete from "+tableName+" where DoctId = "+DoctId+";"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Patient with Doctor ID {DoctId} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  InsuranceID = {InsuranceID} is refered by PatientDetails Table! Can't Delete.\n")

def printDoctor(doctors):
    print("\n***** Doctors Details *****")
    print("+--------+-------------------+-----------------------+----------------+----------------+")
    print("| DoctId |      DoctName     |      DoctSpeciality   |      DoctTelNo |      Doctemail |")
    print("+--------+-------------------+-----------------------+----------------+----------------+")
    for doctor in doctors:
        p = list(doctor)
        print("   ",p[0],"    ",p[1],"\t",p[2],"\t",p[3],"\t",p[4])
        
    print("\n")






