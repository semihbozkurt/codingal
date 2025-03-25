import datetime as dt
import calendar
now=dt.datetime.now()

day=int(input("write your birth day: "))
month=int(input("birth month: "))
year=int(input("birth year: "))

birth=dt.datetime(year,month,day)

age=now-birth
print("your age is:",age.days//365)



print("-------------------------------------------------")

weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

print("today is:",weekdays[now.weekday()])



print("calendar of december 2025")
print(calendar.month(2025,12))

