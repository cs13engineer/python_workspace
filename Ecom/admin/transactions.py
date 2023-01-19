import csv
import pandas as pd
Transactions = {
    "transactionId":[],
    "orderId":[]
}

def readTransaction():
    # print("Reading")
    with open('./transactions.csv','r') as file:
        reader = csv.reader(file)
        for read in reader:
            Transactions["transactionId"].append(read[0])
            Transactions["orderId"].append(read[1])
    # print("Transactions: ",Transactions)


def addTransaction():
    print("adding")
    transId = input("Enter Transaction Id:  ")
    orderId = input("Enter Order Id:  ")
    Transactions["transactionId"].append(transId)
    Transactions["orderId"].append(orderId)
    # print("Transaction Added:  ",Transactions)

def saveTransaction():
    # print("saving")
    with open('./transactions.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(Transactions,columns=["transactionId","orderId"])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("Trasaction saved!")

def clearTrasaction():
    # print("clearing")
    Transactions["transactionId"].clear()
    Transactions["orderId"].clear()
    # print("Clear: ",Transactions)

def updateTransaction():
    print("updating")

def deleteTransaction():
    print("deleting")
    readTransaction()
    transId = input("Enter transaction Id:  ")
    idx = Transactions["transactionId"].index(transId)
    Transactions["transactionId"].pop(idx)
    Transactions["orderId"].pop(idx)
    saveTransaction()
    clearTrasaction()


# iter =True
# while iter:
    print("1. addTransaction\t2.saveTrasaction\t3.clearTrasaction\t4.Exit")
    try:
        ch = int(input("enter your choice:  "))
        if(ch == 1):
            readTransaction()
            addTransaction()
            saveTransaction()
            clearTrasaction()
        elif(ch == 3):
            deleteTransaction()
        else:
            iter = False
    except Exception as e:
        print("Excetion: ",e)