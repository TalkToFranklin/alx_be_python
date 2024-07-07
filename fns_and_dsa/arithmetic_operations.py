def perform_operation(num1, num2, operation):
    """
    This is a functions that performs basic arithmetic operations on the given numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (string): The arithmetic operation to perform ('add', 'subtract', 'multiply', or 'divide').

    Returns:
    float: The result of the arithmetic operation.
    """
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            else:
                return num1 / num2
        else:
            return "Error: Invalid operation"
    except ValueError:
        return "Error: Invalid input"


from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()