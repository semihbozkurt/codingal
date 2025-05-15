rakam = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1)
]




class Roman:
    def __init__(self,num):
        self.num=num
        


    def transfer(self):
        num=self.num
        romen=""
        for key,value in rakam:
            while num>=value:
                romen+=key
                num-=value

        return romen
    
    def __str__(self):
        return self.transfer()
    


giris=int(input("write a integer: "))

if 0<giris<4000:
    print("roman number is: ",Roman(giris))

else:
    print("unexepteble number!")

