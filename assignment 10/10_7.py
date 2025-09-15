# 7. Write a program to create a new list from existing list which contains cube of
# each number of list.

li=[1,2,3,4,5]
li2=[]
for i in range(len(li)):
    t=li[i]**3
    li1=[t]
    li2+=li1
    
print(li2,end=' ')



