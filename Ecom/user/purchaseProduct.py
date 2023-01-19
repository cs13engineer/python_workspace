import csv
import string
import random
from datetime import date
from admin import product
import pandas as pd
from employee import customers 
from user import orders
from admin import transactions
from Accounts import accountRCV
from Accounts import accountsPay
from Accounts import ledger
"""
    1. See Available Products
    2. enter customerId and prodcutId to purchase
"""

def purchaseProduct():
    #list Available Producs
    i = True
    while i:
        #1.
        print("\n Following Products are Available to Purchase  \n")
        product.showAvailableProducts()
        # df = pd.DataFrame(product.Product,columns=['productId', 'productName', 'Price', 'Quantity', 'Status'])
        # # print(df)
        # if (df.empty):
        #     print("\n::Products are currently Un-Available for PURCHASE::\n\tSorry for Inconvinience\n")
        # else:
        #     print(df)
        product.clearProduct()
        # print(product.Product)
        
        print("\n1. Purchase Product\t\t2. Retrun Product\t\t3. Exit\n")
        try:
            choice = int(input("Enter your choice:  "))
            if(choice == 1):
                """
                    1. products and customers
                    2. if product is availble and then place order and creat transaction
                       |--> deduct quantity by 1 and if its last item then make it uavailbe
                       |--> get all details to create a order
                            |--> readOrders
                            |--> create transaction 
                            |    |--> if customer credit is greater than and equals to the price
                            |         commitTransaction(by saving Transaction)
                            |--> place and saveOrder.  
                """
                product.readProducts()
                productId = input("Select Product[productId]:  ")
                customers.readCustomer()
                customerId = input("Enter Customer Id:  ")
                # print(product.Product)
                # print(customers.Customers)
                prodIndex = product.Product["productId"].index(productId)
                # print("Product index: ",prodIndex)
                # print("Product Name: ",product.Product["productName"][prodIndex])
                custIndex = customers.Customers["customerId"].index(customerId)
                # print("Customers Index: ",custIndex)

                ## prepare order
                # orders.test()
                orders.readOrders()
                """
                    customerCredit = customerCredit - productPrice
                """
                if(float(customers.Customers["customerCredit"][custIndex]) >= float(product.Product["Price"][prodIndex])):
                    if(int(product.Product["Quantity"][prodIndex]) != 0 ):
                        transactions.readTransaction()
                        TransId = ''.join(random.choices(string.ascii_uppercase + string.digits,k=4))
                        uniqueTransactionId = "TRANS_"+str(TransId)
                        orderId= ''.join(random.choices(string.ascii_uppercase + string.digits,k=4))
                        uniqueOrderId="ORDER_"+str(orderId)
                        ##placing order
                        orders.Orders["orderId"].append(uniqueOrderId)
                        orders.Orders["orderDate"].append(date.today())
                        orders.Orders["customerId"].append(customers.Customers["customerId"][custIndex])
                        orders.Orders["productId"].append(product.Product["productId"][prodIndex])
                        orders.Orders["value"].append(product.Product["Price"][prodIndex])
                        ##creating transaction
                        transactions.Transactions["transactionId"].append(uniqueTransactionId)
                        transactions.Transactions["orderId"].append(uniqueOrderId)
                        ##savingAccounts
                                ##1
                        accountRCV.test()
                        accountRCV.readRCV()
                        accountRCV.AccountRCV["transactionId"].append(uniqueTransactionId)
                        accountRCV.AccountRCV["orderId"].append(uniqueOrderId)
                        accountRCV.AccountRCV["accDate"].append(date.today())
                        accountRCV.AccountRCV["customerId"].append(customers.Customers["customerId"][custIndex])
                        accountRCV.AccountRCV["value"].append(product.Product["Price"][prodIndex])
                        accountRCV.saveRCV()
                        accountRCV.clearRCV()
                            ##2
                        
                        # accountsPay.readPay()
                        # accountsPay.AccountPay["transactionId"].append(uniqueTransactionId)
                        # accountsPay.AccountPay["orderId"].append(uniqueOrderId)
                        # accountsPay.AccountPay["accDate"].append(date.today())
                        # accountsPay.AccountPay["customerId"].append(customers.Customers["customerId"][custIndex])
                        # accountsPay.AccountPay["value"].append(product.Product["Price"][prodIndex])
                        # accountsPay.savePay()
                        # accountsPay.clearPay()
                                ##3
                        
                        ledger.readLedger()
                        ledger.Ledger["transactionId"].append(uniqueTransactionId)
                        ledger.Ledger["orderId"].append(uniqueOrderId)
                        ledger.Ledger["accDate"].append(date.today())
                        ledger.Ledger["customerId"].append(customers.Customers["customerId"][custIndex])
                        ledger.Ledger["value"].append(product.Product["Price"][prodIndex])
                        ledger.saveLedger()
                        ledger.clearLedger()
                                ##finish
                        ##saving Customers
                        toSaveCredit = float(customers.Customers["customerCredit"][custIndex]) - float(product.Product["Price"][prodIndex])
                        customers.Customers["customerCredit"][custIndex] = float(toSaveCredit)
                        customers.saveCustomer()
                        customers.clearCustomer()
                        ##saving Product
                        qtt = int(product.Product["Quantity"][prodIndex])-1
                        if (qtt == 0):
                            product.Product["Quantity"][prodIndex] = qtt
                            product.Product["Status"][prodIndex] = "Not Available"
                            product.saveProduct()
                            product.clearProduct()
                        else:
                            product.Product["Quantity"][prodIndex] = qtt
                            product.saveProduct()
                            product.clearProduct()
                        ##saving Transaction
                        transactions.saveTransaction()
                        transactions.clearTrasaction()
                        ##saving Orders
                        orders.saveOrder()
                        orders.clearOrders()
                        print("transaction can be complete: ")
                    else:
                        print("Product Is Not Available")
                else:
                    print("\ninsufficient Fund")
                # orderId= ''.join(random.choices(string.ascii_uppercase + string.digits,k=4))
                # orders.Orders["orderId"].append(orderId)
                # orders.Orders["orderDate"].append(date.today())
                # orders.Orders["customerId"].append(customers.Customers["customerId"][custIndex])
                # orders.Orders["productId"].append(product.Product["productId"][prodIndex])
                # orders.Orders["value"].append(product.Product["Price"][prodIndex])
                # orders.saveOrder()
                # orders.clearOrders()

                product.clearProduct()
                customers.clearCustomer()
                orders.clearOrders()
                transactions.clearTrasaction()

            elif(choice == 2):
                print("Return Products")
                returnProduct()
            elif(choice == 3):
                i = False
        except Exception as e:
            print("Please provide valid input: ",e)


def returnProduct():
    """
       1. Product to be returned 
       2. customer form return
       ____
       |
       |--> custermer should credit the exact amount
       |--> product quantity will increment
            |--> if product is not available then make if available and inc. qtt
            |--> else if increment the qtt
       |
       |--> save product, save customer
       |--> update pay, update ledger
       
       orderId--prodId--custId
    """

    product.readProducts()
    print("Products: ",product.Product)
    orders.readOrders()
    orderId = input("Enter the orderId:  ")
    ID = orders.Orders["orderId"].index(orderId)
    print("Id:  ",ID)
    custId = orders.Orders["customerId"][ID]
    print("custId:  ",custId)
    prodId = orders.Orders["productId"][ID]
    print("productID:  ",prodId)
    customers.readCustomer()
    c_ID = customers.Customers["customerId"].index(custId)
    print("c_ID:  ",c_ID)

    p_ID = product.Product["productId"].index(prodId)
    print("p_ID:  ",p_ID)
    print(int(product.Product["Quantity"][p_ID]) == 0)
    if( int(product.Product["Quantity"][p_ID]) == 0 ):
        print("inside")
        product.Product["Quantity"][p_ID] = int(product.Product["Quantity"][p_ID]) + 1
        product.Product["Status"][p_ID] = "Avalilable"
        customers.Customers["customerCredit"][c_ID] = float(customers.Customers["customerCredit"][c_ID])+ float(orders.Orders["value"][ID])
        ##open transction find id
        transactions.readTransaction()
        t_ID = transactions.Transactions["orderId"].index(orderId)
        transactionId = transactions.Transactions["transactionId"][t_ID]
        transactions.clearTrasaction()
        ##2
                        
        accountsPay.readPay()
        accountsPay.AccountPay["transactionId"].append(transactionId)
        accountsPay.AccountPay["orderId"].append(orderId)
        accountsPay.AccountPay["accDate"].append(date.today())
        accountsPay.AccountPay["customerId"].append(customers.Customers["customerId"][c_ID])
        accountsPay.AccountPay["value"].append(product.Product["Price"][p_ID])
        accountsPay.savePay()
        accountsPay.clearPay()
        ##3
                        
        ledger.readLedger()
        ledger.Ledger["transactionId"].append(transactionId)
        ledger.Ledger["orderId"].append(orderId)
        ledger.Ledger["accDate"].append(date.today())
        ledger.Ledger["customerId"].append(customers.Customers["customerId"][c_ID])
        ledger.Ledger["value"].append(product.Product["Price"][p_ID])
        ledger.saveLedger()
        ledger.clearLedger()
        ##delete from orders
        orders.Orders["orderId"].pop(ID)
        orders.Orders["orderDate"].pop(ID)
        orders.Orders["customerId"].pop(ID)
        orders.Orders["productId"].pop(ID)
        orders.Orders["value"].pop(ID)

        orders.saveOrder()
        orders.clearOrders() 

        product.saveProduct()
        product.clearProduct()
        customers.saveCustomer()
        customers.clearCustomer()
        orders.clearOrders()
        print("reaturned Successfully")
    else:
        product.Product["Quantity"][p_ID] = int(product.Product["Quantity"][p_ID]) + 1
        print("in else")
        # product.Product["Status"][p_ID] = "Avalilable"
        customers.Customers["customerCredit"][c_ID] = float(customers.Customers["customerCredit"][c_ID])+ float(orders.Orders["value"][ID])
        print("in else 1")
        ##open transction find id
        transactions.readTransaction()
        t_ID = transactions.Transactions["orderId"].index(orderId)
        transactionId = transactions.Transactions["transactionId"][t_ID]
        transactions.clearTrasaction()
        ##2
                        
        accountsPay.readPay()
        accountsPay.AccountPay["transactionId"].append(transactionId)
        accountsPay.AccountPay["orderId"].append(orderId)
        accountsPay.AccountPay["accDate"].append(date.today())
        accountsPay.AccountPay["customerId"].append(customers.Customers["customerId"][c_ID])
        accountsPay.AccountPay["value"].append(product.Product["Price"][p_ID])
        accountsPay.savePay()
        accountsPay.clearPay()
        ##3
                        
        ledger.readLedger()
        ledger.Ledger["transactionId"].append(transactionId)
        ledger.Ledger["orderId"].append(orderId)
        ledger.Ledger["accDate"].append(date.today())
        ledger.Ledger["customerId"].append(customers.Customers["customerId"][c_ID])
        ledger.Ledger["value"].append(product.Product["Price"][p_ID])
        ledger.saveLedger()
        ledger.clearLedger()
        ##delete from orders
        orders.Orders["orderId"].pop(ID)
        orders.Orders["orderDate"].pop(ID)
        orders.Orders["customerId"].pop(ID)
        orders.Orders["productId"].pop(ID)
        orders.Orders["value"].pop(ID)

        orders.saveOrder()
        orders.clearOrders()

        product.saveProduct()
        product.clearProduct()
        customers.saveCustomer()
        customers.clearCustomer()
        orders.clearOrders()
        print("reaturned Successfully")
    
    orders.clearOrders()
    product.clearProduct()
    transactions.clearTrasaction()
    customers.clearCustomer()
    ledger.clearLedger()
    accountsPay.clearPay()
