# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
      - num1 (float): first number
      - num2 (float): second number
      - operation (str): one of 'add', 'subtract', 'multiply', 'divide'

    Returns:
      - float result for successful arithmetic operations
      - a string error message for division by zero or unknown operation
    """
    # Normalize the operation string (remove surrounding spaces, make lowercase)
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        # Handle division by zero explicitly
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        # Unknown operation - return a clear message the main script can show
        return f"Error: Unknown operation '{operation}'"
