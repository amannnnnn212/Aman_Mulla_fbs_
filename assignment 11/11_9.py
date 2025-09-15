# 9. Write a program to create three lists of numbers, their squares and cubes

def cube_squre(li,li2,li3):
    sum=1
    for i in range(1,len(li)+1):
        sum = i*i
        li2.append(sum)

    for i in range(len(li)):
        li3.append(li[i] ** 3)


li=[1,2,3,4,5]
li2=[]
li3=[]
print("Origional list is :",li)

cube_squre(li,li2,li3)

print("\nSqure of given list is :",li2)
print("\nCube of given list is :",li3)