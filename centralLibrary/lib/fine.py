import csv
import pandas as pd
Fine = {
    "StudentID":[],
    "StudentName":[],
    "BookName":[],
    "Amount":[],
    "ReturnDate":[],
    "DueDate":[],
    "TimeElapsed":[]
}

def readCSV():
    with open('./fine.csv','r') as file:
        reader = csv.reader(file)
        for read in reader:
            Fine["StudentID"].append(read[0])
            Fine["StudentName"].append(read[1])
            Fine["BookName"].append(read[2])
            Fine["Amount"].append(read[3])
            Fine["ReturnDate"].append(read[4])
            Fine["DueDate"].append(read[5])
            Fine["TimeElapsed"].append(read[6])  

def eraseMe():
    Fine["StudentID"].clear()
    Fine["StudentName"].clear()
    Fine["BookName"].clear()
    Fine["Amount"].clear()
    Fine["ReturnDate"].clear()
    Fine["DueDate"].clear()
    Fine["TimeElapsed"].clear()

# print("Reading CSV")
# readCSV()
# print("This is the reasult::-->",Fine)
# print("Clearing CSV")
# eraseMe()
# print("This is the reasult::-->",Fine)

def modifyFine():
    df = pd.DataFrame(Fine,columns=['StudentID','StudentName','BookName','Amount','ReturnDate','DueDate','TimeElapsed'])
    with open('./fine.csv','w') as file:
        writer = csv.writer(file)
        
        idx = df.index
        # print("\n",idx)

        for id in idx:
            writer.writerow(df.loc[id])
        # print("Fine data is saved Successfully!")

def showFine():
    df = pd.DataFrame(Fine,columns=['StudentID',    'StudentName',    'BookName',    'Amount',    'ReturnDate',    'DueDate',    'TimeElapsed'])
    print("\n\t\t####  Fine Details ####")
    print("\n\n",df)
    print('\n')

    