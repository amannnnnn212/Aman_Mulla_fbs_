# 9. Write a program to calculate the m to the power n using recursion.

def power(n,m):
    if m==0 :
        return 1
    else:
    #     total=1
    #     for i in range(1,m+1):
    #         total*=n
        return n * power(n,m-1)
    
n=int(input("enter number = "))
m=int(input("enter m ="))
total=0
result=power(n,m)
print("Total = ",result)

# num=int(input("enter number = "))
# m=int(input("enter 'M' value = "))
# total=0
# total1=num*num
# for i in range(1,m-1):
#     total1*=num

# print("Total = ",total1)