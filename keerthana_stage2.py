# input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

# calculation
if operator == "+":
    result = a + b

elif operator == "-":
    result = a - b

elif operator == "*":
    result = a * b

elif operator == "/":
    if b == 0:
        print("Error")
        exit()
    else:
        result = a / b

else:
    print("Invalid operator")
    exit()

# result
print("Result =", result)

# check result
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")
