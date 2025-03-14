'''
Develop a simple calculator using Python. The program should:
- Ask the user to enter two numbers (use input function).
- Store these numbers in two separate variables.
- Convert the input strings into integers or floats.
- Calculate and print the sum of these two numbers.
- For example, if the user enters 5 and 3, the program should print "The sum of 5 and 3 is 8."
'''

num1 = (input('Enter first number '))
num2 = (input('Enter second number '))
num1=float(num1)
num2=float(num2)
sum=num1+num2
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))