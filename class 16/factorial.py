'''
f=1
x=int(input("the number"))
for i in range(x+1):
    f*=i
'''

num=int(input("Write the number "))

def f(n):
    if n==1 or n==0 : return 1
    return n*f(n-1)  

print(f(num))

"i get some help from chatGPT, But I understanded how it is working"


