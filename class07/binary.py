num=int(input("write a number"))
print(("binary number of the number that you write is:",bin(num)))


a= 14
b= 14
print(a is b)
print(a is not b)
print(id(a))
print(id(b))

print("-------------")

x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)
print(id(x))
print(id(y))


print("-------------")

print(1 in x)
print(2 in  y)