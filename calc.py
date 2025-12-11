number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))


operator = input("Enter operation (+, -, *, /): ")

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error: Division by zero")


