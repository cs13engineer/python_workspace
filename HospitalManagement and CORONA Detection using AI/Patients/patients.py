from Database import connection
tableName = "PatientDetails"
"""
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| PatientId   | int         | NO   | PRI | NULL    |       |
| PatientName | varchar(50) | NO   |     | NULL    |       |
| PatientAddr | varchar(50) | NO   |     | NULL    |       |
| Email       | varchar(50) | YES  |     | NULL    |       |
| Zipcode     | int         | NO   |     | NULL    |       |
| TelNo       | varchar(50) | YES  |     | NULL    |       |
| InsuranceId | int         | YES  | MUL | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Patients")

def insertPatient():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nRegister Patient. Fill Patient Details\n")
        
        PatientId = input("Enter Patients ID: ")
        PatientName = input("Enter Patients Name: ")
        PatientAddr = input("Enter Patients Address: ")
        Email = input("Enter Patients email: ")
        Zipcode = int(input("Enter Patients zip-code: "))
        TelNo = input("Enter Patients telphone number: ")
        InsuranceId = int(input("Enter Patients Insurance ID: "))

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s,%s,%s);"
        print("Operational Query:=> ",query)
        values = (PatientId,PatientName,PatientAddr,Email,Zipcode,TelNo,InsuranceId)

        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        # print("Inserting Patients")
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0] == '1452'):
            print(f"\nWARNING: Add InsuranceInfo First with InsuranceID = {InsuranceId}")
        elif(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate patientID::  {PatientId} is already present!")
        else:
            print("ERROR: ",e)
def displayPatients():
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
    
def updatePatients():
    
    print("Update Patients")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update Patients ID.\n2. Update Patients Name\n3. Update Patients Address\n4. Update Patients Email\n5. Update Patient zip-code.\n6. Update Patient telNo.\n7. Update Patient Insurance ID.\n8. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient ID:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = int(input("Enter Patient ID to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set PatientID = "+str(toChange)+" where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient Name:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = input("Enter Patient Name to be Upadated:  ")

                query = "update "+tableName+" set PatientName = \'"+toChange+"\' where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient Address:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = input("Enter Patient Address to be Upadated:  ")

                query = "update "+tableName+" set PatientAddr = \'"+toChange+"\' where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient email:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = input("Enter Patient Email to be Upadated:  ")

                query = "update "+tableName+" set Email = \'"+toChange+"\' where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient zip:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = int(input("Enter Patient Zipcode to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set Zipcode = "+str(toChange)+" where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 6):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient tel:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = input("Enter Patient TelNo to be Upadated:  ")

                query = "update "+tableName+" set TelNo = \'"+toChange+"\' where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 7):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Patient Insurance ID:")
                patientID = int(input("Enter Patient ID:  "))
                toChange = int(input("Enter Patient InsuranceId to be Upadated:  "))
                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set InsuranceId = "+str(toChange)+" where PatientID = "+str(patientID)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{patientID} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            
            elif(ch == 8):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deletePatients():
    try:
        print("Deleting Patients")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        patientID = input("Enter Patient ID to DELETE patient")
        query = "delete from "+tableName+" where patientID = "+patientID+";"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Patient with Patient ID {patientID} is Deleted from the record")
    except Exception as e:
        print("ERROR: ",e)

def printPatients(patients):
    print("\n***** Patients Details *****")
    print("+-----------+----------------------+----------------+-----------------+---------+--------------+-------------+")
    print("| patientID | patientName          | patientAddress | email           | zipCode | telNo        | insuranceId |")
    print("+-----------+----------------------+----------------+-----------------+---------+--------------+-------------+")
    for patient in patients:
        p = list(patient)
        print("\t",p[0],p[1],"\t",p[2],"\t",p[3],"\t",p[4],"\t",p[5],"\t",p[6])
        
    print("\n")
