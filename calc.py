def calculator():
    """Performs basic arithmetic operations."""

    while True:  # Keeps the calculator running until the user chooses to exit
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue  # Prompts the user again if input is invalid

        operator = input("Enter the operation (+, -, *, /) or 'exit' to quit: ").strip()

        if operator == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if operator == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operator. Please enter +, -, *, or /.")
            continue  # Allows user to enter operator again if invalid


if __name__ == "__main__":
    calculator()
