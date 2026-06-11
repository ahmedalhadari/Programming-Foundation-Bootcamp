# class Animal:    # Parent Class
#     def __init__(self, name):
#         self.animal_name = name
#     def speak(self):
#         print (self.animal_name)

# class Cat(Animal):
#     pass
# ani1 = Animal("Catty")
# cat1 = Cat("Meme")
# ani1.speak()
# cat1.speak()


# Adding new methods in the child class

# class Animal:   # Parent
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print (f"{self.name} is eating ....")

# ani1 = Animal("Cat")
# ani1.eat()

# class Dog(Animal):   # Dog is the child and Animal is the Parent
#     def bark(self):
#         print (f"{self.name} says: Woof!")

# buddy = Dog("Buddy")
# buddy.eat()
# buddy.bark()


# Overriding methods - replace parent's method version

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print (f"{self.name} makes a sound ")

class Dog(Animal):
    def speak(self):
        print (f"{self.name} syas: Woof!")

dog1 = Dog("Doggy")
dog1.speak()
# class Cat(Animal):
#     def speak(self):
#         print (f"{self.name} syas: Meow!")

# buddy = Dog("Buddy")
# buddy.speak()
# cat1 = Cat("Catty")
# cat1.speak()


# super () - call the parent's method version

# class Vehicle:
#     def describe(self):
#         print ("This is a Vehicle")

# class Car (Vehicle):
#     def describe(self):
#         super().describe()
#         print ("This is a Car")
# car1 = Car()
# car1.describe()

# Multi-level Inheritance

# class Vehicle:
#     def __init__(self, wheels):
#         self.wheels = wheels

# class Car(Vehicle):
#     def __init__(self, brand):
#         super().__init__(4)
#         self.brand = brand

# class ElectricCar(Car):
#     def __init__(self, brand, battery):
#         super().__init__(brand)
#         self.battery = battery
        
# ec = ElectricCar("Tesla", 75)
# print (ec.wheels, ec.brand, ec.battery)
