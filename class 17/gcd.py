'''

n1=12
n2=18

for i in range(n1,1,-1):
    if n1%i==0 and n2%i==0:
        print(i)
        break
'''
n1=12
n2=24

def f(n):
    if n1%n==0 and n2%n==0:
        print(n)
        return
    f(n-1)
    n+=1

f(10)
