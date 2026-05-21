age = 18
if age >= 18:
    print("Adult")
# another form
x = 1
y = 2

if age >= 18:
    x = 10
    y = 20
    print("Adult")

if age >= 18:
    x = 10
    y = 20
    print("Adult")

age = 18
if age >= 65:
    print("Adult")
else:
    print("Child")

age = 20
status = "Adult" if age >= 18 else "Child"
print(status)

number = 5
print("Even" if number % 2 == 0 else "Odd")

age  = 10
print (f"You are {'Adult' if age >=18  else 'Child'}")
