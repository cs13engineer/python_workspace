import random
import string
from datetime import datetime
import requests

def createACNumber():
    N = 11
    acNum = ''.join(random.choices(string.digits, k=N))
    # print("The generated random string : " + str(bankId))
    return str(acNum)

def CreateAccount(custId,bankId,ifsc):
    Account={}
    Account['accountNumber'] = createACNumber()
    Account['ifscCode'] = ifsc
    Account['bankId'] = bankId
    Account['custId'] = custId
    # current dateTime
    now = datetime.now()
    # convert to string
    today = now.strftime("%Y-%m-%d")
    # print('DateTime String:', date_time_str)
    Account['issuedOn'] = today

    print('Im in Client: ',Account)
    response = requests.post('http://localhost:5000/createAccount', json=Account).json()

    if (response['response'] == 'success'):
        return 'yes'
    else:
        return 'no'


