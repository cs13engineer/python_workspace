from prettytable import PrettyTable
from Login import registerBank
from Login import registerCustomers

def Registration():
    iteration = True
    while iteration:
        try:
            x = PrettyTable()
            x.field_names = ["1. Add Bank", "2. Add Customers","3. Exit"]
            print(x)
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                print("adding bank")
                res = registerBank.BankRegister()
                print(res)
            elif choice == 2:
                print("adding customer")
                # res = registerCustomers.getBanks()
                res = registerCustomers.RegisterCustomer()
                print("Available Banks: ",res)
                if(res['response'] == 'success'):
                    print(res['data'])
                else:
                    print("User Not Get Registered")
            elif choice == 3:
                iteration = False
            print("Register bank and customer here")
        except Exception as e:
            print("ERROR: ",e)