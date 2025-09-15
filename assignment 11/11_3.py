# 3. Python Program to Sort the List According to the Second Element in Sublist

def sort(li):
    for i in range(1,(len(li))):
        
        for j in range(0,len(li)-i):
            
            if (li[j][1]>li[j+1][1]):
                
                li[j],li[j+1]=li[j+1],li[j]
    
    return li




li=[(1, 2), (3, 4), (4, 7), (2, 5)]
print("Origional list :",li)
res=sort(li)

print("Sorted list :",res)