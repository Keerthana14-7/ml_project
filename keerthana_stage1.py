# input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

# calculation
if operator == "+":
    result = a+b
    print("Result =", result)

elif operator == "-":
    result = a-b
    print("Result =", result)

elif operator == "*":
    result = a*b
    print("Result =", result)

elif operator == "/":
    if b == 0:
        print("Error")
    else:
        result = a/b
        print("Result =", result)

else:
    print("Invalid operator")
