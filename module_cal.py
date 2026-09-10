def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed!"
        return num1 / num2
    else:
        return "Invalid operator! Only +, -, *, / are allowed!"


if __name__ == "__main__":
    print("--- Simple Calculator ---")
    try:
        num1 = float(input("Enter the first number: "))
        op = input("Operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        result = calculate(num1, op, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter a valid number!")