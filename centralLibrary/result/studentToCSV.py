import pandas as pd
import csv
def storeStudentDetails(Dict):
    # print("storing book details",Dict)
    df = pd.DataFrame(Dict,columns = ['ID', 'StudentName', 'Class', 'Dept'])
    # print("\n",df)
    with open('./students.csv','w') as file:
        writer = csv.writer(file)
        
        idx = df.index
        # print("\n",idx)

        for id in idx:
            writer.writerow(df.loc[id])
        print("Saved Student Data SuccessFully")