class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move (self):
        print ("Drive!")
        
class Boat: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move (self):
        print ("Sail!")
     
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print ("Fly!")
car1 = Car("TOYOTA", "Camry")
boat1 = Boat("Ibiza", "Touring 20") 
plan1 = Plane("Boeing", "747")

for fun in (car1, boat1, plan1):
    fun.move()
    