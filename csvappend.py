import csv
with open("D:\qwerty\\forcsv.csv","a",newline="") as f:
    data=csv.writer(f,delimiter=",")
    data.writerow(["Asad","19","A+"])
    data.writerow(["Ahmas", "19", "A"])
with open("D:\qwerty\\forcsv.csv") as f:
    contents=csv.reader(f)
    potter=[]
    for i in contents:
        potter+=i
print(potter)


#output
#['Name', 'age', 'grade', 'Ali', '18', 'A+', 'Asad', '19', 'A+', 'Ahmas', '19', 'A']
