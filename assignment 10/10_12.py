# 12. Write a program to create three lists of numbers, their squares
# and cubes

li1=[1,2,3,4,5]
li2=[6,7,8,9,10]
li3=[11,12,13,14,15]
print("first List : ",li1)
print("Second list :",li2)
print("Third list :",li3)
li4=[]
li5=[]
li6=[]
li7=[]
li8=[]
li9=[]
temp=0
for i in range(len(li1)):
    temp=li1[i]**2
    li4.append(temp)
print("\nSqure of first list : ",li4)

for i in range(len(li1)):
    temp=li1[i]**3
    li5.append(temp)
print("\nCube of first list :",li5)

for i in range(len(li2)):
    temp1=li2[i]**2
    li6.append(temp1)
print("\nSqure of second  list : ",li6)


for i in range(len(li2)):
    temp2=li2[i]**3
    li7.append(temp2)
print("\nCube of second list :",li7)


for i in range(len(li3)):
    temp=li3[i]**2
    li8.append(temp)
print("\nSqure of third list : ",li8)

for i in range(len(li3)):
    temp3=li3[i]**3
    li9.append(temp3)
print("\nCube of third list :",li9)