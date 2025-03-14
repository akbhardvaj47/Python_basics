'''
Print the following pattern using nested loops:

1
22
333
4444
55555
'''
row=6
col=6
for i in range(1,row):
    for j in range(1,i+1):
        print(i, end=' ')
    print()    
