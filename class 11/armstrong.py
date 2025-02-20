num=int(input("write the number to se if it is armstrong number or not "))
nmbr=num
x=0
while nmbr>0:
    nmbr=nmbr//10
    x+=1

a=0
sum=0
while a<x:
    sum+=int((str(num)[a]))**x

if sum==num:
    print("it is a armstrong number")
else:
    print("no it is not")

print("something")
