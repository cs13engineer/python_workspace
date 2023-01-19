import string
import random
from datetime import date
import datetime
# S = 4

ran = ''.join(random.choices(string.ascii_uppercase + string.digits,k=4))

print("ORD_"+str(ran))                                                         
print("TRANS_"+str(ran))
print(date.today())
# import string    
# import random # define the random module  
# S = 10  # number of characters in the string.  
# # call random.choices() string module to find the string in Uppercase + numeric data.  
# ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
# print("The randomly generated string is : " + str(ran)) # print the random data  

data = input("Enter Date[yyyy-mm-dd]:  ")
dateArr = data.split('-')
year = dateArr[0]
month = dateArr[1]
day = dateArr[2]

datee = datetime.datetime(int(year),int(month),int(day))

print("Caclulated date:  ",datee)