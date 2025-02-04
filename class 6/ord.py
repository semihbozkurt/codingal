#variable =input("Enter a symbol: ")

# you have to check whther the entered symbol is alphabet or not

# A-Z or a-z

#print(ord(variable))

# math, bio, phy,chem

# total

# percentage

# grade

#m+p+c+bi/400 *100

#65-90


x=input("enter a symbol")
if 65<=ord(x)<=90 or 97<=ord(x)<=122:
   print("yes it is a alphabet letter")
else:
   print("no its not a alphabet letter")