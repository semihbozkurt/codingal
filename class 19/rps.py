import random
print("velcome to the Rock paper and sissors game")

computer=0 #point of computer
mann=0  #point of mann

move=["rock", "paper", "sissors"]

while True:
    comp=random.choice(move)
    man=input("make your choice:  paper, sissors, rock   ")
    print(comp)

    if comp==man: print("tie, no points")

    elif (comp=="rock" and man=="paper" )or(comp=="sissors" and man=="rock") or(comp=="paper" and man=="sissors"):
        print("you win this round: 1 point")
        mann+=1

    elif (comp=="paper" and man=="rock") or (comp=="rock" and man=="sissors")or(comp=="sissors" and man=="paper"):
        print("you loose this round: 1 point to computer")
        computer+=1

    else: print("you need to write: rock, paper or sissors")

    if computer==3:
         print ("computer wins the game") 
         break
    
    elif mann==3: 
        print("player wins the game")
        break

print("game is finneshed")

