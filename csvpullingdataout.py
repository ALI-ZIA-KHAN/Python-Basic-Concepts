import csv
with open("D:\qwerty\\forcsv.csv") as f:
    contents=csv.reader(f)
    potter=[]
    for i in contents:
        potter+=i
print(potter)
target=input("Enter competetiion:")
index_num=potter.index(target)
index_winner=index_num+1
the_winner=potter[index_winner]
print("The winner is:  "+the_winner)
#
#['year', 'event', 'winner', '1995', 'lawn', 'none', '1992', 'cricket', 'pakistan', '2019', 'cricket', 'england', '2018', 'football', 'france']
#Enter competetiion:football
#The winner is:  france
#