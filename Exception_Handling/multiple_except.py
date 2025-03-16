'''
You can handle multiple exceptions using multiple except blocks or a single block for multiple exception types.
'''

try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input, not a number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("The result is:", result)
finally:
    print("Execution finished.")
