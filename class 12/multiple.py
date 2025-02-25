n1=int(input("write the first number"))
n2=int(input("write the second number"))
for i in range(n1,n2+1):
    print("-"*10)
    for a in range(1,10):
        print(f"{i} * {a} =",i*a)


print("-"*30)

name=input("write the name")
char=input("write the character that you want to see how many times it occours")
c=0
for i in name:
    if i==char:
        c+=1
print(c)

