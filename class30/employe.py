class employe:
    def __init__(self,id,name,depart,salary):
        self.id=id
        self.name=name
        self.depart=depart
        self.salary=salary
    
    def info(self):
        print(self.id ,("\n") ,self.name , ("\n"),self.depart ,("\n") ,self.salary)

    def reise(self,amount):
        self.salary +=amount
        print(self.salary)

    def change(self,new):
        self.depart=new
        print(self.depart)


e1=employe("101","alice","HR",50000)
e2=employe("102","bob","engineer",70000)
e3=employe("103","charlie","marketing",60000)

e2.reise(5000)
e3.change("sales")

e1.info()
e2.info()
e3.info()


emplst=[e1,e2,e3]
for i in emplst:
    if i.salary>=60000:
        print(i.name)
