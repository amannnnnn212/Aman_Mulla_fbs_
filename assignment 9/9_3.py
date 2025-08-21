# 3. Write a program to reverse a given number using recursive function.

# def reverse1(num):

#     if(num==0):
#         return 0
#     else:
#         return 1+ reverse1(num//10)


def reverse(num,temp,t,i):
    if(num!=0):
        for i in range(1,num+1):
            d=temp%10
            print(d,end='')
            temp=temp//10
            if(temp==0):
                break

num=int(input("enter number = "))
temp=num
t=0
i=0
reverse(num,temp,t,i)
