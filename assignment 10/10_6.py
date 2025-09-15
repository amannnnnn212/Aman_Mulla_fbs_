# 6. Write a program to remove duplicates from the list.

li1=[1,2,3,1]

unique_list=[]

for i in li1:
    if i not in unique_list :
        unique_list.append(i)


print(unique_list)