medic=input("do you have a medical excuse, Y for yes and N for no ")
attendence=int(input("your attendence "))
if medic=="Y":
    print("you can take the exam")
else:
    if attendence>=75:
        print("you can take the exam")
    else:
        print("you can't take the exam")

print("\n \n ")


unit=int(input("write the number of units "))
if unit<=50:
    print("bill is", unit*2.60+25)

elif 50<unit<=100:
    print("bill is", (50*2.60) + (unit-50)*3.25+35)

elif 100<unit<=200:
    print("bill is", (50*2.60) + (50*3.25) + (unit-100)*5.26+45)

elif 200<unit:
    print("bill is",(50*2.60) + (50*3.25) + (100*5.26) + (unit-100)*8.45+75)

print("\n \n ")


ride=input("do you want bike(B) or car(C)")
if ride=="C":
    a=input("fast(F) or slow(S)")
    if a=="F":
        print("you  will have a fast ride with car")
    elif a=="S":
        print("you will have a slow ride with car")
elif ride=="B":
    b=input("fast(F) or slow(S)")
    if b=="F":
        print("you  will have a fast ride with bike")
    elif b=="S":
        print("you will have a slow ride with bike")
else:
    print("try again")

