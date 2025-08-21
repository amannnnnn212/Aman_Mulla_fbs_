# 10. Write a program to reverse a number using recursion.

def reverse(num,total):
    if(num==0):
        return total
    else:
        return  reverse(num // 10, total * 10 + num % 10)
        
    
num=int(input("enter number = "))
total=0
digit=0
i=0
temp=num
result=reverse(num,total)

print('reverse number = ',result)


# for i in range(1,num):
#     digit=temp%10
#     total=total*10+digit
#     temp=temp//10
#     if(temp==0):
#         break

# print(total)