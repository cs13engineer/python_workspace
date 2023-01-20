import requests
import random
import string
def uniqueBankId():
    N = 10
    bankId = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
    # print("The generated random string : " + str(bankId))
    return str(bankId)


def BankRegister():
    bankDetails={}
    bankDetails['bankName'] =  input("Enter Bank Name: ") 
    bankDetails['bankId'] = uniqueBankId()
    bankDetails['branchName'] = input("Enter Branch Name: ")
    bankDetails['IFSC'] = input("Enter IFSC Code: ")

    print("Bank Details are: \n",bankDetails)

    response = requests.post('http://localhost:5000/addBank',json=bankDetails).json()
    print(response)

    if response['response'] == 'success':
        return str(response['data'])+' row is added\n'
    else:
        return response['response']+' something went wrong\n'
    



