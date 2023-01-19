import pandas as pd
import csv
Ledger = {
    "transactionId":[],
    "orderId":[],
    "accDate":[],
    "customerId":[],
    "value":[]     
} 


def readLedger():
    with open("./ledger.csv", 'r') as file:
        reader = csv.reader(file)
        for read in reader:
            Ledger["transactionId"].append(read[0])
            Ledger["orderId"].append(read[1])
            Ledger["accDate"].append(read[2])
            Ledger["customerId"].append(read[3])
            Ledger["value"].append(read[4])

        # print("Ledger:  ",Ledger)


def saveLedger():
    with open('./ledger.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(Ledger,columns=["transactionId","orderId","accDate","customerId","value"])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("File saved..!")


def clearLedger():
    Ledger["transactionId"].clear()
    Ledger["orderId"].clear()
    Ledger["accDate"].clear()
    Ledger["customerId"].clear()
    Ledger["value"].clear()
    # print("Cleared Ledger")