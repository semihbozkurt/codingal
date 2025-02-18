
num=int(input("write a number"))
for i in range (10):
    print(f"{i+1}*{num}=",num*(i+1))

print("\n ---------------")

for i in range (100,201,1):
    print(i)
for i in range(200,99,-1):
    print(i)

print("\n ---------------------")

x=int(input("write the small number"))
y=int(input("write the big number"))
for i in range (x,y+1):
    print(i**2)

print("\n --------------")

top=0
a=int(input("write the number"))
for i in range(1,a+1):
    top+=i
print(top)

print("\n --------------")

mul=1
b=int(input("write the number"))
for i in range(1,b+1):
    mul*=i
print(mul)
