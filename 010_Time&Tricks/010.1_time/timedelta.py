import datetime
from datetime import timedelta

#timedelta
t1 = timedelta(weeks = 2, days = 5, hours = 11, minutes = 8, seconds = 43)
t2 = timedelta(days = 5, hours = 10, minutes = 45, seconds = 24)

print(t1)
print(t2)
print(t1-t2)
print(t1 + timedelta(days = 5))

print('------------------------------')

print(datetime.datetime.today())
print(datetime.date.today())

print('------------------------------')

i_RepublicDay = datetime.date(1950,1,26)
print(i_RepublicDay)

totalDay = datetime.date.today() - i_RepublicDay
print("Total Days:" , totalDay)