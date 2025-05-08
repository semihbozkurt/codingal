class Car: 
    def __init__ (self,name,maxspeed,kilometer):
        self.name=name
        self.maxspeed=maxspeed
        self.kilometer=kilometer

class Bus(Car):
    def __init__(self, name, maxspeed, kilometer):
        super().__init__(name, maxspeed, kilometer)
    def info(self):
        print(self.name,self.maxspeed,self.kilometer)

buss=Bus("volvo",2000,100000)

buss.info()
