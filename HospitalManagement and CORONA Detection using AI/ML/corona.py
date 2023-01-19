from termcolor import colored, cprint
import pandas as pd
import csv
import sklearn
from sklearn import tree
#reading data from file into pandas 
def Corona():
    data = pd.read_csv("./DataForCoronoVirus.csv")
    #checking for negative value from file and converting into 0
    data[data < 0]=0
    #data frame head
    data.head()
    #variavle for feature,label for sklearn library
    #reading from dataframe 
    feature = data[["NoOfDays","Fever","Cough","Tiredness","DifficultyInBreathing"]]
    label=data["Label"]
    #by using sklearn library
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(feature,label)
    #variable for no of day
    noOfDays= int(input("How Long Have You Been Sick. Please Enter Number Of Days : \n"))
    #condition for Number of daye must be greater than 0
    if(noOfDays<=0):
        print(colored("Number of days must be greater than 0",'red', attrs=['bold']))

    else:
        #variable for fever,cough,tiredness,difficultyInBreathing
        fever=int(input("Are You Suffering From Fever Yes/No (0/1): \n"))
        cough=int(input("Are You Suffering From Cough Yes/No (0/1): \n"))
        tiredness=int(input("Are You Suffering From Tiredness Yes/No (0/1): \n"))
        difficultyInBreathing=int(input("Have you Facing difficulty While Breathing Yes/No (0/1): \n"))
        #Checking correct input
        if((fever==0 or fever==1) and (cough==0 or cough==1) ):
                #Checking correct input
                if((tiredness==0 or tiredness==1) and  (difficultyInBreathing==0 or difficultyInBreathing==1)):
                    # if clf.predict is 0
                    if (clf.predict([[noOfDays,fever,cough,tiredness,difficultyInBreathing]]) == 0):
                        print(colored("You are Suffering From Corona Virus \n",'blue', attrs=['bold']))
                    # if clf.predict is 1
                    else:
                        print(colored("You are Suffering From Viral Fever  \n",'blue', attrs=['bold']))
                #if user enter the wrong data   
                else:
                    print(colored("Input must be 0 or 1",'blue', attrs=['bold']))
        #if user enter the wrong data
        else:
            print(colored("Input must be 0 or 1",'blue', attrs=['bold']))


def test():
    print("Corana It is Corona")