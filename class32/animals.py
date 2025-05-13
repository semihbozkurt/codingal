class animal:
    def speak(self):
        print("animal speaks")
class dog(animal):
    def speak(self):
        print("bark")
class cat(animal):
    def speak(self):
        print("meaw")
    
A1=cat()
A2=dog()
A3=animal()

A1.speak()
A2.speak()
A3.speak()
