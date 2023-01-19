from lib import books
from result import libraryToCSV
from stud import students
from result import studentToCSV
from result import bookTransactionToCSV
from lib import bookTransaction
from lib import fine

def modifyCSV():
    # innerIterator = True
    # while innerIterator:
    #     try:
            # print("A. Store All Book Details to the CSV")
            # print("B. Don't Save For Now")
            # store = input("enter your choice:  ")
            # if(store=="A"):
    libraryToCSV.storeBookDetails(books.Books)
    books.Books["Name"].clear()
    books.Books["Author"].clear()
    books.Books["Price"].clear()
    books.Books["isAvailable"].clear()
    books.Books["bookCount"].clear()
    # innerIterator = False
        #     elif(store=="B"):
        #         innerIterator = False
        # except Exception as e:
        #     print("Please provide valid input: ",e.message)     
    # print("index of ite")

def modifyStudentCSV():
    # innerIterator = True
    # while innerIterator:
    #     try:
    #         print("A. Store All Students Details to the CSV")
    #         print("B. Don't Save For Now")
    #         store = input("enter your choice:  ")
    #         if(store=="A"):
    studentToCSV.storeStudentDetails(students.Students)
    students.Students["ID"].clear()
    students.Students["StudentName"].clear()
    students.Students["Class"].clear()
    students.Students["Dept"].clear()
        #         innerIterator = False
        #     elif(store=="B"):
        #         innerIterator = False
        # except Exception as e:
        #     print("Please provide valid input: ",e.message)     
    # print("index of ite")

def modifyBookTransactionCSV():
    # print("Inside Modifying book Transaction CSV")
    # innerIterator = True
    # while innerIterator:
    #     try:
    #         print("A. Store BookTransaction Students Details to the CSV")
    #         print("B. Don't Save For Now")
    #         store = input("enter your choice:  ")
    #         if(store=="A"):
    bookTransactionToCSV.storeBookTransactionDetails(bookTransaction.BookTransaction)
    bookTransaction.BookTransaction["StudentID"].clear()
    bookTransaction.BookTransaction["StudentName"].clear()
    bookTransaction.BookTransaction["StudentDept"].clear()
    bookTransaction.BookTransaction["BookName"].clear()
    bookTransaction.BookTransaction["Author"].clear()
    bookTransaction.BookTransaction["IssuedDate"].clear()
    bookTransaction.BookTransaction["ExpectedReturnDate"].clear()
    # bookTransaction.BookTransaction["Fine"].clear()
    # bookTransaction.BookTransaction["Status"].clear()
    # print("cleared Or not::: -->",bookTransaction.BookTransaction,"\n\n")
        #         innerIterator = False
        #     elif(store=="B"):
        #         innerIterator = False
        # except Exception as e:
        #     print("Please provide valid input: ",e.message)     
    # print("index of ite")

def modifyFineToCSV():
    fine.modifyFine()
    # fine.eraseMe()
    # print("At Last Fine--:",fine.Fine)


def newModifyCSV():
    if len(students.Students) > 0:
        studentToCSV.storeStudentDetails(students.Students)
    

def newModifyBookTransactionCSV():
    bookTransactionToCSV.storeBookTransactionDetails(bookTransaction.BookTransaction)

