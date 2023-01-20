import string
import random
from datetime import datetime 
# initializing size of string
N = 10

res = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))

# print result
# print("The generated random string : " + str(res))
 # current dateTime
now = datetime.now()
    # convert to string
today = now.strftime("%d-%m-%Y")
print('DateTime String:', today)