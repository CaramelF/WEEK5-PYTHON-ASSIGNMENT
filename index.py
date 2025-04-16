#Defining a class
class Smartphone: 
    def init(self, model):
        self.model = model

    def OS(self):
        print(f"{self.model} uses IOS")

Smartphone1 = Smartphone("model")
print(Smartphone1.model)

#Polymorphism

class iPhone(Smartphone): 
    def OS(self):
        print(f"{self.model} uses IOS") 

class Samsung(Smartphone): 
    def OS(self):
        print(f"{self.model} uses Android")

def Smartphone_OS(display):
    display.OS()

iPhone2 = iPhone("Pro-Max")
Samsung2 = Samsung("Galaxy S21")

Smartphone_OS(iPhone2)
Smartphone_OS(Samsung2)
