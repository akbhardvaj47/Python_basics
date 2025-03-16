'''
Exception handling is a mechanism to handle runtime errors in a graceful manner without terminating the program unexpectedly. Python provides a robust way to handle exceptions using the try, except, else, and finally blocks.

try block: Code that might raise an exception is put in the try block.
except block: Catches and handles exceptions raised in the try block.
else block: Executes if no exception is raised in the try block.
finally block: Executes regardless of whether an exception was raised or not. It’s commonly used to clean up resources, like closing files or network connections.'''

try:
    x = 10
    y = 0
    result = x / y  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")    
else:
    print("No error occurred, result:", result)
finally:
    print("This block always executes.")
