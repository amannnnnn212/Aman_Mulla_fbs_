# 7. Python Program to Find the Intersection of Two Lists

def intersect(li1,li2,li4):

    for i in range(len(li1)):
        if li1[i] in li2:
            li4.append(li1[i])

    return li4



li1 = [3, 4, 1, 2]
li2 = [5, 6, 3, 4]

li4=[]
print("Origional list :",li1,li2)
result=intersect(li1,li2,li4)

print("\nThe common element in bith list is : ",result)