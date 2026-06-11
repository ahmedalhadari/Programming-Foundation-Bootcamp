class Animal:   
    def __init__(self, name):
        self.animal_name = name
    def speak(self):
        print (self.animal_name)
        
        
class Person: 
    name = "Omar"
    def __init__(self, name , age):
        self.p_name = name
        self.p_age = age
    def myfunc(self):
        print ("Hello my name is " + self.p_name)
        return 5