num=int(input("Write a number "))

while True:
    if num%20==0:
        print("TWIST")
        break
    elif num%15==0:
        pass
    elif num%5==0:
        print("WHIRL")
        break
    elif num%3==0:
        print("BOING")
        break
    else: print(num)
