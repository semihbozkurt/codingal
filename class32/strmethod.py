class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class employee(person):
    def __init__(self, name, age,ID):
        super().__init__(name, age)
        self.ID=ID
    def __str__(self):
        return(f"name: {self.name}, age: {self.age}, employeeID: {self.ID}")

emplo=employee("jason","28","1220275932")
pers=person("ali",15)

print(emplo)
print(pers)

    
