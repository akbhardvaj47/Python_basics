
row=5
col=5
for i in range(row):
    for j in range(col):
        if i==j or i+j==row-1:
            print("   ",end="")
        else:
            print(" * ",end="")
    print()
      