from abc import ABC,abstractmethod
class Tesla(ABC):
    def __init__(self):
        print("tesla class constructor")
    
    def battery(self):
        print("tesla is runnin on battery")
    
    def fuel(self):
        print("tesla is runnin on fuel")

    @abstractmethod
    def autodriwe(self):
        pass

class Model1(Tesla):
    def __init__(self):
        super().__init__()
    
    def autodriwe(self):
        print( "now tesla is autodriwing")
    
a1=Model1()
a1.autodriwe()