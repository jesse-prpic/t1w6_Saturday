# Simple calculator using if-else statements

# Get user inputs
num1 = float(input("Enter first number:"))
operation = input("enter operations (+, -, *,/):")
num2 = float(input("Enter second number:"))

# Perofrm calculation using if else statements
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result = "Error! INvalid Operation"

print(f"The result is: {result}")