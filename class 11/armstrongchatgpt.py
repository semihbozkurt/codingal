num=int(input("write the number to se if it is armstrong number or not "))
nmbr=num
x=0
while nmbr>0:
    nmbr=nmbr//10
    x+=1

nmbr=num


sum=0
while nmbr>0:
    sum+=(nmbr%10) **x
    nmbr//=10

if sum==num:
    print("it is a armstrong number")
else:
    print("no it is not")


