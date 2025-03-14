'''
Syntax =>
var_name = {key1:value1,
            key2:value2,
            ....}
'''

# Initialize a dictionary
menu={}

# Add element in dictionary
menu['Apple']=100
menu['Banana']=120

# Read a value
print(menu['Apple'])

# Update a value
menu['Apple']=150

# Remove element from dictionary
del menu['Apple']

# Find length of dictionary
print(len(menu))

# Clear a dictionary
menu.clear()

print(menu)
