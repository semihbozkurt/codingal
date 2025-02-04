h=float(input("write your hight by meters"))
w=float(input("write your weight"))
bmi=w/(h**2)
if bmi<18.5:
    print("underweight")
elif 18.5>=bmi<25:
    print("normal")
elif 25>=bmi<30:
    print("overweight")
elif 30>=bmi<40:
    print("obese")
elif bmi>=40:
    print("morbidly obese")
else:
    print("something went wrong, please try again")