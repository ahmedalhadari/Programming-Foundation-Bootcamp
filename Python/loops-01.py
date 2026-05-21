# for _ in range(10):
#     print("Hello")

# stars = []
# for _ in range(5):
#     stars = []
#     stars.append("*")
#     print (stars)

# Repeat a question
# for _ in range(3):
#     name = input("Enter your name:")
#     print (f"Hi {name}")


# # Counting
# for i in range (5):
#     print (f"{i}")


# for i in range (1, 12):
#     print (f"{i}")


# for i in range (5, 10):
#     print (f"{i}")

# Count with step
# for i in range (1, 11, 2):
#     print (f"{i}")

# for i in range (5, 51, 5):
#     print (f"{i}")

# for i in range (10, 0, -1):
#     print (f"{i}")

# for i in range (100, -1, -10):
#     print (f"{i}")

# for i in range (5, 5): # Print Nothing
#     print (f"{i}")

# for i in range (10, 5, -1):
#     print (f"{i}")

# Looping on Collections (list, tuple, and set)
# Loop over List
# fruits = ["Apple", "Banana", 1, [1,2,3,4], True]
# for fruit in fruits:
#     print (f"{fruit}", end="")

# Loop over tuple
# point = (3, 4, 5)
# for p in point:
#     print (f"{p}")

# Loop over set
# colors = {"Red", "Green", "Blue", "White"}
# for color in colors:
#     print(f"{color}")

# loop over s string
# for letter in "Programming in Python":
#     if letter != " ":
#         print (f"{letter}", end="")

# enumerate()
# fruits = ["Apple", "Banana", "Cherry"]
# for i, fruit in enumerate(fruits):
#     print(f"{i}: {fruit}")

# fruits = ["Apple", "Banana", "Cherry"]
# for i, fruit in enumerate(fruits, start=101):
#     print(f"{i}: {fruit}")

# zip() loop over multiple sequences in parallel

# names = ["Ali", "Sara", "Omer", "Ahmed"]
# ages = [17, 19, 14, 15]
# addresses = ["Riyadh", "Jeddah", "Dammam", "Khobar"]

# for name, age, address in zip(names, ages, addresses):
#     print (f"{name} is {age} and lives in {address}")


# for i in range (5):
#     print (f"{i}")
#     if i > 2:
#         print (f"i is greater than 2")
#         break

student = {
    "name": "Sara",
    "age": 23,
    "city": "Riyadh"
}

# for key in student:
#     print (key)


# for key in student.keys():
#     print (key)

# for value in student.values():
#     print (value)

# for key, value in student.items():
#     print(key)
#     print(value)

# # Loop over multiple structures

# # List of tuples
# points = [(1, 2), (3, 4), (5, 6)]

# for x, y in points:
#     print (f"x= {x}, y={y}")


# pairs = [("A", 1), ("B", 2), ("C", 3)]
# for letter, number in pairs:
#     print (f"{letter} = {number}")


# # Nested Unpacking
# students = [("Sara", (90, 50, 60)), ("Omer", (100, 20, 55))]
# for name, (mark1, mark2, mark3) in students:
#     print (f"{name}: {mark1}, {mark2}, {mark3}")

# for x in (1,2,3,4,5,6,7,8,9):
#     print (x)


# for x in reversed ([1,2,3,4,5,6,7,8,9]):
#     print(x)

# for letter in reversed("Python"):
#     print (f"{letter}", end="")
 
 
 
# for i in sorted([5,6,1,3,4,7,2,9,0,10]):
#     print (i)
# from itertools import count 
import time

# for i in count(1,2):
#     print (i)
#     time.sleep(1)
#     if i > 10:
#         break
    
