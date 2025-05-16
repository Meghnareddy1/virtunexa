import logging
import math  # Import the math module
import sys # Import the sys module

# Configure logging
logging.basicConfig(filename="calculator.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(x, y):
    """
    Adds two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtracts two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The difference of x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divides two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The quotient of x and y.
    
    Raises:
        ZeroDivisionError: If y is zero.
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y

def power(x, y):
    """
    Calculates x to the power of y.

    Args:
        x (float): The base number.
        y (float): The exponent.

    Returns:
        float: x raised to the power of y.
    """
    return math.pow(x, y)

def square_root(x):
    """
    Calculates the square root of a number.

    Args:
        x (float): The number.

    Returns:
        float: The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(x)

def get_input(operation_name=""):
    """
    Gets user input for a number, handling potential errors.

    Args:
        operation_name (str, optional): The name of the operation for the prompt. Defaults to "".

    Returns:
        float: The valid number entered by the user.
    """
    while True:
        try:
            prompt_text = f"Enter number for {operation_name}: " if operation_name else "Enter number: "
            num = float(input(prompt_text))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            logging.warning("Invalid input entered by user.")

def get_operator():
    """
    Gets the operator from the user.

    Returns:
        str: The operator entered by the user.
    """
    while True:
        operator = input("Enter operator (+, -, *, /, ^, sqrt): ")
        if operator in ('+', '-', '*', '/', '^', 'sqrt'):
            return operator
        else:
            print("Invalid operator. Please enter a valid operator.")
            logging.warning("Invalid operator entered by user.")

def main():
    """
    Main function to run the calculator program.
    """
    print("Welcome to the Calculator!")
    logging.info("Calculator started")

    while True:
        try:
            operator = get_operator()

            if operator == 'sqrt':
                x = get_input("square root")
                result = square_root(x)
                print(f"The square root of {x} is {result}")
                logging.info(f"Square root of {x} is {result}")
            else:
                x = get_input("first")
                y = get_input("second")

                if operator == '+':
                    result = add(x, y)
                    print(f"{x} + {y} = {result}")
                    logging.info(f"{x} + {y} = {result}")
                elif operator == '-':
                    result = subtract(x, y)
                    print(f"{x} - {y} = {result}")
                    logging.info(f"{x} - {y} = {result}")
                elif operator == '*':
                    result = multiply(x, y)
                    print(f"{x} * {y} = {result}")
                    logging.info(f"{x} * {y} = {result}")
                elif operator == '/':
                    result = divide(x, y)
                    print(f"{x} / {y} = {result}")
                    logging.info(f"{x} / {y} = {result}")
                elif operator == '^':
                    result = power(x, y)
                    print(f"{x} ^ {y} = {result}")
                    logging.info(f"{x} ^ {y} = {result}")
                else:
                    print("Invalid operator") #This part of the code will never be reached

            another = input("Do another calculation? (yes/no): ")
            if another.lower() != 'yes':
                break
        except Exception as e:
            print(f"Error: {e}")
            logging.error(f"An error occurred: {e}")

    print("Thank you for using the Calculator!")
    logging.info("Calculator ended")

if __name__ == "__main__":
    main()
