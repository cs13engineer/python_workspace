"""
    This Dictionary will get automatically updated on 
        1. Borrowing Book,
        2. Returning Book.
        3. Paying fine
"""
import csv
BookTransaction = {
    "StudentID":[],
    "StudentName":[],
    "StudentDept":[],
    "BookName":[],
    "Author":[],
    "IssuedDate":[],
    "ExpectedReturnDate":[]
    # "Fine":[],
    # "Status":[]
}

def readCSV():
    # print("Before add anything:",BookTransaction)
    with open('./bookTransaction.csv','r') as file:
        reader = csv.reader(file)
        # print("rows are extracted from csv")
        for read in reader:
            BookTransaction["StudentID"].append(read[0])
            BookTransaction["StudentName"].append(read[1])
            BookTransaction["StudentDept"].append(read[2])
            BookTransaction["BookName"].append(read[3])
            BookTransaction["Author"].append(read[4])
            BookTransaction["IssuedDate"].append(read[5])
            BookTransaction["ExpectedReturnDate"].append(read[6])
    # print("\nAfter adding everythng:",BookTransaction)
