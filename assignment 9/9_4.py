# 4. Write a program to find sum of n numbers using recursion.

def sum(num):
    if(num==0):
        return 0
    else:
        return num +sum(num-1)
    
num=int(input("enter number = "))
temp=num
result=sum(num)
print('the sum of the number is : ',result)

 