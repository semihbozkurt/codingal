'''

n1=12
n2=18

for i in range(n1,1,-1):
    if n1%i==0 and n2%i==0:
        print(i)
        break
'''

def gcd(a,b):
    if b>a:
        if a==0: return(b)
        return gcd(a,b%a )
    elif a>b:
        if b==0: return(a)
        return gcd(b,a%b)
    


print(gcd(a=int(input("first number")),b=int(input("second number"))))