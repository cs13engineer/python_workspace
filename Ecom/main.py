import os
from admin import product
from employee import customers
from user import orders
from user import purchaseProduct
from admin import reports

i =  True 
while i:
    print("\n\t\t**#E-Commerce#**")
    print("\n________________________________________________________\n\n1. Admin",end="\t")
    print("2. User",end="\t\t")
    print("3. Employee",end="\t")
    print("4. Reports",end="\t")
    print("4. Exit\n________________________________________________________\n")
    try:
        choice = int(input("enter your choice:  "))
        if (choice == 1):

            i1 = True
            while i1:
                print("\n::Admin Block::\n")
                print("_________________________________________________________________________________________________________")
                print("\n1. Add Product",end="\t")
                print("2. Display Products",end="\t")
                print("3. Update Product",end="\t")
                print("4. Delete Product",end="\t")
                print("5. Orders Menu\n")
                print("6. Exit")
                print("_________________________________________________________________________________________________________\n")
                try:
                    ch = int(input("enter your choice:  "))
                    if(ch == 1):
                        product.readProducts()
                        product.addProduct()
                        product.saveProduct()
                        product.clearProduct()
                        print("Added Product Successfully")
                    elif(ch == 2):
                        print("\n Products are###\n")
                        product.displayProduct()
                    elif(ch == 3):
                        product.updateProduct()
                    elif(ch == 4):
                        product.deleteProduct()
                    elif(ch == 5):
                        i11 = True
                        while i11:
                            print("\n::Orders Menu::")
                            print("_________________________________________________________________________________________________________")
                            print("\n1. Add Order\t\t2. Display Orders\t\t3. Update Orders\t\t4. Delete Order\n5. Exit")
                            print("_________________________________________________________________________________________________________\n")
                            try:
                                c = int(input("Enter your choice:  "))
                                if(c == 1):
                                    orders.readOrders()
                                    orders.addOrder()
                                    orders.saveOrder()
                                    orders.clearOrders()
                                elif(c == 2):
                                    orders.displayOrders()
                                elif(c == 3):
                                    orders.updateOrder()
                                elif(c == 4):
                                    orders.deleteOrder()                                    
                                else:
                                    i11 = False
                            except Exception as e:
                                print("please give a valid input",e)
                    elif(ch==6):
                        i1 = False
                    else:
                        i1 = False
                except Exception as e:
                    print("please give a valid input",e)        
        elif (choice == 2):
            i2 = True
            while i2:
                print("\n## Place Orders Here ##")
                print("1. Check List of availabel Products\t\t2. Exit\n")
                try:
                    ch = int(input("Eneter your choice:  "))
                    if(ch == 1):
                        purchaseProduct.purchaseProduct()
                    elif(ch == 2):
                        i2 = False
                except Exception as e:
                    print("please give a valid input",e)
        elif (choice == 3):
            i3 = True
            while i3:
                print("\n::Customers Menu::")
                print("_________________________________________________________________________________________________________")
                print("\n1. Add Customer\t\t2. Display Customers\t\t3. Update Customer\t\t4. Delete Customer\n5. Exit")
                print("_________________________________________________________________________________________________________\n")
                
                try:
                    ch = int(input("Enter your choice:  "))
                    if(ch == 1):
                        customers.readCustomer()
                        customers.addCustomer()
                        customers.saveCustomer()
                        customers.clearCustomer()
                        print("Customer Added")
                    elif(ch == 2):
                        customers.displayCustomer()
                    elif(ch == 3):
                        customers.updateCustomer()
                    elif(ch == 4):
                        customers.deleteCustomer()
                    elif(ch == 5):
                        i3 = False
                except Exception as e:
                    print("please give a valid input",e)
        elif(choice == 4):
            # print("Reports Section")
            i0 = True
            while i0:
                print("\n1. Orders On Day\t\t2.Largest and Smallest Order\t3. Pie Chart of customer\n4. Available Product\t5. Total Receivale and Payble\t6. Exit\n")
                try:
                    getCh = int(input("Enter your choice:  "))
                    if(getCh == 1):
                        reports.dateWiseOrders()
                    elif(getCh == 2):
                        reports.gtrSml()
                    elif(getCh == 3):
                        print("Pie Chart")
                        reports.pie()
                    elif(getCh == 4):
                        print("inside 4")
                        product.showAvailableProducts()
                    elif(getCh == 5):
                        print("Payble and Receivalble")
                        reports.receivalble()
                        reports.payable()
                    elif(getCh == 6):
                        i0 = False
                    else:
                        i0 = False
                except Exception as e:
                    print("please give a valid input",e)
                    
        elif (choice == 5):
            print("exiting")
            i = False
    except  Exception as e:
        print("please give a valid input",e)

