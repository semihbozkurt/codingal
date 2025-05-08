class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    
    def info(self):
        print(self.make , self.model, self.year)

class car(vehicle):
    def __init__(self, make, model, year,doornum):
        super().__init__(make, model, year)
        self.doornum=doornum
    
    def carinfo(self):
        print(self.make, self.model, self.year, self.doornum)

class motorcycle(vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar=has_sidecar
    def motorcycleinfo(self):
        print(self.make , self.model , self.year , self.has_sidecar)

v1=car("car","toyota",2009,4)
v2=motorcycle("motorcycle","kawasaki",2000,True)

v1.info()
v1.carinfo()
v2.info()
v2.motorcycleinfo()
