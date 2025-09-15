# 1. Python Program to Put Even and Odd elements of a List into two Different
# Lists

def evenodd(li,li1,li2):
    for i in range(len(li)):
        if(li[i]%2==0):
            li1.append(li[i])
        else:
            li2.append(li[i])
    print("Even number :",li1)
    print("Odd Number : ",li2)           
    
li=[1,2,3,4,5,6,7,8,9,10]
li1=[]
li2=[]
evenodd(li,li1,li2)

