## will update books.csv after addition,deletion and updation of any details
import pandas as pd
import csv

def storeBookTransactionDetails(Dict):
    # print("storing book details",Dict)
    df = pd.DataFrame(Dict,columns = ['StudentID', 'StudentName', 'StudentDept','BookName', 'Author','IssuedDate', 'ExpectedReturnDate', 'Fine', 'Status'])
    # print("\n",df)
    with open('./bookTransaction.csv','w') as file:
        writer = csv.writer(file)
        
        idx = df.index
        # print("\n",idx)

        for id in idx:
            writer.writerow(df.loc[id])
        # print("Books data is saved Successfully!")

def ShowBookTransaction(Dict):
    # print("storing book details",Dict)
    df = pd.DataFrame(Dict,columns = ['StudentID', 'StudentName', 'StudentDept','BookName', 'Author','IssuedDate', 'ExpectedReturnDate'])
    if len(df) > 0:
        print("## List Of Issued Books ##")
        print("\n",df)
    else:
        print("\n\t## No Records Are Present ##\n")