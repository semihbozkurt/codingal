class exemple:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        sum=self.x+other.x
        sumy=self.y+other.y
        return exemple(sum,sumy)
    def __str__(self):
        return (f"this object id: {id(self)} and values: x: {self.x}   y: {self.y}")
    
o1=exemple(10,100)
o2=exemple(20,200)

print(o1+o2)
