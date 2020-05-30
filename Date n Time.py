import datetime
time1=datetime.datetime.now()

date=time1.strftime("%H:%M:%S")
print(date)  ###04:00:49
date=time1.strftime("%H:%M")
print(date)  ##04:13
date=time1.strftime("%H:%S")
print(date)  ##04:49
date=time1.strftime("%H")
print(date)   ##04
date=time1.strftime("%Y:%B:%d")
print(date) ##2020:May:31
date=time1.strftime("%D")
print(date) #05/31/20
date=time1.strftime("%y:%b:%d")
print(date)  ##20:May:31