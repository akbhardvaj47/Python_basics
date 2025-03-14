list=[1,2,2,3,4,5,6,3,8,77,6,5,4,3,2]
new_list=[]
for i in list:
    if i not in new_list:
        new_list.append(i)
print("Original list = ",list)
print("new list = ",new_list)