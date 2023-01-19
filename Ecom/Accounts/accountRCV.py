import pandas as pd
import csv
AccountRCV = {
    "transactionId":[],
    "orderId":[],
    "accDate":[],
    "customerId":[],
    "value":[]     
} 


def readRCV():
    with open("./accRCV.csv", 'r') as file:
        reader = csv.reader(file)
        for read in reader:
            AccountRCV["transactionId"].append(read[0])
            AccountRCV["orderId"].append(read[1])
            AccountRCV["accDate"].append(read[2])
            AccountRCV["customerId"].append(read[3])
            AccountRCV["value"].append(read[4])

        # print("AccountRCV:  ",AccountRCV)


def saveRCV():
    with open('./accRCV.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(AccountRCV,columns=["transactionId","orderId","accDate","customerId","value"])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("File saved..!")


def clearRCV():
    AccountRCV["transactionId"].clear()
    AccountRCV["orderId"].clear()
    AccountRCV["accDate"].clear()
    AccountRCV["customerId"].clear()
    AccountRCV["value"].clear()
    # print("Cleared RCV")

def test():
    print("testing..!")