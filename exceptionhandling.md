
                                             Exception Handling


The requirement for handling exceptions in Python arises when an error occurs that can cause the program to terminate. Errors interrupt the flow of the program at the point where they appear, so any further code stops executing. This error is called an exception.


Different types of exceptions in python:
 In Python, there are several built-in Python exceptions that can be raised when an error occurs during the           execution of a program. Here are some of the most common types of exceptions in Python:
SyntaxError: This exception is raised when the interpreter encounters a syntax error in the code, such as a misspelled keyword, a missing colon, or an unbalanced parenthesis.
TypeError: This exception is raised when an operation or function is applied to an object of the wrong type, such as adding a string to an integer.
NameError: This exception is raised when a variable or function name is not found in the current scope.
IndexError: This exception is raised when an index is out of range for a list, tuple, or other sequence types.
KeyError: This exception is raised when a key is not found in a dictionary.
ValueError: This exception is raised when a function or method is called with an invalid argument or input, such as trying to convert a string to an integer when the string does not represent a valid integer.
AttributeError: This exception is raised when an attribute or method is not found on an object, such as trying to access a non-existent attribute of a class instance.
IOError: This exception is raised when an I/O operation, such as reading or writing a file, fails due to an input/output error.
ZeroDivisionError: This exception is raised when an attempt is made to divide a number by zero.
ImportError: This exception is raised when an import statement fails to find or load a module

Features
Custom Exceptions: Handle specific errors such as negative numbers or division by zero with custom error messages.
Standard Exception Handling: Demonstrates handling built-in exceptions like ZeroDivisionError, TypeError, and FileNotFoundError.
Raising Exceptions: Shows how to raise custom exceptions to signal errors in the program.
File Handling: Handles exceptions when working with files, including checking for file existence.
Multiple Operations: Demonstrates multiple exception handling scenarios in a single function, such as dividing numbers, calculating square roots, and reading files.
finally Block: Ensures that certain code (like cleanup or logging) is always executed after the try-except block, even if an exception is raised.
