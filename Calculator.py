number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

summary = number1 + number2
print("The summary of two numbers is", summary)

subtraction = number1 - number2
print("The subtraction of two numbers is", subtraction)

multiply = number1 * number2
print("The multiplication of the two numbers is", multiply)

if number2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    division = number1 / number2
    print("The division of two numbers is", division)