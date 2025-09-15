# 10. Write a program to print list after removing even numbers.

def even(li,li2):
    for i in range(len(li)):
        if(li[i]%2!=0):
            li2.append(li[i])
    return li2

li=[1,2,3,4,5,6,7,8,9,10,11,12,13,1,15,16,17,18,19,20]
li2=[]
print("origional list : ",li)

result=even(li,li2)

print("\nList after removing even number :",result)