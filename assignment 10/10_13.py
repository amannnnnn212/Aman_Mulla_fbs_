# 13 . Write a program to print list after removing even numbers.

li1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
li2=[]
for i in range(len(li1)):

    if(li1[i] % 2 == 0):
        pass
    else:
        li2.append(li1[i])


print("List after removing all the even number",li2)
