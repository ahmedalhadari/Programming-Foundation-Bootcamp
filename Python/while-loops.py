    
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

# while age < 0 or age > 95:   # Same 0 > age > 95
#     text = input ("Enter Age: ")
#     if text.isdigit():
#         age = int(text)
#     else:
#         print ("Enter Numbers Only: ")
# print (f" Ok, {age}")

 # Old way
    # line = input("> ")
    # while line != "":
    #     print(line)
    #     line = input("> ")

#     # New way — assign and test in one expression
# while (line := input("Enter Number ")) != "quit":
#     print(line)