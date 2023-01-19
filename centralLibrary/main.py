from lib import books
from stud import students
from result import libraryToCSV
from toCSV import saveToCSV
from lib import bookTransaction
from result import bookTransactionToCSV
from lib import fine
# books.addBooks()
# print("my books are: ",books.Books)
iterator = True
while iterator:
    try:
        print("### Welocome To Library Management System ###")
        print("\n1. Libray",end="\t")
        print("2. Student", end="\t")
        print("3. Exit\n")
        choice = int(input("enter your choice: "))
        if(choice == 1):
            iterator1 = True
            while iterator1:
                try:
                    print("\n### Central Library ###")
                    print("\n\ta. Add Book", end="\t\t")
                    print("b. Delete Book", end="\t\t")
                    print("c. Fine Student",end="\t\t")
                    print("d. Add Student",end="\t\t")
                    print("e. Borrowed Book Status\n")
                    print("\tf. List Students \n")
                    print("Press any key to Exit\n")
                    ch = input("select one: ")
                    if(ch=='a'):
                        print("\n## Enter Book Details ##")
                        books.readCSV()
                        books.addBooks()
                        # print("my books are: ",books.Books)
                        saveToCSV.modifyCSV()
                    elif(ch=='b'):
                        print("Deleting...")
                        books.readCSV()
                        toDelete = input("enter book name to delete: ")
                        books.findIndex(toDelete)
                        print("After Deletion:\n")
                        # print("my books are: ",books.Books)
                        saveToCSV.modifyCSV()
                        books.clearMyBooks()
                    elif(ch=='c'):
                        fine.readCSV()
                        #Function to display
                        fine.showFine()
                        fine.eraseMe()
                    elif(ch == 'd'):
                        print("Adding Student")
                        students.readCSV()
                        students.addStudent()
                        saveToCSV.modifyStudentCSV()
                    elif(ch == 'e'):
                        bookTransaction.readCSV()
                        bookTransactionToCSV.ShowBookTransaction(bookTransaction.BookTransaction)
                    elif(ch == 'f'):
                        students.readCSV()
                        students.displayStudent()
                        students.clearStudent()
                    else:
                        iterator1 = False
                except Exception as e:
                    print("Please provide valid input:  ",e)
            print("Exiting from the Library..")
        elif(choice == 2):
            iterator2 = True
            while iterator2:
                try:
                    print("\na. Borrow Book ",end=" ")
                    print("b. Return Book ",end=" ")
                    print("c. Pay Fine ",end=" ")
                    print("d. List Available Books")
                    print("\n**Press any key to Exit\n")
                    c = input("enter your choice: ")
                    if(c == 'a'):
                        students.NewBorrow()
                    elif(c == 'b'):
                        students.NewReturnBook()
                    elif(c == 'c'):
                        print("Paying fine...")
                        students.payingFine()
                    elif(c == 'd'):
                        print("Listing Available books")
                        books.listBooks()
                        
                    else:
                        iterator2 = False
                except Exception as e:
                    print("Please provide valid input",e)
            print("Exiting From the Student..")
        else:
            iterator = False
            
    except Exception as e:
        print("Please provide valid input:  ",e)
print("Exiting from App..")

def A():
        BookTransaction["StudentID"].append(read[0])
        BookTransaction["StudentName"].append(read[1])
        BookTransaction["StudentDept"].append(read[2])
        BookTransaction["BookName"].append(read[3])
        BookTransaction["Author"].append(read[4])
        BookTransaction["IssuedDate"].append(read[6])
        BookTransaction["ExpectedReturnDate"].append(read[7])