'''
Print the multiplication table of a given number using nested loops.
Input: 5

Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
'''
num=int(input('Enter number '))
for i in range(1):
    for j in range(1,11):
        print(f'{num} * {j} = {num*j}')
    print()