import csv
#reading in  csv file
with open("D:\qwerty\\forcsv.csv") as f:
    contents=csv.reader(f)
    potter=[]
    for i in contents:
        potter+=i
print(potter)

#['year', 'event', 'winner', '1995', 'lawn', 'none', '1992', 'cricket', 'pakistan', '2019', 'cricket', 'england', '2018', 'football', 'france']
#