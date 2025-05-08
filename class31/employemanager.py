class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def info(self):
        print(self.name ,"\n", self.salary)

    def bonus(self,amount):
        self.salary+=amount
        print("new salary is: ", self.salary)

class Manager(Employee):
    def __init__(self, name, salary,groupsize):
        super().__init__(name, salary)
        self.groupsize=groupsize


e1=Employee("Ali", 20000)
m1=Manager("veli",30000,12)

m1.bonus(5000)
e1.bonus(2000)

m1.info()
e1.info()
    
