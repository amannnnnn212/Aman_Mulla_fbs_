# 4. Python Program to Find the Second Largest Number in a List Using Bubble
# Sort

# for i in range(len(li)):
#     if(li[i] > max):
#         smax=max
#         max=li[i]
#     elif(li[i]>smax):
#         smax=li[i]
    

def second_max():
    for i in range(1,len(li)):
        for j in range(0,len(li)-1):
            if(li[j] > li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
                
    return li[-2]


li=[1,18,30,28,2,3,4,5,6,7,11]

result=second_max()

print("Second Largest element is : ",result)
