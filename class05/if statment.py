age=int(input("write your age"))
if age<18:
    print("you are not adult")
else:
    print("you are adult")



print("---------------")

buy=int(input("how many oranges did you buy"))
buyp=int(input("what is the buying price"))
sell=int(input("how many oranges did you sell"))
sellp=int(input("what is the selling price"))

if (buyp*buy)<sell*sellp:
    print("profit")
    print("profit is:",(sell*sellp) - (buy*buyp))

else:
    print("loss")
    print("loss is:", (buy*buyp)-(sell*sellp))


print("-------------")

n=int(input("write the number"))

if n%17==0:
    print("yes it is")
else:
    print("no it isn't")