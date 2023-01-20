# from urllib import response
import requests
from prettytable import PrettyTable
import random
import string

from Account import createAccount
from Details import customerDetails

IFSCcode = '' #use to store IFSC CODE
def uniqueCustId():
    N = 5
    bankId = ''.join(random.choices(string.digits, k=N))
    # print("The generated random string : " + str(bankId))
    return str(bankId)

def getBanks():
    bankData = requests.get('http://localhost:5000/getBankDetails').json()
    # print("Bank Data: ",bankData)
    return bankData

def RegisterCustomer():
    try:
        customer = {}
        x = PrettyTable()
        x.field_names=["SR.No","Bank Name"]
        Banks = getBanks()
        for i in range(0,len(Banks['data'])):
            x.add_row([i,Banks['data'][i][1]])
        print(x)
        # print("selected bank is: ",Banks['data'][selectBank])
        # print("unique CustID: ",uniqueCustId())
        customer['custId'] = int(uniqueCustId())
        customer['custName'] = input("Enter Full Name:  ")
        selectBank = int(input("Select Bank, Enter SR.No: "))
        customer['bankId'] = Banks['data'][selectBank][0]
        IFSCcode = Banks['data'][selectBank][3]
        response = requests.post('http://localhost:5000/registerCustomer',json=customer).json()
        # print("customer is: ",customer)
        if response['response'] == 'success':
            res = createAccount.CreateAccount(response['data']['custId'],response['data']['bankId'],IFSCcode)
            #res == OK
            if res == 'yes':
                choice = input("Do you want to fill the Basic-Details(y/n): ")
                if choice == 'y' or choice == 'Y':
                    print("adding user information")
                    detailResponse = customerDetails.FillDetails(response['data']['custId'])
                    if detailResponse['response'] == 'success':
                        print("enter login details here",detailResponse['data'])
                        return detailResponse
                    else:
                        return detailResponse['response']
                else:
                    y = PrettyTable()
                    y.field_names = ["Customer ID","Customer Name"]
                    y.add_row([response['data']['custId'],response['data']['custName']])
                    return {
                        'response':response['response'],
                        'data':y
                    }
                ## add users basic Details
            else:
                print("Something went wrong account is not created")
                
            # y = PrettyTable()
            # y.field_names = ["Customer ID","Customer Name"]
            # y.add_row([response['data']['custId'],response['data']['custName']])
            # return {
            #     'response':response['response'],
            #     'data':y
            # }
        else:
            return{
                'response':response['response']
            }
        
    except Exception as e:
        print("ERROR in registerCustomers.py: ",e)