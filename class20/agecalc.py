import datetime as dt
import calendar
now=dt.datetime.now()

#taking birth date
day=int(input("write your birth day: "))
month=int(input("birth month: "))
year=int(input("birth year: "))

birth=dt.datetime(year,month,day)

#age as day
age=(now-birth).days


# parts of age:
agey=int(float(age)//365.25)
agem=(float(age)%365.25)//30
aged=int((float(age)%365.25)%30)

print(f"you are {agey} years {agem} months and {aged} days old" )

#space
print("-------------------------------------------------",end="\n\n\n")

#today
weekdays=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print("today is:",weekdays[now.weekday()],end="\n\n")


#calendar of december 2025
print("calendar of december 2025")
print(calendar.month(2025,12))

