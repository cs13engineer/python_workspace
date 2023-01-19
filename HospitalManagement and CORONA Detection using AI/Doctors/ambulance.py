from Database import connection
tableName = "ambulance"
"""
+-----------------------+-----------------------------+------+-----+---------+-------+
| Field                 | Type                        | Null | Key | Default | Extra |
+-----------------------+-----------------------------+------+-----+---------+-------+
| vanNumber             | varchar(20)                 | NO   | PRI | NULL    |       |
| ambulanceType         | enum('Equiped','Unequiped') | YES  |     | NULL    |       |
| driverName            | varchar(40)                 | YES  |     | NULL    |       |
| driverContact         | int                         | YES  |     | NULL    |       |
| associateHospitalName | varchar(50)                 | YES  |     | NULL    |       |
+-----------------------+-----------------------------+------+-----+---------+-------+
"""
def test():
    print("Testing Ambulance")

def insertAmbulance():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Ambulance Details\n")
        
        vanNumber = input("Enter vanNumber: ")
        ambulanceType = input("Enter ambulanceType ('Equiped','Unequiped'): ")
        driverName = input("Enter driverName: ")
        driverContact = int(input("Enter driverContact: "))
        associateHospitalName = input("Enter associateHospitalName: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s);"
        
        values = (vanNumber,ambulanceType,driverName,driverContact,associateHospitalName)
        print("Operational Query:=> ",query,values)
        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate vanNumber::  {vanNumber} is already present!\n")
        else:
            print("ERROR: ",e)
def displayAmbulance():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printAmbulance(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateAmbulance():
    
    print("Update Nurses")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update vanNumber.\n2. Update ambulanceType\n3. Update driverName\n4. Update driverContact\n5. Update associateHospitalName\n6. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update vanNumber:")
                vanNumber = input("Enter vanNumber:  ")
                toChange = input("Enter vanNumber to be Upadated:  ")

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set vanNumber = \'"+toChange+"\' where vanNumber = \'"+vanNumber+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{vanNumber} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update ambulanceType:")
                vanNumber = input("Enter vanNumber:  ")
                toChange = input("Enter ambulanceType ('Equiped','Unequiped'):  ")

                query = "update "+tableName+" set ambulanceType = \'"+toChange+"\' where vanNumber = \'"+vanNumber+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{vanNumber} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update driverName:")
                vanNumber = input("Enter vanNumber:  ")
                toChange = input("Enter driverName to be Upadated:  ")

                query = "update "+tableName+" set driverName = \'"+toChange+"\' where vanNumber = \'"+vanNumber+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{vanNumber} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update driverContact:")
                vanNumber = input("Enter vanNumber:  ")
                toChange = input("Enter driverContact to be Upadated:  ")

                query = "update "+tableName+" set driverContact = "+toChange+" where vanNumber = \'"+vanNumber+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{vanNumber} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update associateHospitalName:")
                vanNumber = input("Enter vanNumber:  ")
                toChange = input("Enter associateHospitalName to be Upadated:  ")

                query = "update "+tableName+" set associateHospitalName = \'"+toChange+"\' where vanNumber = \'"+vanNumber+"\';"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{vanNumber} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()          
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteAmbulance():
    try:
        print("Deleting Ambulance")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        vanNumber = input("Enter vanNumber to DELETE Amblance: ")
        query = "delete from "+tableName+" where vanNumber = \'"+vanNumber+"\';"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Ambulance with vanNumber {vanNumber} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  vanNumber = {vanNumber} is refered by PatientDetails Table! Can't Delete.\n")
        else:
            print("ERROR: ",e)
def printAmbulance(ambulances):
    print("\n***** Ambulance Details *****")
    print("+---------------+---------------+------------+---------------+-----------------------+")
    print("| vanNumber     | ambulanceType | driverName | driverContact | associateHospitalName |")
    print("+---------------+---------------+------------+---------------+-----------------------+")
    for ambulance in ambulances:
        p = list(ambulance)
        print(p[0],"\t",p[1],"\t",p[2],"\t",p[3],"\t",p[4])
        
    print("\n")





