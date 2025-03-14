list=[1,2,3,4,5,5,6,78,8]
print(max(list))

list=[1,2,3,4,5,5,6,78,8]
maxValue=list[0]
for i in list:
    if i > maxValue:
        maxValue=i
print(maxValue)