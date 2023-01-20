# from urllib import request
from flask import Flask, request
from Login import loginServer
from Register import registerBank
from Register import registerCustomer
from Account import account
from Register import addCustomerDetails


app = Flask(__name__)

@app.route('/login',methods=['POST'])
def Login():
    data = request.json
    return loginServer.Login(data)

@app.route('/addBank',methods=["POST"])
def AddBank():
    data = request.json
    return registerBank.Bank(data)

@app.route('/getBankDetails')
def getBankDetails():
    return registerCustomer.getBankDetails()   

@app.route('/getCustomer')
def getCustomer():
    return account.GetCustomer()

@app.route('/registerCustomer',methods=["POST"])
def registerUser():
    data = request.json
    return registerCustomer.RegisterCustomer(data)

@app.route('/addCustomerDetails',methods=["POST"])
def addCustomerDetail():
    data = request.json
    return addCustomerDetails.AddDetails(data)

@app.route('/createAccount',methods=["POST"])
def createAccount():
    data = request.json
    return account.CreateAccount(data)


@app.route('/loginUser',methods=["POST"])
def loginUser():
    data = request.json
    return loginServer.UserLogin(data)

if __name__ == '__main__':
    app.run() 