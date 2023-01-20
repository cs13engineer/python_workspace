import random
import string
import requests
def detailID():
    N = 5
    detailId = ''.join(random.choices(string.digits, k=N))
    # print("The generated random string : " + str(bankId))
    return str(detailId)

def FillDetails(custId):
    details = {}
    details['detailId'] = detailID()
    details['custId'] = custId
    details['adharNumber'] = input("Enter Adhar Number(12 digits): ")
    details['mobileNumber'] = input("Enter Mobile Number(10 digits): ")
    details['panNumber'] = input("Enter PAN Number: ")
    details['emailId'] = input("Enter Email ID: ")
    details['address'] = input("Enter Address: ")

    response = requests.post('http://localhost:5000/addCustomerDetails', json=details).json()

    if response['response'] == "success":
        return {
            "response":"success",
            "data":response['data']
        }
    else:
        return {
            "response":"fail"
        }