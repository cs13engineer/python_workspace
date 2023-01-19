import csv
Books={"Name":[],"Author":[],"Price":[],"isAvailable":[],"bookCount":[]}
    print("Before add anything:",Books)
    with open('./test.csv','r') as file:
        reader = csv.reader(file)
        print("rows are extracted from csv")
        for read in reader:
            Books["Name"].append(read[0])
            Books["Author"].append(read[1])
            Books["Price"].append(read[2])
            Books["isAvailable"].append(read[3])
            Books["bookCount"].append(read[4])
    # print("After adding everythng:",Books)

