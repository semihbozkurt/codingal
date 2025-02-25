'''
num1=int(input("write the number "))
for i in range(2,num1):
    if num1%i==0:
        print("NO its not")
        break

    if i==num1-1:
        print("it is a prime number")
'''
        
lav=(int(input("write the small number ")))
high=int(input("write the big number "))

for a in range (lav,high+1):
    for i in range(2,a):
        if a%i==0:
            print(a,"is not a prime number",end="\n -------------------- \n")
            break
        if i == a-1:
            print(a,"is a prime number",end="\n -------------------- \n")

