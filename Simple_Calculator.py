"""
This is an intermediate calculator consisting of five operations
"""

def add(first_value, second_value):
    """
    The function of the addition of two values
    Args:
        first_value (float): The first number to add
        second_value (float): The second number to add
    Returns:
        float: The result of the addition
    """
    return first_value + second_value

def subtract(first_value, second_value):
    """
    The function of the subtraction of two values
    Args:
        first_value (float): The number to subtract from
        second_value (float): The number to subtract
    Returns:
        float: The result of the subtraction
    """
    return first_value - second_value

def multiply(first_value, second_value):
    """
    The function of the multiplication of two values
    Args:
        first_value (float): The first number to multiply
        second_value (float): The second number to multiply
    Returns:
        float: The result of the multiplication
    """
    return first_value * second_value

def divide(first_value, second_value):
    """
    The function of the division of two values
    Args:
        first_value (float): The number to divide
        second_value (float): The number to divide by
    Returns:
        float: The result of the division
    Raises:
        ValueError: If the second value is zero
    """
    if second_value == 0:
        raise ValueError("Cannot divide by zero")
    return first_value / second_value

def power(first_value, second_value):
    """
    The function of the power of two values
    Args:
        first_value (float): The base number
        second_value (float): The exponent
    Returns:
        float: The result of the power operation
    """
    return first_value ** second_value

def print_result(operation, result):
    """
    Prints the result of an operation
    Args:
        operation (str): The operation string (e.g. "2 + 3")
        result (float): The result of the operation
    """
    print(f"{operation} = {result}")

def calculator():
    """
    This is the body of our calculator of intermediate program
    """
    print("""
        Select the operation choice
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5. Power
        0. Exit
          """)
    
    while True:
        try:
            choice = int(input("Enter the choice between 0-5: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 5.")
            continue
        
        if choice == 0:
            print("Exiting calculator...")
            break
        
        if choice not in [1, 2, 3, 4, 5]:
            print("Invalid option of operation. Please try again.")
            continue
        
        try:
            first_value = float(input("Enter the first value: "))
            second_value = float(input("Enter the second value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if choice == 1:
            print_result(f"{first_value} + {second_value}", add(first_value, second_value))
        elif choice == 2:
            print_result(f"{first_value} - {second_value}", subtract(first_value, second_value))
        elif choice == 3:
            print_result(f"{first_value} * {second_value}", multiply(first_value, second_value))
        elif choice == 4:
            try:
                print_result(f"{first_value} / {second_value}", divide(first_value, second_value))
            except ValueError as e:
                print(e)
        elif choice == 5:
            print_result(f"{first_value} ** {second_value}", power(first_value, second_value))
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()
