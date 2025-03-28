import calendar

print("welcome to calculator \n \n ")

n1=int(input("write the first number: "))
n2=int(input("write the second number: "))

print(f"sum of numbers is: {n1+n2}")
print(f"substracsjon of numbers is: {n1-n2}")
print(f" multiplication of numbers is: {n1*n2}")
print(f"division of numbers is: {n1/n2}")
print(f" ren of numbers is: {n1%n2} \n")

year=int(input("======write the year:====== "))
print(calendar.calendar(year))