from math import*
set1={"item1","item2","item3","item4","item5"}
dict1={}
list1=[]
for i in range(len(set1)):
    dict1[set1.pop()]=input("Enter price")
print(dict1)
for x in dict1.values():
    list1.append(x)
print(list1)
print("the max price of an item is{}".format(max(list1)))
print("the min price of an item is{}".format(min(list1)))
