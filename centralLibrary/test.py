# # ## will update books.csv after addition,deletion and updation of any details
# # import pandas as pd
# # import csv
# # from datetime import date
# # def storeBookDetails(Dict):
# #     print("storing book details",Dict)
# #     df = pd.DataFrame(Dict,columns = ['Name'])
# #     with open('./test.csv','w') as file:
# #         writer = csv.writer(file)
# #         idx = df.index
# #         for id in idx:
# #             writer.writerow(df.loc[id])
# #         print("Books data is saved Successfully!")


# # Dict = {
# #     "Name":[{
# #         "fistName":"Amol",
# #         "lastName":"Chavhan"
# #     },{
# #         "fistName":"Aditi",
# #         "lastName":"Pandey"
# #     },
# #     ]
# # }

# # # storeBookDetails(Dict)


# # d0 = date(2008, 8, 18)
# # d1 = date(2008, 9, 26)
# # delta = d1 - d0
# # print(delta.days)

# # from datetime import date

# # today = date.today()
# # today = today + 3
# # print("Today's date:", today)

# from datetime import datetime
# from datetime import timedelta
# from datetime import date

# # taking input as the date
# Begindatestring = date.today()#"2020-10-11"

# # carry out conversion between string
# # to datetime object
# # Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")

# # print begin date
# print("Beginning date")
# print(Begindatestring)

# # calculating end date by adding 10 days
# Enddate = Begindatestring + timedelta(days=10)

# # printing end date
# print("Ending date")
# print(Enddate)
# #35 t0 60 uncommenrt
# from lib import bookTransaction
# from datetime import datetime
# from datetime import timedelta
# from datetime import date
# bookTransaction.readCSV()
# retuningDate = datetime.strptime(bookTransaction.BookTransaction["ExpectedReturnDate"][0], "%Y-%m-%d")
# today = datetime.strptime('2022-06-10', "%Y-%m-%d")

# calSrt = (retuningDate-today)
# print(calSrt)
# # hello = calSrt.split(' ')
# print(type(calSrt))
# srt = str(calSrt)
# print(srt)
# hello = srt.split(' ')
# print(hello)
# diffDay=int(hello[0])
# print(diffDay,type(diffDay))

# print(today,retuningDate,today<=retuningDate)

# if(retuningDate<today):
#     diff = today-retuningDate
#     print("diff",diff)


hello = {
    "hello":[
        'amol',
        'hell0'
    ]
}

hello["hello"].pop('amol')

print(hello)