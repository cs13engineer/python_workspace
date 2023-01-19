import csv
import pandas as pd
from employee import customers
Orders = {
    "orderId":[],
    "orderDate":[],
    "customerId":[],
    "productId":[],
    "value":[]
}


def readOrders():
    with open('./orders.csv','r') as file:
        reader = csv.reader(file)
        for read in reader:
            Orders["orderId"].append(read[0])
            Orders["orderDate"].append(read[1])
            Orders["customerId"].append(read[2])
            Orders["productId"].append(read[3])
            Orders["value"].append(read[4])
    # print("Orders: ",Orders)

def addOrder():
    print("\nPlease fill Order Information")
    orderId = input("Pelase enter Order Id:  ")
    orderDate = input("please enter order date [yyyy-mm-dd]:  ")
    customerId = input("please enter customer ID:  ")
    productId = input("plase enter the Product ID:  ")
    value = input("Please enter the total amt/value/price of Order:  ")
    #appending to the Dictionary
    Orders["orderId"].append(orderId)
    Orders["orderDate"].append(orderDate)
    Orders["customerId"].append(customerId)
    Orders["productId"].append(productId)
    Orders["value"].append(value)

    print("Orders:  ", Orders)

def saveOrder():
    with open('./orders.csv','w') as file:
        writer = csv.writer(file)
        df = pd.DataFrame(Orders, columns=[
            "orderId",
            "orderDate",
            "customerId",
            "productId",
            "value"
        ])

        idx = df.index
        for id in idx:
            writer.writerow(df.loc[id])
    # print("Orders are stored successfully!")

def displayOrders():
    readOrders()
    df = pd.DataFrame(Orders, columns=[
            "orderId",
            "orderDate",
            "customerId",
            "productId",
            "value"
        ])
    print("\n",df)
    clearOrders()

def clearOrders():
    Orders["orderId"].clear()
    Orders["orderDate"].clear()
    Orders["customerId"].clear()
    Orders["productId"].clear()
    Orders["value"].clear()
    # print("Cleared:  ", Orders)

def updateOrder():
    print("## Update Order ##")
    i = True
    while i:
        try:
            print("\n1. update Order ID\t\t2. update Order Date\t\t3. update Customer ID\t\t4.update Product ID\n5. update Value.\t\t6. Exit\n")
            choice = int(input("Enter your choice:  "))
            if(choice == 1):
                readOrders()
                orderId = input("Enter current Order ID:  ")
                id = Orders["orderId"].index(orderId)
                updatedId = input("Enter Order3 Id to be updated:  ")
                Orders["orderId"][id] = updatedId
                saveOrder()
                clearOrders()
            elif(choice == 2):
                readOrders()
                orderId = input("Enter current Order ID:  ")
                id = Orders["orderId"].index(orderId)
                updatedDate = input("Enter Order Date to be updated:  ")
                Orders["orderDate"][id] = updatedDate
                saveOrder()
                clearOrders()
            elif(choice == 3):
                readCustomer()
                orderId = input("Enter current Order ID:  ")
                id = Orders["orderId"].index(orderId)
                updatedCustID = input("Enter Customer ID to be updated:  ")
                Orders["customerId"][id] = updatedCustID
                saveOrder()
                clearOrders()
            elif(choice == 4):
                readCustomer()
                orderId = input("Enter current Order ID:  ")
                id = Orders["orderId"].index(orderId)
                updatedProdID = input("Enter Product ID to be updated:  ")
                Orders["productId"][id] = updatedProdID
                saveOrder()
                clearOrders()
            elif(choice == 5):
                print("value")
                readOrders()
                orderId = input("Enter current Order ID:  ")
                id = Orders["orderId"].index(orderId)
                updatedValue = input("Enter Value/Price/Ammt. to be updated:  ")
                Orders["value"][id] = updatedValue
                saveOrder()
                clearOrders()
            elif(choice == 6):
                i = False
        except Exception as e:
            print("Please give a valid input",e)

def deleteOrder():
    print("\nDeleting Order::")
    readOrders()
    orderId = input("Please enter the Order ID to delete the Order:  ")
    id = Orders["orderId"].index(orderId)
    
    Orders["orderId"].pop(id)
    Orders["orderDate"].pop(id)
    Orders["customerId"].pop(id)
    Orders["productId"].pop(id)
    Orders["value"].pop(id)
    saveOrder()
    clearOrders()
    print("Deleted Order: ",orderId)

# def test():
#     print("Testing Orders")    