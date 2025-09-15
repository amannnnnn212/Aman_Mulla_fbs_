li=[8,2,3,1]

li1=[4,5,6]
li3=li+li1
max=li3[0]
li4=[]
for i in range(len(li3)):
    if(li3[i]< max):
        max=li3[i]
        li4.append(max)
print(li4)