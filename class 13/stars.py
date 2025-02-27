'''
n=int(input("write a number: "))

count=1

for i in range(n):
    print("\n")
    for j in range(i+1):
        print(count, end=" ")
        count+=1


print(" \n ----------------")


num=int(input("write the number of stars "))

clone=num

for i in range(num):
    for j in range(clone):
        print("* "*clone)
        clone-=1

print("------------\n")
'''


s=int(input("write a number: "))

hesap=1+((s-1)*2)

spc=s-1

for i in range(0,hesap,2):
    for a in range(spc):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for b in range(spc):
        print(" ",end="")
    spc-=1
    print()

''''''


spc=1

for i in range(hesap-1,0,-2):
    for a in range(spc):
        print(" ",end="")
    for j in range(i-1):
        print("*",end="")
    for b in range(spc):
        print(" ",end="")
    spc+=1
    print()


