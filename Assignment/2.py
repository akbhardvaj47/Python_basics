'''
Create a Python program that prompts the user to enter their age in years using the input
function. Convert this age from a string to an integer and store it in a variable. Then,
calculate and print the age in months (assume 12 months in a year). For example, if the user
enters "20", the program should output "You are 240 months old."
'''
# Age in years
userInputAge = input('Please Enter your Age in year!...')
age = int(userInputAge)   # Convert string value in integer value
finalAge=age*12           # Applying formula to convert the year in months
print('Your age in months is {}'.format(finalAge))
print('So you are {} months old'.format(finalAge))
