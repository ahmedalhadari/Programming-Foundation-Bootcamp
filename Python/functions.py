# def greeting():
#     print ("Hello, Tuwaiq Academy!")

# greeting()
# if True:
#     greeting()

# for i in range (3):
#     greeting()


# def greeting_by_name(name):
#     print (f"Hello, {name}")

# greeting_by_name("Ahmed")

# def add(a, b):
#     print (f"The sumation of {a} and {b} is: ", end="")
#     print (f"{a + b}")
# add (5, 5)

# def sub(a, b):
#     print (f"The subtraction of {a} and {b} is: ", end="")
#     print (f"{a - b}")
# sub (5, 6)

# def square(price, qty):
#     # print ("This is the start of Function")
#     # print (price * qty)
#     # print ("This is the end of Function")
#     total = price * qty
#     return total
# total_price = square(1, 10)
# print(total_price)

# # total_with_vat = total_price + (total_price * 0.15)
# # print (total_with_vat)


# def test ():
#     print ("hi")
#     #return "Ahmed"

# print (test())

# def min_max(numbers):
#     return min(numbers), max(numbers), "Ahmed"


# print(min_max([5, 10, 25, 1, 7, 0, 500]))
# min_number, max_number, name = min_max([5, 10, 25, 1, 7, 0, 500])
# print (max_number)


# def safe_devide (a, b):
#     if b == 0:
#         return "Error: Divide by Zero"
#     return a/b
# print (safe_devide (10, 5))


# def describe (name, age, city):
#     print(f"{name}, {age}, {city}")

# describe (14, "Dammam", "Sara")


# def describe (name, age, city):
#     print(f"{name}, {age}, {city}")

# describe (age=14, city="Dammam", name="Sara")

# Default Values
# def greet(name, greeting="Hello"):
#     print (f"{greeting}, {name}")

# greet ("Mohammed", "Salam")


# def total (*numbers):
#     return sum(numbers)

# print (total (1,2,3,65,6,5,89,8))

# SCOPE
# def calculate ():
#     result = 100
#     print (result)

# calculate()
# print (result) # It will not work (Out of scope)

# Local VS Global

# x_globale = 10    # Global Variable
# def show():
#     x_globale = 50
#     print ("Inside : ", x_globale)
# show()
# print ("Outside: ", x_globale)


# Recurcive Function
# def factorial(n):
#     if n <=1:
#         return 1
#     return n * factorial(n-1)

# print (factorial(5))

# DOCSTRING - Documentation for Functions

# def add (a, b):
#     """
#     This functiont is returning the sum of a and b.
#     """
#     return a + b
# # print (add(5,6))
# #help(add)
# print(add.__doc__)


# Pass a Dict to a Function
# student = {"Name":"Ali", "age": 26, "city": "Khobar", "programs":{"name":"IT", "topics": "Programming, Networking"}}

# def describe (**details):
#     for key, value in details.items():
#         print (f"{key}: {value}")

# name = "Ahmed"
# describe(**student)


# # Decorators
# def welcome_decorator(func):
#     def wrapper():
#         print ("Your are Student!")
#         print ("Here is another Decore")
#         func()
#         print ("Hi, You are welcome!")
#         print ("Here is another Decore 2026")

#     return wrapper

# @welcome_decorator
# def say_hello():
#     print ("Hello!")


# # call Function
# say_hello()


# def add_mango(func):
#     def wrapper(*flavor):
#         print (f"You add mango {flavor} 🥭")
#         func(*flavor)
#     return wrapper
# def add_chocolate(func):
#     def wrapper(*flavor):
#         print (f"You add chocolate {flavor}🍫")
#         func(*flavor)
#     return wrapper

# @add_chocolate
# @add_mango
# def get_ice_cream(flavor="Apple"):
#     print (f"Here is your {flavor} Ice cream 🍦")

# get_ice_cream()

# def func (a, b, *args, c=10, **kwargs):
#     print (f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")


# func(1,2,3,4,5,c=99, x="Hello", y="hi")


# Function as Values
def double(x): return x*2
def triple(x): return x*3
# # stor the functions in a list
# funcs = [double, triple, 5]
# for f in funcs:
#     if callable(f):
#         print (f(5))
#     else:
#         print("Error")

# # double(5)
# # triple(5)
# # 5(5)

# def double(x): return x*2
# # Pass a function as argument 
# def apply (func, value):
#     return func(value)


# print (apply(double, 5))
