# class Person:
#     name = "Ahmed"    # Properity or Attribute
#     age = 20
#     def walk ():     # Method or Behavior 
#         pass
# person1 = Person()   # Instance 

# class Student:
#     name = "Ahmed"
#     age = 17
#     def greet():
#         print ("HI")

# studen1 = Student()
# print (studen1.name)
# print (studen1.age)


# class Emp:
#     def __init__(self, name, age, email):
#         self.emp_name = name
#         self.emp_age = age
#         self.emp_email = email
    
# emp1 = Emp("Ahmed", 17, "ahmed@gmail.com")
# emp2 = Emp("Omar", 22, "omar@gmail.com")


# print (emp1.emp_name, emp1.emp_age, emp1.emp_email)   

# print (emp2.emp_name, emp2.emp_age, emp2.emp_email)   


class Person: 
    name = "Omar"
    def __init__(self, name , age):
        self.p_name = name
        self.p_age = age
    def myfunc(self):
        print ("Hello my name is " + self.p_name)
        return 5
    
person1 = Person("Mohammed", 32)
person2 = Person("Sara", 30)
print (person2.myfunc())
# print (Person.p_name)
# print(person1.name)