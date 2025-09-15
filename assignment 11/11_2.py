# 2. Python Program to Merge Two Lists and Sort it

def short(li3):
    
    
    for i in range(1,len(li3)):
        for j in range(0,len(li3)-1):
            if(li3[j] > li3[j+1]):
                li3[j],li3[j+1]=li3[j+1],li3[j]
    return li3
   
    
li1=[3,1,2,7]
li2=[6,4,5,8]
li3=[]

li3=li1+li2
print("List before sorting : ",li3)
res=short(li3)

print("list after sorting : ",res)
