'''
def makete():
    print("boil water")
    print("put te bag inside")
    print("wait ")
    print("take te bag out")

makete()
'''








def add(a,b):
    print(f"sum of {a} and {b} is {a+b}")


def minus(a,b):
    print(f"{a} minus {b} is {a-b}")


def multi(a,b):
    print(f"{a} * {b} is {a*b}")

def divi(a,b):
    print(f"{a} divided by {b} is {a/b}")



choice=str(input('''
a=adition
s=substraction
m=multiplication
d=division                 
'''))



num1=int(input("write the big number"))
num2=int(input("write the small number"))


if choice=="a":
    add(num1,num2)

elif choice=="s":
    minus(num1,num2)

elif choice=="m":
    multi(num1,num2)

elif choice=="d":
    divi(num1,num2)

print("program ended")

print("multiple calculator")

def multiadd(*nmbr):
    sum=0
    for i in nmbr:
        sum+=i
    print(sum)


def multimulti(*nmbr):
    sum=1
    for i in nmbr:
        sum*=i
    print(sum)


multimulti(4,5,10,33)
multiadd(14,83,72,100,22)
