import pandas as pd
import csv
AccountPay = {
    "transactionId":[],
    "orderId":[],
    "accDate":[],
    "customerId":[],
    "value":[]     
} 


def readPay():
    with open("./accPay.csv", 'r') as file:
        reader = csv.reader(file)
        for read in reader:
            AccountPay["transactionId"].append(read[0])
            AccountPay["orderId"].append(read[1])
            AccountPay["accDate"].append(read[2])
            AccountPay["customerId"].append(read[3])
            AccountPay["value"].append(read[4])

        # print("AccountPay:  ",AccountPay)


def savePay():
    with open('./accPay.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(AccountPay,columns=["transactionId","orderId","accDate","customerId","value"])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("File saved..!")


def clearPay():
    AccountPay["transactionId"].clear()
    AccountPay["orderId"].clear()
    AccountPay["accDate"].clear()
    AccountPay["customerId"].clear()
    AccountPay["value"].clear()
    # print("Cleared Pay")