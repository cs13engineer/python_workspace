from user import orders
from datetime import date
import datetime
import numpy as np
import matplotlib.pyplot as plt
from Accounts import accountRCV
from Accounts import accountsPay

def dateWiseOrders():
    orders.readOrders()
    Date = input("Enter the Date in [yyyy-mm-dd] format only::  ")
    dateArr = Date.split('-')
    year = dateArr[0]
    month = dateArr[1]
    day = dateArr[2]

    datee = datetime.datetime(int(year),int(month),int(day))
    d = str(datee)
    d = d.split(" ")
#     print("printed",d)
#     print("Caclulated date:  ",datee)
    # orders.readOrders()
#     print("date",str(d[0]))
    count = 0
    print("\nOrderID\tOrderDate\tCustomerId\tProductID\tValue\n")
    for order in range(len(orders.Orders["orderId"])):

        if(orders.Orders["orderDate"][order] == d[0]):
            count = count + 1
            print(orders.Orders["orderId"][order]+"\t"+orders.Orders["orderDate"][order]+"\t"+orders.Orders["customerId"][order]+"\t"+orders.Orders["productId"][order]+"\t"+orders.Orders["value"][order])
#         else:
#             print("date is not Present")

    # print("count is count: ",count)
    orders.clearOrders()

def gtrSml():
    # orders.readOrders()
    # orders.Orders["value"].sort()
    # print("largetst purchase value:",orders.Orders["value"][0])
    # orders.clearOrders()
    orders.readOrders()
    Date = input("Enter the Date in [yyyy-mm-dd] format only::  ")
    dateArr = Date.split('-')
    year = dateArr[0]
    month = dateArr[1]
    day = dateArr[2]

    datee = datetime.datetime(int(year),int(month),int(day))
    d = str(datee)
    d = d.split(" ")
    # print("printed",d)
    # print("Caclulated date:  ",datee)
    # orders.readOrders()
    Largest = 0
    idx = 0
    # print("\nOrderID\tOrderDate\tCustomerId\tProductID\tValue\n")
    for order in range(len(orders.Orders["orderId"])):

        if(orders.Orders["orderDate"][order] == str(d[0])):
            if (Largest >= int(orders.Orders["value"][order])):
                Largest = Largest
                idx = order 
                # print(order)
            else:
                Largest = int(orders.Orders["value"][order])
                idx = order
                # print("Largestsss: ",Largest,int(orders.Orders["value"][order]))
            # count = count + 1
            # print(orders.Orders["orderId"][order]+"\t"+orders.Orders["orderDate"][order]+"\t"+orders.Orders["customerId"][order]+"\t"+orders.Orders["productId"][order]+"\t"+orders.Orders["value"][order])
#         else:
#             print("date is not Present")
            
   
    print(f"Largest Purchase of {Date}:")
    idx = orders.Orders["value"].index(str(Largest))
    print("_________________________________________________________________________\n")
    print("OrderID\t\tOrderDate\tCustomerId\tProductID\tValue\n")
    print(orders.Orders["orderId"][idx]+"\t"+orders.Orders["orderDate"][idx]+"\t"+orders.Orders["customerId"][idx]+"\t\t"+orders.Orders["productId"][idx]+"\t\t"+orders.Orders["value"][idx]+"\n")
    print("_________________________________________________________________________")
    
    Smallest = 0
    for order in range(len(orders.Orders["orderId"])):
#         print(orders.Orders["orderDate"][order] == str(d[0]))
        if(orders.Orders["orderDate"][order] == str(d[0])):
            if (Smallest <= int(orders.Orders["value"][order])):
                if order == 0:
                    Smallest = int(orders.Orders["value"][order])
                else:
                    Small = int(orders.Orders["value"][order])
                    if(Small <= Smallest):
                        Smallest = Small
#                         print("::",Smallest)
#                     print("Smallest in IF: ",Smallest)
                    idx = order 
#                     print(idx)
                # print(order)
            else:
                Smallest = int(orders.Orders["value"][order])
#                 print("Smallest in ELSE: ",Smallest)
                idx = order
#                 print(idx)
                # print("Largestsss: ",Largest,int(orders.Orders["value"][order]))
            # count = count + 1
            # print(orders.Orders["orderId"][order]+"\t"+orders.Orders["orderDate"][order]+"\t"+orders.Orders["customerId"][order]+"\t"+orders.Orders["productId"][order]+"\t"+orders.Orders["value"][order])
#         else:
#             print("date is not Present")
            
#     print("the smallest:  ",Smallest)
    print(f"\nSmallest Purchase of the day{Date}:")
    idx = orders.Orders["value"].index(str(Smallest))
    print("_________________________________________________________________________\n")
    print("OrderID\t\tOrderDate\tCustomerId\tProductID\tValue\n")
    print(orders.Orders["orderId"][idx]+"\t"+orders.Orders["orderDate"][idx]+"\t"+orders.Orders["customerId"][idx]+"\t\t"+orders.Orders["productId"][idx]+"\t\t"+orders.Orders["value"][idx])
    print("_________________________________________________________________________")
    orders.clearOrders()


def pie():
    orders.readOrders()
    custId = input("Please enter the customers Id:   ")
    l = len(orders.Orders["orderId"])
    custIndexes = []
    for i in range(l):
        if (orders.Orders["customerId"][i] == custId):
            custIndexes.append(i)
        else:
            print("customer is not found")
    
    products = []
    price = []
    # print("customer indexes: ",custIndexes)
    for a in custIndexes:
        print(a)
        products.append(orders.Orders["productId"][a])
        price.append(orders.Orders["value"][a])
    # print(products,price)
    fig = plt.figure(figsize =(10, 7))
    # plt.pie(, labels = employees)
    plt.pie(price,labels=products,  shadow = True , autopct='%.2f')
    print("Kindly Close the Current Graph for NEXT operation")
    plt.title(f"Customer {custId} purchased Products")
    plt.show()
    orders.clearOrders()
    
    
def receivalble():
    # print("Receivable")
    """
        order total of particular date
    """
    # orders.readOrders()
    accountRCV.readRCV()
    Date = input("\n\nEnter the Date in [yyyy-mm-dd] format only for checking Returnable::  ")
    dateArr = Date.split('-')
    year = dateArr[0]
    month = dateArr[1]
    day = dateArr[2]

    datee = datetime.datetime(int(year),int(month),int(day))
    d = str(datee)
    d = d.split(" ")
    
#     print(d)
    Receivable = 0.0
    idx = 0
    # print("\nOrderID\tOrderDate\tCustomerId\tProductID\tValue\n")
    for order in range(len(accountRCV.AccountRCV["transactionId"])):
        
        if(accountRCV.AccountRCV["accDate"][order] == str(d[0])):
            Receivable += float(accountRCV.AccountRCV["value"][order])
    print(f"\nTotal Receivalbe on Date {d[0]} : ",Receivable)
    accountRCV.clearRCV()

def payable():
    # print("Receivable")
    """
        order total of particular date
    """
    # orders.readOrders()
    accountsPay.readPay()
    Date = input("Enter the Date in [yyyy-mm-dd] format only for checking Payble::  ")
    dateArr = Date.split('-')
    year = dateArr[0]
    month = dateArr[1]
    day = dateArr[2]

    datee = datetime.datetime(int(year),int(month),int(day))
    d = str(datee)
    d = d.split(" ")
    
#     print(d)
    Payable = 0.0
    idx = 0
    # print("\nOrderID\tOrderDate\tCustomerId\tProductID\tValue\n")
    for order in range(len(accountsPay.AccountPay["transactionId"])):
        
        if(accountsPay.AccountPay["accDate"][order] == str(d[0])):
            Payable += float(accountsPay.AccountPay["value"][order])
    print(f"\nTotal Payable on Date {d[0]} : ",Payable)
    accountsPay.clearPay()
            


    