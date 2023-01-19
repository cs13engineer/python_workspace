# from lib import books
from datetime import datetime
from datetime import timedelta
from datetime import date
from lib import bookTransaction
from lib import books
from toCSV import saveToCSV
from lib import fine
import pandas as pd
import csv

beginingDate = date.today()
Enddate = beginingDate + timedelta(days=10)

Students={
    "ID":[],
    "StudentName":[],
    "Class":[],
    "Dept":[]
}

def readCSV():
    # print("Hello")
    # print("Before add anything:",Students)
    with open('./students.csv','r') as file:
        reader = csv.reader(file)
        # print("rows are extracted from csv")
        for read in reader:
            Students["ID"].append(read[0])
            Students["StudentName"].append(read[1])
            Students["Class"].append(read[2])
            Students["Dept"].append(read[3])
    # print("After adding everythng:",Students)

def addStudent():
    print("Inside Students.py adding students")
    ID = input("Enter Student Id: ")
    studName = input("Enter Student Name: ")
    Class = input("Enter Class: ")
    dept = input("Enter Department Name: ")
    print(ID,studName,Class,dept)
    """
        Adding student information to Students dictionary!
    """
    Students["ID"].append(ID)
    Students["StudentName"].append(studName)
    Students["Class"].append(Class)
    Students["Dept"].append(dept)
    
def clearStudent():
    Students["ID"].clear()
    Students["StudentName"].clear()
    Students["Class"].clear()
    Students["Dept"].clear()

def payingFine():
    print("paying fine")

def ClearTransaction():
    bookTransaction.BookTransaction["StudentID"].clear()
    bookTransaction.BookTransaction["StudentName"].clear()
    bookTransaction.BookTransaction["StudentDept"].clear()
    bookTransaction.BookTransaction["BookName"].clear()
    bookTransaction.BookTransaction["Author"].clear()
    bookTransaction.BookTransaction["IssuedDate"].clear()
    bookTransaction.BookTransaction["ExpectedReturnDate"].clear()
    # bookTransaction.BookTransaction["Fine"].clear()
    # bookTransaction.BookTransaction["Status"].clear()
    # print("cleared Or not::: -->",bookTransaction.BookTransaction)

def displayStudent():
    df = pd.DataFrame(Students, columns=['ID','StudentName','Class','Dept'])
    if len(df) > 0:
        print("## List Students ##")
        print("\n",df)
    else:
        print("\n\t## No Records Are Present ##\n")

def NewBorrow():
    # print("Borrowing")
    #readBook from csv
    books.readCSV()
    readCSV()
    #check by name
    book = input("enter book Name: ")
    i = books.Books["Name"].index(book)
    studentID = input("enter student ID: ")
    sI = Students["ID"].index(studentID)
    # print(type(sI),type(index))

    # print("isAvailable", )
    total = int(books.Books["bookCount"][i])
    # print("total",type(total))
    if(books.Books["isAvailable"][i] == 'True'):
        if (books.Books["bookCount"][i] == '1'):
            total = total - 1
            books.Books["bookCount"][i] = total
            books.Books["isAvailable"][i] = 'False'
        else:
            total = total - 1
            books.Books["bookCount"][i] = total
        bookTransaction.readCSV()
        bookTransaction.BookTransaction["StudentID"].append(Students["ID"][sI])
        bookTransaction.BookTransaction["StudentName"].append(Students["StudentName"][sI])
        bookTransaction.BookTransaction["StudentDept"].append(Students["Dept"][sI])
        bookTransaction.BookTransaction["BookName"].append(books.Books["Name"][i])
        bookTransaction.BookTransaction["Author"].append(books.Books["Author"][i])
        bookTransaction.BookTransaction["IssuedDate"].append(beginingDate)
        bookTransaction.BookTransaction["ExpectedReturnDate"].append(Enddate)
            # print(bookTransaction.BookTransaction)
        saveToCSV.newModifyBookTransactionCSV()
        saveToCSV.modifyCSV()
        # print("this is uncleared: ",bookTransaction.BookTransaction)
        ClearTransaction()
        books.clearMyBooks()
        clearStudent()
        # print("this is cleared: ",bookTransaction.BookTransaction)
        print(book+" Issued Successfylly to: "+studentID)
       
            
    else:
        print("Book is not available")
    books.clearMyBooks()#clear compulsory
    
def NewReturnBook():
    print("\nThis is NewReturnBook() and we are returning..")
    # print("Only I need BookTransaction, Books and FIne Dictionaries. ")
    
    studentID = input("Enter student ID: ")
    bookToReturn = input("Enter Name of Book to Return: ")
    
    ## readCSV --> Student and readCSV--> Books
    readCSV()# reading students
    # print("\nSudents Are: ",Students)
    
    # clearStudent()## to Clear students
    # print("After Clearance Sudents Are: ",Students)
    
    books.readCSV()
    # print("\nBooks are : ",books.Books)

    bookTransaction.readCSV()
    # print("\nBookTransactions after read are : ",bookTransaction.BookTransaction)
    
    # ClearTransaction()
    # print("\nBookTransactions after read are : ",bookTransaction.BookTransaction)

    # books.clearMyBooks()
    # print("After Clearance Books Are: ",books.Books)
    SID = Students["ID"].index(studentID) 
    BID = books.Books["Name"].index(bookToReturn)
    BTID = bookTransaction.BookTransaction["StudentID"].index(studentID)
    BTBID = bookTransaction.BookTransaction["BookName"].index(bookToReturn)

    # print("\nStudent ID index is: ",SID," and Index Of Book to be Return: ",BID)
    
    returningDate = datetime.strptime(bookTransaction.BookTransaction["ExpectedReturnDate"][BTBID], "%Y-%m-%d")
    today = datetime.strptime(str(date.today()), "%Y-%m-%d")
    # print(returningDate,today)

    length = len(bookTransaction.BookTransaction["StudentID"])
    for i in range(length):
        # print(i)
        
        if((bookTransaction.BookTransaction["StudentID"][i]==studentID) and (bookTransaction.BookTransaction["BookName"][i]==bookToReturn)):
            print(i," and ",i)
            #open fine.Fine={}
           
            fine.readCSV()
            fine.Fine["StudentID"].append(bookTransaction.BookTransaction["StudentID"][i])
            fine.Fine["StudentName"].append(bookTransaction.BookTransaction["StudentName"][i])
            fine.Fine["BookName"].append(bookTransaction.BookTransaction["BookName"][i])
            FineAmount = 0
            DayElapsed = 0
            perDayCharge = 2
            if(today<=returningDate):
                FineAmount = 0
                DayElapsed = 0

            if(today>returningDate):
                difference = str(today-returningDate)
                arr = difference.split(' ')
                DayElapsed = int(arr[0])
                FineAmount = DayElapsed * perDayCharge
            
            fine.Fine["Amount"].append(FineAmount)
            
            fine.Fine["ReturnDate"].append(date.today())
            fine.Fine["DueDate"].append(bookTransaction.BookTransaction["ExpectedReturnDate"][i])
            fine.Fine["TimeElapsed"].append(DayElapsed)
            
            #update fine.Fine={},  calculate the fine
            saveToCSV.modifyFineToCSV()
            #close fine.Fine={}
            fine.eraseMe()
            #modify book
            total=int(books.Books["bookCount"][BID])
            if(books.Books["isAvailable"][BID] == 'True'):
                total = total + 1
                books.Books["bookCount"][BID] = total
                saveToCSV.modifyCSV()
                books.clearMyBooks()
            else:
                books.Books["isAvailable"][BID] = 'True'
                total = total + 1
                books.Books["bookCount"][BID] = total
                saveToCSV.modifyCSV()
                books.clearMyBooks()
            #payFine
            
            bookTransaction.BookTransaction["StudentID"].pop(i)
            bookTransaction.BookTransaction["StudentName"].pop(i)
            bookTransaction.BookTransaction["StudentDept"].pop(i)
            bookTransaction.BookTransaction["BookName"].pop(i)
            bookTransaction.BookTransaction["Author"].pop(i)
            bookTransaction.BookTransaction["IssuedDate"].pop(i)
            bookTransaction.BookTransaction["ExpectedReturnDate"].pop(i)
            saveToCSV.modifyBookTransactionCSV()
            ClearTransaction()
            print("\n",bookToReturn,"Returned Successfully!")        
        else:
            print("Not Present")
            

    
    clearStudent()
    ClearTransaction()
    books.clearMyBooks()
    fine.eraseMe()
    """
        compulsory Erase following Dictionaries
        |-->Books
        |-->BookTransaction
        |-->Fine
    """
