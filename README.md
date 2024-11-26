                                                                Exceptionh                                          Exception Handling

This Python script demonstrates various ways to handle exceptions in Python using different techniques like try-except blocks, custom exceptions, and file handling. The script handles common errors such as division by zero, invalid input types, negative number handling, and more. It also demonstrates how to raise custom exceptions and catch multiple exceptions in one block.

Features
Custom Exceptions: Handle specific errors such as negative numbers or division by zero with custom error messages.
Standard Exception Handling: Demonstrates handling built-in exceptions like ZeroDivisionError, TypeError, and FileNotFoundError.
Raising Exceptions: Shows how to raise custom exceptions to signal errors in the program.
File Handling: Handles exceptions when working with files, including checking for file existence.
Multiple Operations: Demonstrates multiple exception handling scenarios in a single function, such as dividing numbers, calculating square roots, and reading files.
finally Block: Ensures that certain code (like cleanup or logging) is always executed after the try-except block, even if an exception is raised.

Requirements
Python 3.x

How to Run the Code
Clone or download the repository to your local machine.
Navigate to the directory containing the script.
Open a terminal or command prompt in the directory.
Run the script using Python by executing the following command:
bash
Copy code

python exception_handling_demo.py
The script will execute and demonstrate various exception handling scenarios.
Script Breakdown1. Custom Exception Classes
NegativeNumberError: Raised when an attempt is made to process a negative number for operations like square roots.
DivisionByZeroError: Raised when attempting to divide by zero.

1. Functions with Exception Handling
divide_numbers(a, b): Divides two numbers and handles ZeroDivisionError and TypeError.
square_root(number): Calculates the square root of a number, raises a custom NegativeNumberError if the input is negative.
validate_age(age): Validates an age input, raising a ValueError if the age is invalid (negative or under 18).
read_file(filename): Reads a file and handles file-related exceptions like FileNotFoundError and IOError.
perform_operations(a, b): A combination of multiple operations demonstrating handling of different exceptions.

2. Main Execution Flow
The main() function orchestrates the flow, calling each of the functions above and demonstrating how each handles different types of errors.
It also shows generic exception handling using the Exception base class for unexpected errors.

3. Exception Handling Mechanisms
try-except: Catches specific exceptions and handles them gracefully.
else: Executes if no exception was raised in the try block.
finally: Ensures the execution of cleanup or finalization code, regardless of exceptions.

Example Output
When running the script, the following types of output can be seen depending on the scenario:
Divide by Zero:
Copy code
Error: You attempted to divide by zero!
Execution of divide_numbers function completed.

Square Root of Negative Number:
typescript
Copy code
Error: Number cannot be negative (number = -4)
Execution of square_root function completed.

File Not Found:
javascript
Copy code
Error: The file nonexistent_file.txt does not exist.
handling
