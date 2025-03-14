row=5
for i in range(row):
    print(""*(row-i),end="")
    number=1
    for j in range(i+1):
        print(number,end="")
        number=number*(i-j)//(j+1)
    print()