import pandas as pd
import csv
"""
    1. Read
    2. Add
    3. Save
    4. Save
"""

Product= {
    "productId":[],
    "productName":[],
    "Price":[],
    "Quantity":[],
    "Status":[]
}

def readProducts(): # print("Before add anything:-->",Books)
    with open('./products.csv','r') as file:
        reader = csv.reader(file)
        # print("rows are extracted from csv")
        # print(reader)
        for read in reader:
            # print(read)
            Product["productId"].append(read[0])
            Product["productName"].append(read[1])
            Product["Price"].append(read[2])
            Product["Quantity"].append(read[3])
            Product["Status"].append(read[4])
    # print("After adding everythng:",Product)

def addProduct():
    print("Getting Product for you")
    prodId = input("Enter Product ID:  ")
    prodName = input("Enter Product Name:  ")
    price = input("Enter Price:  ")
    qtt = input("Enter Quantity: ")

    Product["productId"].append(prodId)
    Product["productName"].append(prodName)
    Product["Price"].append(price)
    Product["Quantity"].append(qtt)
    if(int(qtt)>0):
        Product["Status"].append("Availble")
    else:
        Product["Status"].append("Not Available")
    # print(Product) 
    
def saveProduct():
    with open('./products.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(Product,columns=['productId', 'productName', 'Price', 'Quantity', 'Status'])
        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("File saved Successfully!")

def clearProduct():
    Product["productId"].clear()
    Product["productName"].clear()
    Product["Price"].clear()
    Product["Quantity"].clear()
    Product["Status"].clear()
    # print("Cleared the dictionary")
    # print(Product)

def displayProduct():
    readProducts()
    df = pd.DataFrame(Product,columns=['productId', 'productName', 'Price', 'Quantity', 'Status'])
    if df.empty:
        print("Products Are Not Available.. Please Add")
    else:
        print(df)
    clearProduct()

def updateProduct():
    print("## Update Product ##")
    i = True
    while i:
        try:
            print("1. update Product ID\t\t2. update Product Name\t\t3. update Price\t\t4.update Quantity\t\t5. Show Products\t\t6. Exit")
            choice = int(input("Enter your choice:  "))
            if(choice == 1):
                readProducts()
                prodId = input("Enter current Product ID:  ")
                id = Product["productId"].index(prodId)
                updatedId = input("Enter Product Id to be updated:  ")
                Product["productId"][id] = updatedId
                saveProduct()
                clearProduct()
            elif(choice == 2):
                readProducts()
                prodId = input("Enter current Product ID:  ")
                id = Product["productId"].index(prodId)
                updatedName = input("Enter Product Name to be updated:  ")
                Product["productName"][id] = updatedName
                saveProduct()
                clearProduct()
            elif(choice == 3):
                readProducts()
                prodId = input("Enter current Product ID:  ")
                id = Product["productId"].index(prodId)
                updatedPrice = input("Enter Product Price to be updated:  ")
                Product["Price"][id] = updatedPrice
                saveProduct()
                clearProduct()
            elif(choice == 4):
                readProducts()
                prodId = input("Enter current Product ID:  ")
                id = Product["productId"].index(prodId)
                updatedQtt = input("Enter Product Price to be updated:  ")
                print("the count",updatedQtt)
                if (int(updatedQtt) == 0):
                    print("Is true")
                    Product["Status"][id] = "Not Available"
                else:
                    print("Is False")
                    Product["Status"][id] = "Available"
                Product["Quantity"][id] = updatedQtt
                saveProduct()
                clearProduct()
            elif(choice == 5):
                displayProduct()
            elif(choice == 6):
                i = False
        except Exception as e:
            print("Please give a valid input",e)

def deleteProduct():
    readProducts()
    prodId = input("Enter current Product ID:  ")
    id = Product["productId"].index(prodId)
    Product["productId"].pop(id)
    Product["productName"].pop(id)
    Product["Price"].pop(id)
    Product["Quantity"].pop(id)
    Product["Status"].pop(id)
    saveProduct()
    clearProduct()
    print("Product is Deleted")

def showAvailableProducts():
    with open('./products.csv','r') as file:
        reader = csv.reader(file)
        for read in reader:
            if(int(read[3]) > 0):
                Product["productId"].append(read[0])
                Product["productName"].append(read[1])
                Product["Price"].append(read[2])
                Product["Quantity"].append(read[3])
                Product["Status"].append(read[4])
        # print("Products: ",Product)
        df = pd.DataFrame(Product,columns=['productId', 'productName', 'Price', 'Quantity', 'Status'])
        if df.empty:
            print("Now Product is Available")
        else:
            print("--- Availbale Products ---\n")
            print(df)
            print("_______________________________________________________")
        

