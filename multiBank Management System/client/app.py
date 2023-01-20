from prettytable import PrettyTable
from Login import register
iterator = True
while iterator:
    try:
        x = PrettyTable()
        print("### Bank Services ###")
        x.field_names = ["1. Register   ","2. Bank Services"]
        x.add_row(["3. ATM        ","4. EXIT        "])
        
        print(x)
    
        choice = int(input('Enter Your Choice: '))

        if choice == 1:
           register.Registration()
        elif choice == 2:
            print('Cash Withdrawn\n')
            # res = login.logIn()
            # print('\nserver Response: ',res)  
        elif choice == 3:
            print("Registering\n")  
        elif choice == 4:
            print("Exiting ...!")
            iterator = False 

    except Exception as e:
        print('ERROR: ',e)





# iter = True
# while iter: 
#     res = login.logIn()
#     if(res == 'Logged In Successfully!'):
#         iterator = True
#         while iterator:
#             try:
#                 print('1. Login\t2. Register\n3. Exit\n')
#                 choice = int(input('Enter Your Choice: '))

#                 if choice == 1:
#                     print('Looging \n')
#                     res = login.logIn()
#                     print('\nserver Response: ',res)
#                 elif choice == 2:
#                     print("Registering\n")
#                     employee.hello()   
#                 elif choice == 3:
#                     print("Exiting ...!")
#                     iterator = False 

#             except Exception as e:
#                 print('ERROR: ',e)
#     else:
#         i = int(input('Press 1 to exit'))
#         if(i == 1):
#             iter = False
