import requests

user={
    # "userName":'',
    # "password":''
}

def logIn():
    print('\t### Login ###')
    user["userName"] = input("Enter userName:  ")
    user['password'] = input("Entet password:  ")
    response = requests.post('http://localhost:5000/login',json=user).json()
    if(response['response'] == 'loggedIn'):
        return 'Logged In Successfully!'
    elif(response['response'] == 'incorrectPassword'):
        return 'Password is Incorrect. Please enter valid password!'
    elif(response['response'] == 'userNotFound'):
        return 'Account is not found, Please REGISTER!'
