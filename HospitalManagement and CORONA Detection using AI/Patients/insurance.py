from Database import connection
tableName = "InsuranceInfo"
"""
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| InsuranceID     | int         | NO   | PRI | NULL    |       |
| InsuringCompany | varchar(50) | NO   |     | NULL    |       |
| TypeofPlan      | varchar(50) | NO   |     | NULL    |       |
| StartDate       | date        | YES  |     | NULL    |       |
| EndDates        | date        | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Insurance")

def insertInsurance():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Insurance Details\n")
        
        InsuranceID = int(input("Enter InsuranceID: "))
        InsuringCompany = input("Enter InsuringCompany Name: ")
        TypeofPlan = input("Enter Type of Plan: ")
        StartDate = input("Enter StartDate: ")
        EndDates = input("Enter EndDates: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s);"
        print("Operational Query:=> ",query)
        values = (InsuranceID,InsuringCompany,TypeofPlan,StartDate,EndDates)

        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate patientID::  {InsuranceID} is already present!\n")
def displayInsurance():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printPatients(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateInsurance():
    
    print("Update Insurance")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update InsuranceID.\n2. Update InsuringCompany\n3. Update TypeofPlan\n4. Update StartDate\n5. Update EndDates\n6. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update InsuranceID:")
                InsuranceID = int(input("Enter InsuranceID:  "))
                toChange = int(input("Enter InsuranceID to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set InsuranceID = "+str(toChange)+" where InsuranceID = "+str(InsuranceID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{InsuranceID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Insurance Company Name:")
                InsuranceID = int(input("Enter InsuranceID:  "))
                toChange = input("Enter Insuring Company to be Upadated:  ")

                query = "update "+tableName+" set InsuringCompany = \'"+toChange+"\' where InsuranceID = "+str(InsuranceID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{InsuranceID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Type Of Plan:")
                InsuranceID = int(input("Enter InsuranceID:  "))
                toChange = input("Enter Type Of Plan to be Upadated:  ")

                query = "update "+tableName+" set TypeofPlan = \'"+toChange+"\' where InsuranceID = "+str(InsuranceID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{InsuranceID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update StartDate:")
                InsuranceID = int(input("Enter InsuranceID:  "))
                toChange = input("Enter Start Date to be Upadated:  ")

                query = "update "+tableName+" set StartDate = \'"+toChange+"\' where InsuranceID = "+str(InsuranceID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{InsuranceID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update EndDate:")
                InsuranceID = int(input("Enter InsuranceID:  "))
                toChange = input("Enter End Date to be Upadated:  ")

                query = "update "+tableName+" set EndDates = \'"+toChange+"\' where InsuranceID = "+str(InsuranceID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{InsuranceID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()          
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteInsurance():
    try:
        print("Deleting Insurance")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        InsuranceID = input("Enter InsuranceID to DELETE Insurance: ")
        query = "delete from "+tableName+" where InsuranceID = "+InsuranceID+";"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Patient with Insurance ID {InsuranceID} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  InsuranceID = {InsuranceID} is refered by PatientDetails Table! Can't Delete.\n")

def printPatients(insurances):
    print("\n***** Insurance Details *****")
    print("+-------------+-----------------+------------+--------------+---------------+")
    print("| InsuranceID | InsuringCompany | TypeofPlan |   StartDate  |    EndDates   |")
    print("+-------------+-----------------+------------+--------------+---------------+")
    for insurance in insurances:
        p = list(insurance)
        print("\t",p[0],"\t\t",p[1],"\t",p[2],"\t",p[3],"\t",p[4])
        
    print("\n")



