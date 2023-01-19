import csv
import pandas as pd

Customers = {
    "customerId":[],
    "customerName":[],
    "customerAddress":[],
    "customerCredit":[]
}

def readCustomer():
    with open('./customers.csv','r') as file:
        reader = csv.reader(file)
        for read in reader:
            Customers["customerId"].append(read[0])
            Customers["customerName"].append(read[1])
            Customers["customerAddress"].append(read[2])
            Customers["customerCredit"].append(read[3])
        # print("Custmers:  ",Customers)

def addCustomer():
    print("Adding customer for you!")
    custId = input("Enter the Customer ID:  ")
    custName = input("Enter the Customer Name:  ")
    custAddress = input("Enter the Customer Address:  ")
    custCredit = float(input("Enter Customer Credit:  "))

    Customers["customerId"].append(custId)
    Customers["customerName"].append(custName)
    Customers["customerAddress"].append(custAddress)
    Customers["customerCredit"].append(custCredit)

    print("Customer Added SuccessFully!")


def saveCustomer():
    with open('./customers.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(Customers,columns=['customerId','customerName','customerAddress','customerCredit'])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
        # print("file is written and saved successfully!")

def clearCustomer():
    Customers["customerId"].clear()
    Customers["customerName"].clear()
    Customers["customerAddress"].clear()
    Customers["customerCredit"].clear()
    # print("cleared the customer: ",Customers)

def displayCustomer():
    readCustomer()
    df = pd.DataFrame(Customers,columns=['customerId','customerName','customerAddress','customerCredit'])
    print("\n**Customer List**\n")
    if df.empty:
        print("No Customers Data is Available. Please Add Customers")
    else:
        print(df)
    clearCustomer()

def updateCustomer():
    print("## Update Customer ##")
    i = True
    while i:
        try:
            print("1. update Customer ID\t\t2. update Customer Name\t\t3. update Customer Address\t\t4.update Customer Credit\n5. Exit")
            choice = int(input("Enter your choice:  "))
            if(choice == 1):
                readCustomer()
                custId = input("Enter current Customer ID:  ")
                id = Customers["customerId"].index(custId)
                updatedId = input("Enter Customer Id to be updated:  ")
                Customers["customerId"][id] = updatedId
                saveCustomer()
                clearCustomer()
            elif(choice == 2):
                readCustomer()
                custId = input("Enter current Customer ID:  ")
                id = Customers["customerId"].index(custId)
                updatedName = input("Enter Customer Name to be updated:  ")
                Customers["customerName"][id] = updatedName
                saveCustomer()
                clearCustomer()
            elif(choice == 3):
                readCustomer()
                custId = input("Enter current Customer ID:  ")
                id = Customers["customerId"].index(custId)
                updatedAddress = input("Enter Customer Address to be updated:  ")
                Customers["customerAddress"][id] = updatedAddress
                saveCustomer()
                clearCustomer()
            elif(choice == 4):
                readCustomer()
                custId = input("Enter current Customer ID:  ")
                id = Customers["customerId"].index(custId)
                updatedCredit = input("Enter Customer Credit to be updated:  ")
                Customers["customerCredit"][id] = updatedCredit
                saveCustomer()
                clearCustomer()
            
            elif(choice == 5):
                i = False
        except Exception as e:
            print("Please give a valid input",e)

def deleteCustomer():
    readCustomer()
    custId = input("Enter the Custome ID:  ")
    id = Customers["customerId"].index(custId)
    Customers["customerId"].pop(id)
    Customers["customerName"].pop(id)
    Customers["customerAddress"].pop(id)
    Customers["customerCredit"].pop(id)
    saveCustomer()
    clearCustomer()
    print("Customer is Deleted!")
