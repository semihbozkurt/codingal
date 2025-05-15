rakam= {"I":1,
"IV":4,
"V":5,
"IX":9,
"X":10,
"XL":40,
"L":50,
"XC":90,
"C":100,
"CD":400,
"D":500,
"CM":900,
"M":1000}



romen=""
class roman:
    def __init__(self,num):
        self.num=num
    def transfer(self,num):
        for key,value in rakam:
            while num>=value:
                romen+=key
                num-=value

        return romen
    
giris=int(input("write a integer"))

if 0<giris<4000:
    print("roman number is: ",roman(giris).transfer)

else:
    print("unexepteble number!")

    