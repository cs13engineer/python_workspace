from Database import connection
tableName = "Nurses"
"""
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| NurseId      | int         | NO   | PRI | NULL    |       |
| NurseEmpNo   | int         | NO   |     | NULL    |       |
| NurseName    | varchar(50) | NO   |     | NULL    |       |
| NurseStation | varchar(50) | YES  |     | NULL    |       |
| NurseTelNo   | varchar(50) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Nurses")

def insertNurse():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Nurse Details\n")
        
        NurseId = int(input("Enter NurseId: "))
        NurseEmpNo = input("Enter NurseEmpNo: ")
        NurseName = input("Enter NurseName: ")
        NurseStation = input("Enter NurseStation: ")
        NurseTelNo = input("Enter NurseTelNo: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s);"
        
        values = (NurseId,NurseEmpNo,NurseName,NurseStation,NurseTelNo)
        print("Operational Query:=> ",query,values)
        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate NurseId::  {NurseId} is already present!\n")
        else:
            print("ERROR: ",e)
def displayNurse():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printNurse(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateNurse():
    
    print("Update Nurses")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update NurseId.\n2. Update NurseEmpNo\n3. Update NurseName\n4. Update NurseStation\n5. Update NurseTelNo\n6. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update NurseId:")
                NurseId = int(input("Enter NurseId:  "))
                toChange = int(input("Enter NurseId to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set NurseId = "+str(toChange)+" where NurseId = "+str(NurseId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{NurseId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update NurseEmpNo:")
                NurseId = int(input("Enter NurseId:  "))
                toChange = input("Enter NurseEmpNo to be Upadated:  ")

                query = "update "+tableName+" set NurseEmpNo = "+toChange+" where NurseId = "+str(NurseId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{NurseId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update NurseName:")
                NurseId = int(input("Enter NurseId:  "))
                toChange = input("Enter NurseName to be Upadated:  ")

                query = "update "+tableName+" set NurseName = \'"+toChange+"\' where NurseId = "+str(NurseId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{NurseId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update NurseStation:")
                NurseId = int(input("Enter NurseId:  "))
                toChange = input("Enter NurseStation to be Upadated:  ")

                query = "update "+tableName+" set NurseStation = \'"+toChange+"\' where NurseId = "+str(NurseId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{NurseId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update NurseTelNo:")
                NurseId = int(input("Enter NurseId:  "))
                toChange = input("Enter NurseTelNo to be Upadated:  ")

                query = "update "+tableName+" set NurseTelNo = \'"+toChange+"\' where NurseId = "+str(NurseId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{NurseId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()          
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteNurse():
    try:
        print("Deleting Nurse")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        NurseId = input("Enter NurseId to DELETE Nurse: ")
        query = "delete from "+tableName+" where NurseId = "+NurseId+";"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Patient with Nurse ID {NurseId} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  NurseId = {NurseId} is refered by PatientDetails Table! Can't Delete.\n")
        else:
            print("ERROR: ",e)
def printNurse(nurses):
    print("\n***** Doctors Details *****")
    print("+---------+------------+-----------+--------------+-------------+")
    print("| NurseId | NurseEmpNo | NurseName | NurseStation | NurseTelNo  |")
    print("+---------+------------+-----------+--------------+-------------+")
    for nurse in nurses:
        p = list(nurse)
        print("   ",p[0],"    ",p[1],"\t",p[2],"\t",p[3],"\t",p[4])
        
    print("\n")




