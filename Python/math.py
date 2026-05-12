import math, random
number = -5 
print (f"Print the Absolute Value of ({number}): {abs(number)}")
number = 2.501
print (f"Round the number ({number}) is: {round(number)}")
number = 5
print (f"The power of ({number}) is: {pow(number, 2)} ")
print (f"The min value on {(3,5,-1,10,2,)} is: {min(3,5,-1,10,2,)}")
print (f"The max value on {(3,5,-1,10,2,)} is: {max(3,5,-1,10,2,)}")
print (f"The sum value of {(3,5,-1,10,2,)} is: {sum([3,5,-1,10,2,])}")
print (f"the mod value of (17, 5) is: {divmod(15,5)}")
number = 3.9
print (f"convert ({number}) to int: {int(number)} ")
number = 3
print (f"convert ({number}) to float : {float(number)}")
print (f"The Binary value of ({number}) is: {bin(number)}")
print (f"The Octal value of ({number}) is: {oct(number)}")
print (f"The Hex value of ({number}) is: {hex(number)}")
number = 16
print (f"The Square Root of ({number}) is: {math.sqrt(number)}")
number = 3.9999999999999
print(f"The round down of ({number}) is: {math.floor(number)}")
number = 3.0000001
print(f"The round up of ({number}) is: {math.ceil(number)}")
number = 3.9
print(f"The truncate  of ({number}) is: {math.trunc(number)}")
number = 5
print(f"The factorial of ({number}) is: {math.factorial(number)}")

print (f"This is a random integer {random.randint(1, 10)}")
print (f"This is a random float {random.uniform(1.0, 10.0)}")
number1, number2 = 5, 8
print (f"{number1}, {number2}")
number1, number2 = number2, number1
print (f"{number1}, {number2}")
