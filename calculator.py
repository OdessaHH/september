first = float(input("enter your first number: "))

operator = input("enter your operator: ")



second = float(input("enter your second number number: "))

if operator == "+":
    print("result is: ",first+second)
elif operator == "-":
    print("result is: ",first-second)
elif operator == "*":
    print("result is: ",first*second)
elif operator == "/":
    print("result is: ",first/second)
elif operator == "%":
    print("result is: ",first%second)
elif operator == "**":
    print("result is: ",first**second)
elif operator == "//":
    print("result is: ",first//second)
else:
    print("something is wrong")

