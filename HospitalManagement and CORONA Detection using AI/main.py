from Database import connection
from Patients import patients
from Patients import insurance
from Patients import feedback
from Doctors import doctors
from Doctors import nurses
from Doctors import canteen
from Doctors import ambulance
from Doctors import mis
from ML import corona 
from ML import chronic

iterator = True
while iterator:
    print("\n***Hospital Management****\n")
    print("1. Patient Section\t\t2.Doctor Section\n3. MIS Reports.     \t\t4. ML Algorithm.\n5. EXIT\n")
    try:
        choice = int(input("Enter Your Choice:  "))
        
        if(choice == 1):
            iterator1 = True
            while iterator1:
                print("\n***** Patient's Section *****")
                print("1. Insurance Details\t\t2. Patients Details.\n3. Patient Feedback\t\t4. Exit\n")
                try:
                    choice = int(input("Enter your choice:  "))
                    if(choice == 1):
                        iterator11 = True
                        while iterator11:

                            print("\n*****Insurance Information*****")
                            try:
                                print("\n1. Insert Insurance\t\t2. Display Insurance.\n3. Update Insurance\t\t4. DELETE Insurance\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    insurance.insertInsurance()
                                    # patients.insertPatient()
                                elif(ch == 2):
                                    insurance.displayInsurance()
                                elif(ch == 3):
                                    insurance.updateInsurance()
                                elif(ch == 4):
                                    insurance.deleteInsurance()
                                elif(ch == 5):
                                    print("Exiting :42:")
                                    iterator11 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 2):
                        iterator12 = True
                        while iterator12:

                            try:
                                print("\n1. Insert Patient\t\t2. Display Patients.\n3. Update Patient\t\t4. DELETE Patient\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    patients.insertPatient()
                                elif(ch == 2):
                                    patients.displayPatients()
                                elif(ch == 3):
                                    patients.updatePatients()
                                elif(ch == 4):
                                    patients.deletePatients()
                                elif(ch == 5):
                                    print("Exiting :63:")
                                    iterator12 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 3):
                        
                        iterator12 = True
                        while iterator12:
                            print("\n***** Feedback *****")
                            try:
                                print("\n1. Insert Feedback\t\t2. Display Feedbacks.\n3. Update Feedback\t\t4. DELETE Feedback\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    feedback.insertFeedback()
                                elif(ch == 2):
                                    feedback.displayFeedback()
                                elif(ch == 3):
                                    feedback.updateFeedback()
                                elif(ch == 4):
                                    feedback.deleteFeedback()
                                elif(ch == 5):
                                    print("Exiting :63:")
                                    iterator12 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 4):
                        iterator1 = False
                        print("Exiting Patient Details")
                except Exception as e:
                        print("ERROR: ",e)
        elif(choice == 2):
            iterator1 = True
            while iterator1:
                print("\n***** Patient's Section *****")
                print("1. Doctors Details\t\t2. Nurse Details.\n3. Ambulance\t\t4. Canteen\n5. EXIT")
                try:
                    choice = int(input("Enter your choice:  "))
                    if(choice == 1):
                        iterator11 = True
                        while iterator11:

                            print("\n*****Doctors Information*****")
                            try:
                                print("\n1. Insert Doctor\t\t2. Display Doctor.\n3. Update Doctor\t\t4. DELETE Doctor\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    doctors.insertDoctor()
                                elif(ch == 2):
                                    doctors.displayDoctor()
                                elif(ch == 3):
                                    doctors.updateDoctor()
                                elif(ch == 4):
                                    doctors.deleteDoctor()
                                elif(ch == 5):
                                    print("Exiting :42:")
                                    iterator11 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 2):
                        iterator12 = True
                        while iterator12:
                            print("\n*****Nurse Information*****")
                            try:
                                print("\n1. Insert Nurse\t\t2. Display Nurse.\n3. Update Nurse\t\t4. DELETE Nurse\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    nurses.insertNurse()
                                elif(ch == 2):
                                    nurses.displayNurse()
                                elif(ch == 3):
                                    nurses.updateNurse()
                                elif(ch == 4):
                                    nurses.deleteNurse()
                                elif(ch == 5):
                                    print("Exiting :63:")
                                    iterator12 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 3):
                        
                        iterator12 = True
                        while iterator12:
                            print("\n***** Ambulance *****")
                            try:
                                print("\n1. Insert Ambulance\t\t2. Display Ambulance.\n3. Update Ambulance\t\t4. DELETE Ambulance\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    ambulance.insertAmbulance()
                                elif(ch == 2):
                                    ambulance.displayAmbulance()
                                elif(ch == 3):
                                    ambulance.updateAmbulance()
                                elif(ch == 4):
                                    ambulance.deleteAmbulance()
                                elif(ch == 5):
                                    print("Exiting :63:")
                                    iterator12 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 4):
                        
                        iterator12 = True
                        while iterator12:
                            print("\n***** Canteen Information *****")
                            try:
                                print("\n1. Insert Canteen Information\t\t2. Display Canteen Information.\n3. Update Canteen Information\t\t4. DELETE Canteen Information\n5. Exit\n")
                                ch = int(input("Enter Your Choice:  "))

                                if(ch == 1):
                                    canteen.insertCanteen()
                                elif(ch == 2):
                                    canteen.displayCanteen()
                                elif(ch == 3):
                                    canteen.updateCanteen()
                                elif(ch == 4):
                                    canteen.deleteCanteen()
                                elif(ch == 5):
                                    print("Exiting :63:")
                                    iterator12 = False
                            except Exception as e:
                                print("ERROR: ",e)
                    elif(choice == 5):
                        iterator1 = False
                        print("Exiting Patient Details")
                except Exception as e:
                        print("ERROR: ",e)
        elif(choice == 3):
            
            iterator111 = True
            while iterator111:
                try:
                    print("\n***** MIS Report *****")
                    print("\n1. Patients With Similar Disease\t2. Consultants info treating patients and their disease types.\n\n3. Sum(payment) made by patient to date.\t4. nsurance Information for a patient whose date wise.\n\n5. Feedback details by patients.\t6. Nurse Details – DoctorWise – Patientwise.\n\n7. Operation Details performed by doctors.\t8. Asset Information – satisfaction wise – percentages.\n\n9. Disease details – patient wise.\t10. Depreciation of Assets through the year.\n\n11. EXIT\n")
                    c = int(input("enter your choice: "))
                    if(c == 1):
                        
                        print("\n **** Patients With Similar Disease ****\n")
                        mis.one()
                    elif(c == 2):
                        print("\n **** Consultants info treating patients and their disease types ****\n")
                        mis.two()
                    elif(c == 3):
                        print("\n **** Sum(payment) made by patient to date ****\n")
                        mis.three()
                    elif(c == 4):
                        print("\n **** Insurance Information for a patient whose date wise ****\n")
                        mis.four()
                    elif(c == 5):
                        print("\n **** Feedback details by patients ****\n")
                        mis.five()
                    elif(c == 6):
                        print("\n **** Nurse Details – DoctorWise – Patientwise ****\n")
                        mis.six()
                    elif(c == 7):
                        print("\n **** Operation Details performed by doctors ****\n")
                        mis.seven()
                    elif(c == 8):
                        print("\n **** Asset Information – satisfaction wise – percentages ****\n")
                        mis.eight()
                    elif(c == 9):
                        print("\n **** Disease details – patient wise ****\n")
                        mis.nine()
                    elif(c == 10):
                        print("\n **** Depreciation of Assets through the year ****\n")
                        mis.ten()
                    elif(c ==  11):
                        iterator111 = False
                except Exception as e:
                    print("ERROR: ",e)
        elif(choice == 4):
            print("\n**** ML Algorithms **** ")
            # corona.test()
            ml_iter = True
            while ml_iter:
                print("\n1. Chronic.\t\t2. Corona.\t\t3. Exit\n")
                try:
                    inp = int(input("Enter your choice:  "))

                    if(inp == 1):
                        print("\n**** Chronic ******")
                        chronic.Chronic()
                    elif(inp == 2):
                        print("\n**** Corona ******")
                        corona.Corona()
                    elif(inp == 3):
                        print("\n***** Exiting ML Algorithm ******")
                        ml_iter = False
                except Exception as e:
                    print("ERROR: ",e)
        elif(choice == 5):
            print("Exiting App\n")
            iterator = False 
    except Exception as e:
        print("ERROR: ",e)

# print(connection.ConnectDB)