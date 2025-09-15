# 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.

li1=[1,2,3,4,5]

li2=[]

for i in range(len(li1)):
    t=li1[i]
    li2+=[t]

print("original list =",li1)

print("Duplicate List = ",li2)
