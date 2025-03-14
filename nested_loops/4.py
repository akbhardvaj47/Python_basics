'''
Print a 3x3 matrix using nested loops.
Output:
1 2 3
4 5 6
7 8 9
'''
row=4
col=4
for i in range(1,4):
    for j in range(1,4):
        print(i * 3 + j - 2, end=' ')
    print()


for i in range(1, 10):
    print(i, end=' ')
    if i % 3 == 0:
        print()
