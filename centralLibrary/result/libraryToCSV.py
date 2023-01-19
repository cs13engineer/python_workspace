## will update books.csv after addition,deletion and updation of any details
import pandas as pd
import csv
def storeBookDetails(Dict):
    # print("storing book details",Dict)
    df = pd.DataFrame(Dict,columns = ['Name', 'Author', 'Price', 'isAvailable','bookCount' ])
    # print("\n",df)
    with open('./books.csv','w') as file:
        writer = csv.writer(file)
        
        idx = df.index
        # print("\n",idx)

        for id in idx:
            writer.writerow(df.loc[id])
        # print("Books data is saved Successfully!")






        # for i in range(0,5):
        #     print(i)



