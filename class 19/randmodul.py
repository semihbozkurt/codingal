import random

print("random")

random.seed(1234) #it is seedin a value every random will be the same 

x=random.random() # 0 - 1
y= random.randint(10,100) # something in between 10 and 100

print(x,"\n",y)

list=[12,13,27, 53, 94, 81]
print(random.choice(list))
name="Semih"
print(random.choice(name))


print("\nmath\n")

import math

print("square root of 9 : ",math.sqrt(16))

print("power of 2 : ",math.pow(2,5))

print("factorial of 5 : ",math.factorial(5))

print("floor of 5.6 : ",math.floor(5.6))

print("ceil of 5.6 : ",math.ceil(5.6))

print("pi value : ",math.pi)

print("e value : ",math.e)

print("sin value : ",math.sin(math.radians(90)))

print("cos value : ",math.cos(math.radians(90)))

