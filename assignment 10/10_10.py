# 10. Write a program to remove all occurrences of a given element in the list.


# num1=int(input("enter number to create list  = "))
# li=[]
# for i in range(1,num1+1):
#    li.append(i)
   
li=[1,2,3,2,4,2,5,2,6,2,7,2]
print(li)


num=int(input("enter number to remove in list= "))
li2=[]
for i in range(len(li)):

    if (li[i]!=num):
     li2.append(li[i])

print(li2)   

