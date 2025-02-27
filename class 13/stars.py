
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

