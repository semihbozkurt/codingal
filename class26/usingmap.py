lst1=[10,20,30,40]
lst2=[1,2,3,4]


def add(a,b):
    return a+b

lst3=map(add,lst1,lst2)
print(list(lst3))

def sqr(a):
    return a**2

lst4=map(sqr,lst1)
print(list(lst4))

