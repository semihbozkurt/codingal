x=0
rs=0
rs2=0
try:
    x=int(input("Enter a number "))
    rs=rs/x

except ValueError:
    print("error is handled",ValueError)

except ZeroDivisionError:
    print("error is handled",ZeroDivisionError)

except Exception:
    print("error is handled",Exception)

else: print("no exception occured")

finally:
    print("finally block runs always. its used to clean recources")


rs2=rs2+x
print(rs,"/",rs2)


print("\n -------------- \n")

age=int(input("write your age "))
try:
    if age<0:
        raise ValueError
    print(age)
except:
    print("age cannot be minus")
