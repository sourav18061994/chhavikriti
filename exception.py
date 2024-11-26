# Custom exception class
class NegativeNumberError(Exception):
    """Exception raised for errors in the input if number is negative."""
    def __init__(self, number, message="Number cannot be negative"):
        self.number = number
        self.message = message
        super().__init__(self.message)

class DivisionByZeroError(Exception):
    """Exception raised for division by zero."""
    def __init__(self, message="Cannot divide by zero"):
        self.message = message
        super().__init__(self.message)


# Function to demonstrate handling multiple exceptions
def divide_numbers(a, b):
    try:
        if b == 0:
            raise DivisionByZeroError("You attemLpted to divide by zero!")
        result = a / b
    except DivisionByZeroError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Both inputs must be numbers!")
    else:
        print(f"Result: {result}")
    finally:
        print("Execution of divide_numbers function completed.")


# Function to demonstrate handling negative number input with custom exception
def square_root(number):
    try:
        if number < 0:
            raise NegativeNumberError(number)
        result = number ** 0.5
        print(f"Square root of {number} is {result}")
    except NegativeNumberError as e:
        print(f"Error: {e.message} ({e.number})")
    except TypeError:
        print("Error: Input must be a number!")
    else:
        print("Square root calculation successful.")
    finally:
        print("Execution of square_root function completed.")


# Function demonstrating how to raise a custom exception
def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age < 18:
            raise ValueError("You must be at least 18 years old.")
        print(f"Valid age: {age}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Execution of validate_age function completed.")


# Demonstrating use of exception handling with a file operation
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError as e:
        print(f"Error: An IOError occurred: {e}")
    finally:
        print("Execution of read_file function completed.")


# Function to demonstrate handling multiple exceptions in one try block
def perform_operations(a, b):
    try:
        # Division operation
        print(f"Trying to divide {a} by {b}...")
        result = a / b
        print(f"Result of division: {result}")
        
        # Invalid input scenario
        print(f"Trying to calculate square root of {a}...")
        result = a ** 0.5
        print(f"Square root of {a}: {result}")
        
        # Handling negative numbers with custom exception
        print(f"Trying to handle negative number {a}...")
        if a < 0:
            raise NegativeNumberError(a)
            
        # File reading operation
        read_file("nonexistent_file.txt")

    except ZeroDivisionError as e:
        print(f"Error: Division by zero is not allowed. {e}")
    except NegativeNumberError as e:
        print(f"Error: Negative number encountered: {e}")
    except ValueError as e:
        print(f"Error: Value issue encountered: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
    finally:
        print("Execution of perform_operations function completed.")


# Main function to invoke the different scenarios
def main():
    print("Exception Handling Demo\n")
    
    # Demonstrate divide_numbers
    print("Example 1: Divide Numbers")
    divide_numbers(10, 0)  # Division by zero case
    divide_numbers(10, 'a')  # Type error case
    divide_numbers(10, 2)  # Successful division case
    
    # Demonstrate square_root
    print("\nExample 2: Square Root")
    square_root(-4)  # Negative number case
    square_root(16)  # Valid number case
    square_root("sixteen")  # Type error case
    
    # Demonstrate validate_age
    print("\nExample 3: Validate Age")
    validate_age(15)  # Age less than 18
    validate_age(25)  # Valid age
    validate_age(-5)  # Negative age
    
    # Demonstrate perform_operations
    print("\nExample 4: Perform Multiple Operations")
    perform_operations(16, 4)  # Normal case
    perform_operations(16, 0)  # Division by zero
    perform_operations(-16, 4)  # Negative number case
    perform_operations("abc", 4)  # Invalid input type
    
    # Demonstrate file operation
    print("\nExample 5: File Handling")
    read_file("nonexistent_file.txt")  # File does not exist
    
    # Demonstrate generic exception handling
    print("\nExample 6: Generic Exception Handling")
    try:
        # Code that could raise an unexpected error
        result = 10 / 0
    except Exception as e:
        print(f"Caught an unexpected error: {e}")
    finally:
        print("End of generic exception handling example.")

# Entry point to execute the demo
if __name__ == "__main__":
    main()
