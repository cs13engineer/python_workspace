#importing the package
from termcolor import colored, cprint
import pandas as pd
import csv
import sklearn
from sklearn import  tree
    
#reading data from file into pandas
def Chronic():
    data = pd.read_csv("./DataForChronicDisease.csv")
    #checking for negative value from file and converting into 0
    data[data < 0]=0
    #data frame head
    data.head()
    #variavle for feature,label for sklearn library
    #reading from dataframe 
    feature = data[["NoOfDays","BloodPressure","Depression"]]
    label=data["Label"]
    #by using sklearn library
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(feature,label)
    #variable for no of day
    noOfDays= int(input("How Long Have You Been Suffering From Disease. Please Enter Number Of Days : \n"))#condition for Number of daye must be greater than 0
    if(noOfDays<=0):
        print(colored("Number of days must be greater than 0",'red', attrs=['bold']))
    else:
        #opening the file DataForChronicDisease
        bloodPrssure= int(input("Are You Suffering From High Blood Pressure Yes/No (0/1): \n"))
        depression=int(input("Are You Suffering From Depression Yes/No (0/1): \n"))
        #Checking correct input
    if((bloodPrssure == 0 or bloodPrssure == 1) and  (depression == 0 or depression == 1)):
    # if clf.predict is 0
        if (clf.predict([[noOfDays,bloodPrssure,depression]]) == 0):
            print(colored("You are Suffering From Chronic Disease \n",'blue', attrs=['bold']))
            # if clf.predict is 0
        else:
            print(colored("You are Suffering From Non Chronic Disease \n",'blue', attrs=['bold']))
            #if user enter the wrong data
    else:
        print(colored("Input must be 0 or 1",'red', attrs=['bold']))