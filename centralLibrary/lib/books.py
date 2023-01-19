import csv

Books={"Name":[],"Author":[],"Price":[],"isAvailable":[],"bookCount":[]}

def readCSV():
    # print("Before add anything:-->",Books)
    with open('./books.csv','r') as file:
        reader = csv.reader(file)
        # print("rows are extracted from csv")
        # print(reader)
        for read in reader:
            # print(read)
            Books["Name"].append(read[0])
            Books["Author"].append(read[1])
            Books["Price"].append(read[2])
            Books["isAvailable"].append(read[3])
            Books["bookCount"].append(read[4])
    print("After adding everythng:",Books)


def addBooks():
    bookName = input("enter Book Name:  ")
    bookAuthor = input("enter Book Author:  ")
    bookPrice = int(input("enter Book Price:  "))
    # isAvailable = input("enter Book Name:  ")
    bookCount = int(input("How many pieces are availbale of this book:  "))

    Books["Name"].append(bookName) 
    Books["Author"].append(bookAuthor)
    Books["Price"].append(bookPrice)
    if(bookCount > 0):
        Books["isAvailable"].append(True)
    else:
        Books["isAvailable"].append(False)
    Books["bookCount"].append(bookCount)
    print("\nadding books\n")
def deleteBooks():
    #match Index
    print("\ndeleting Books\n")
def fineStudent():
    print("\nfining student\n")

def findIndex(toFind):
    indexed = Books["Name"].index(toFind)
    Books["Name"].pop(indexed)
    Books["Author"].pop(indexed)
    Books["Price"].pop(indexed)
    Books["isAvailable"].pop(indexed)
    Books["bookCount"].pop(indexed)


def listBooks():
    with open('./books.csv','r') as file:
        reader = csv.reader(file)
        print("+------------+-----------------+-------------+-----------------+-------------+")
        print("|     Name   |      Auther     |     Price   |   isAvailable   |   booCount  +")
        print("+------------+-----------------+-------------+-----------------+-------------+") 
        for read in reader:
            # v = int(read[4])
            # v = v+1
            # s = str(v)
            # print(type(v),type(s),v)
            
            if read[4]!='0':
                # print(read)
                print("  ",read[0],"\t",read[1],"\t",read[2],"\t",read[3],"\t",read[4])
        print("\n")    
# def my():
#     print(Books["Name"][0])

def clearMyBooks():
    Books["Name"].clear()
    Books["Author"].clear()
    Books["Price"].clear()
    Books["isAvailable"].clear()
    Books["bookCount"].clear()
    # print("should be empty now-->",Books)