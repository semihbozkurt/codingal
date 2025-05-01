class car:
    def __init__(self,brandvalue,modelvalue,yearvalue):
        self.brand=brandvalue
        self.model=modelvalue
        self.year=yearvalue
    
    isstarted=False

    def start(self):
        print(self.brand,self.model)
        isstarted=True
        print(isstarted)

    def stop(self):
        print(self.brand,self.model)
        isstarted=False
        print(isstarted)

    def introduce(self):
        print(self.brand,self.model,self.year)

BMV=car("bmv","X5" ,"2022")
TESLA=car("tesla","model3","2023")

BMV.start()

TESLA.stop()

BMV.introduce()
TESLA.introduce()
