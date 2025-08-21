# 7. Write a program to find sum of digits using recursion.

def sum(num):
    if(num==0):
        return 0
    else:
        return (num%10) + sum(num//10)
    
num=int(input("enter number = "))
temp=num
result=sum(num)
print('the sum of the number is : ',result)

 