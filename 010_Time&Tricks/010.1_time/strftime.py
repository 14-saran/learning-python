import datetime
from datetime import timedelta

t = datetime.datetime.now()
print(t)

print("current Data and time: " ,t)
print("New format for the date and time:",t.strftime("%H:%M:%S %m-%d-%Y"))
print("current year:" ,t.strftime("%Y"))
print("current year:" ,t.strftime("%Y"))
print("Month of year:" ,t.strftime("%B"))
print("Week number of the year:" ,t.strftime("%W"))
print("Weekday of the year:" ,t.strftime("%w"))
print("day of the year:" ,t.strftime("%j"))
print(t.strftime("%d"))
print(t.strftime("%A"))



