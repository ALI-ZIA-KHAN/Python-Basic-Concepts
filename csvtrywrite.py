import csv
with open("D:\qwerty\\forcsv.csv","w",newline="") as f:
    data=csv.writer(f,delimiter=",")
    data.writerow(["Name","age","grade"])
    data.writerow(["Ali", "18", "A+"])
with open("D:\qwerty\\forcsv.csv") as f:
    contents=csv.reader(f)
    potter=[]
    for i in contents:
        potter+=i
print(potter)


#output
#['Name', 'age', 'grade', 'Ali', '18', 'A+']
