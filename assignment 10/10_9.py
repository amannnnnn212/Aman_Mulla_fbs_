# 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
# li2.append(j)
num=int(input("enter number = "))
li1=[]
li2=[]
li3=[]
for i in range(1,num+1):
    li1+=[i]

print(li1)

for j in range(len(li1)):
        if(li1[j] % 2 == 0 ):
            li2.append(li1[j])
        else:
             li3.append(li1[j])

print("All even number in the list is :",li2)


print("All odd number in the list is :",li3)


