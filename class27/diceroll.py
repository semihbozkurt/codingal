import random
while True:
    dice=random.randint(1,6)
    print(dice)
    ask=input("continue (c) or finish (f)")
    if ask=="c": pass
    elif ask=="f": break

print("program finished.")
