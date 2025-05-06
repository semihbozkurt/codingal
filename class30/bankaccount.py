class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def addmoney(self,amount):
        self.balance+=  amount
        print(f"you add {amount} money, new balance is: {self.balance}")
    def takemoney(self,amount):
        try:
            self.balance-= amount
            print(f"you get{amount} money, new balance is: {self.balance}")  

        except:
            print("you dont have enough money")

    def balanceshow(self):
        print(self.balance)
    def nameshow(self):
        print(self.name)
