class human:

    def __init__(self,namevalue,age,high):
        print("constructer of human class is called")

        self.name=namevalue
        self.age=age
        self.high=high

    def eat(self):
        print(self.name,"is eating")

    def sleep(self):
        print(self.name,"is sleeping")

    def introduce(self):
        print(self.name,self.age,self.high)


akash=human("Akash",30,160)
semih=human("Semih",16,140)

akash.eat()
semih.eat()

akash.sleep()
semih.sleep()

akash.introduce()
semih.introduce()

print("name value in akash object is : ",akash.name)
print("name value in semih object is : ",semih.name)
