import datetime as dt
now=dt.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.date)

print()

print(now.strftime("%d-%m-%y (%Y)  %T / %I:%M:%S  %p"))

print()

specificdate=dt.datetime(2020,12,1)

diff= now-specificdate
print(diff)
