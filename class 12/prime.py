num1=int(input("write the number "))
for i in range(2,num1):
    if num1%i==0:
        print("NO its not")
        break

    if i==num1-1:
        print("it is a prime number")

        
