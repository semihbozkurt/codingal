import random

rand=random.randint(1,100)
atempt=0

while True:

    atempt+=1

    try:
        guess=int(input("write your guess "))


        if guess==rand:    
            print("you win, number of attempts: ",atempt)
            break

        elif guess < rand: print("too low")
        elif guess > rand: print("too high")

    except:
        print("your guess should be integer")

a=input()
