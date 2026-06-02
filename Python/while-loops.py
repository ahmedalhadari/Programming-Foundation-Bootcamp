
# While Loops
# infinite loop
# count = 0
# while count < 10:
#     print (count)


# count = 0
# while count < 10:
#     print (count)
#     count += 1

# while True:
#     number = int(input("Enter Number"))
#     if number == 0:
#         break


# print ("GoodBye! Number ")

# while True:
#     name = input("Enter Name")
#     if name == "Ahmed":
#         break

# print ("GoodBye!  Name")

# + - / *
# n = 0
# n += 1  # Same as n = n + 1
# n = n + 1
# n *= 3 # Same as n = n * 3
# n /= 2 # Same as n = n / 2
# n -= 2 # Same as n = n - 2

# print (n)

# n = 10
# while n > 0:
#     print (n)
#     n -= 1

# while  True:
#     cmd = input("Enter command: ")
#     if cmd == "quit":
#         break
#         print (f"You typed: {cmd}")

# age = -1

# while age < 0 or age > 95:   # Same 0 < age < 95
#     text = input ("Enter Age: ")
#     if text.isdigit():
#         age = int(text)
#     else:
#         print ("Enter Numbers Only: ")
# print (f" Ok, {age}")

# Old way
# line = input("Enter Value: ")
# while line != "":  # Ahmed
#     print(line)
#     line = input("Enter Value again :")

# New way — assign and test in one expression
# while (line := input("Enter Number ")) != "":
#     print(line)

# Print only odd numbers
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print (i)

# for i in range(5):
#   pass  
# x = 0


# Nested Loops 
# 2D loops 
# for i in range(5):
#     for j in range (3):
#         print (f"(i: {i}, j: {j})", end="   ")
#     print ()


# for i in range(5):
#     for j in range (5):
#         print (f"{j}", end=" ")
#     print()
    
for i in range(5):
    for j in range (5):
        print (f"*" * j, end=" ")
    print()
