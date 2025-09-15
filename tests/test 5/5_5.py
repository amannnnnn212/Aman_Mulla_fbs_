list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

list3=list1+list2
list4=[]
for i in range(len(list3)):
    if list3[i] not in list4:
        list4.append(list3[i])


print(list4)