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


input( "\n \n" )



mat=int(input("math"))
bio=int(input("biology"))
chem=int(input("chemistry"))
phy=int(input("physics"))
top=mat+bio+chem+phy
ort=top/4
if 90<=ort<=100:
   print("A")
elif 80<=ort<90:
   print("B")
elif 70<=ort<80:
   print("C")
elif 60<=ort<70:
   print("D")
elif 50<=ort<60:
   print("E")
elif ort<50:
   print("failure")
else:
   ("somthing went wrong please try again")
