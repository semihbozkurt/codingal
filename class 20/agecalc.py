import datetime as dt
now=dt.datetime.now()

day=int(input("write your birth day: "))
month=int(input("birth month: "))
year=int(input("birth year: "))

birth=dt.datetime(year,month,day)

age=now-birth
print("your age is:",age.days//365)
