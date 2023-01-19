from Database import connection
tableName = "Feedbacks"
"""
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| FeedbackId | int         | NO   | PRI | NULL    |       |
| FeedbackOn | varchar(50) | NO   |     | NULL    |       |
| Texts      | varchar(50) | NO   |     | NULL    |       |
| Dates      | date        | YES  |     | NULL    |       |
| PatientId  | int         | YES  | MUL | NULL    |       |
+------------+-------------+------+-----+---------+-------+
"""
def test():
    print("Testing Feedbacks")

def insertFeedback():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        print("\nFill Feedback Details\n")
        
        FeedbackId = int(input("Enter FeedbackId: "))
        FeedbackOn = input("\nEnter FeedbackOn:\n(Hospital Staff || Doctors || Hospital Facilities[Canteen/Ambulance]): ")
        Texts = input("Enter Texts: ")
        Dates = input("Enter Dates: ")
        PatientId = input("Enter PatientId: ")
       

        query = "insert into "+tableName+" values(%s,%s,%s,%s,%s);"
        print("Operational Query:=> ",query)
        values = (FeedbackId,FeedbackOn,Texts,Dates,PatientId)

        dbCursor.execute(query,values)
        db.commit()
        db.close()
        print("\n",dbCursor.rowcount," row is inserted\n")
        
    except Exception as e:
        # print("ERROR: ",e)
        msg = str(e).split(' ')
        if(msg[0]== '1062'):
            print(f"\nWARNING: Duplicate FeedbackId::  {FeedbackId} is already present!\n")
        elif(msg[0] == '1452'):
            print(f"\nCannot add or update a child row: a foreign key constraint fails. \nPatient is Not Available with patiendID: {PatientId}.")
        else:
            print("ERROR: ",e)
def displayFeedback():
    try:
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        query = "select * from "+tableName+";"
        dbCursor.execute(query)
        result = dbCursor.fetchall()
        printFeedback(result)
        db.close()


    except Exception as e:
        print("ERROR: ",e)
    # print("Displaying Patients")
    
def updateFeedback():
    
    print("Update Feedbacks")
    "need to update each value"
    i = True
    while i:
        print("\n1. Update FeedbackId.\n2. Update FeedbackOn\n3. Update Texts\n4. Update Dates\n5. Update PatientId\n6. EXIT\n")
        try: 
            ch = int(input("Enter Your choice:  "))
            if(ch == 1):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update FeedbackId:")
                FeedbackId = int(input("Enter FeedbackId:  "))
                toChange = int(input("Enter FeedbackId to be Upadated:  "))

                # query = "update "+tableName+" set patientID = "+str(toChange)+" where patientName = \'"+patientName+"\';"
                query = "update "+tableName+" set FeedbackId = "+str(toChange)+" where FeedbackId = "+str(FeedbackId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{FeedbackId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
                # print(result)
            elif(ch == 2):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update FeedbackOn:")
                FeedbackId = int(input("Enter FeedbackId:  "))
                toChange = input("Enter FeedbackOn to be Upadated:  ")

                query = "update "+tableName+" set FeedbackOn = \'"+toChange+"\' where FeedbackId = "+str(FeedbackId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{FeedbackId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 3):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Texts:")
                FeedbackId = int(input("Enter FeedbackId:  "))
                toChange = input("Enter Texts to be Upadated:  ")

                query = "update "+tableName+" set Texts = \'"+toChange+"\' where FeedbackId = "+str(FeedbackId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{FeedbackId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 4):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update Dates:")
                FeedbackId = int(input("Enter FeedbackId:  "))
                toChange = input("Enter Date to be Upadated:  ")

                query = "update "+tableName+" set Dates = \'"+toChange+"\' where FeedbackId = "+str(FeedbackId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{FeedbackId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()
            elif(ch == 5):
                db = connection.ConnectDB()
                dbCursor = db.cursor()
                print("Update PatientId:")
                FeedbackId = int(input("Enter FeedbackId:  "))
                toChange = input("Enter PatientId to be Upadated:  ")

                query = "update "+tableName+" set PatientId = "+toChange+" where FeedbackId = "+str(FeedbackId)+";"
                print("\noperation Query:=> ",query)
                dbCursor.execute(query)
                db.commit()
                print(f"{FeedbackId} updated Sucessfully!")
                db.close()
                result = dbCursor.fetchall()          
            elif(ch == 6):
                i = False
                print("Exiting")
        except Exception as e:
            print("ERROR: ",e)

def deleteFeedback():
    try:
        print("Deleting Insurance")
        db = connection.ConnectDB()
        dbCursor = db.cursor()
        FeedbackId = input("Enter FeedbackId to DELETE Feedback: ")
        query = "delete from "+tableName+" where FeedbackId = "+FeedbackId+";"
        print("\noperation Query:=> ",query)
        dbCursor.execute(query)
        
        db.commit()
        db.close()
        print(f"Patient with Feedback ID {FeedbackId} is Deleted from the record")
    except Exception as e:
        msg = str(e).split(' ')
        if(msg[0]== '1451'):
            print(f"\nWARNING: Reference Error::  InsuranceID = {InsuranceID} is refered by PatientDetails Table! Can't Delete.\n")

def printFeedback(feedbacks):
    print("\n***** Feedback Details *****")
    print("+------------+------------+----------------------------+------------+-----------+")
    print("| FeedbackId | FeedbackOn | Texts                      | Dates      | PatientId |")
    print("+------------+------------+----------------------------+------------+-----------+")
    for feedback in feedbacks:
        p = list(feedback)
        print("   ",p[0],"    ",p[1],"\t",p[2],"\t",p[3],"\t",p[4])
        
    print("\n")





