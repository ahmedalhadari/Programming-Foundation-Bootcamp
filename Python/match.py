day = 9
if day == 1:
    print("Saturday")
elif day == 2:
    print("Sunday")
elif day == 3:
    print("Monday")
elif day == 4:
    print("Tuseday")
elif day == 5:
    print("Wednesday")
elif day == 6:
    print("Thursday")
elif day == 7:
    print("Friday")
else:
    print("Error")

day = 2
age = 18
x = 0
match day:
    case 1 | 1.0 | 1.00:
        print("Saturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuseday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    case _:
        print("Error")
