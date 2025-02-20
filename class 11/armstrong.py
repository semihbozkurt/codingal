num=int(input("write the number"))
x=0
while num>0:
    num=num//10
    x+=1
print(x)