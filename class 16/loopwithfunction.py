def f(a,b):
    return a+b
a=f(10,33)
print(a)

def f2(name,message):
    print("hi",name,message)

f2(message="welcome", name="Semih")

def f3(n):
    if n==0: return
    print(n)
    f3(n-1)

f3(100)