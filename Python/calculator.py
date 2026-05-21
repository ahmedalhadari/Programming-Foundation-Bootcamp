n1 = float(input("Enter Number 1: "))
n2 = float(input("Enter Number 2: "))
op = input("Enter Operator ")
match op:
    case "+":
        print (n1 + n2)
    case "-":
        print (n1 - n2)
    case "*":
        print (n1 * n2)
    case "/":
        if n2 == 0:
            print ("Error: Division by Zero")
        else:
            print (n1 / n2)
    case _:
        print ("Unknown Operator")
    