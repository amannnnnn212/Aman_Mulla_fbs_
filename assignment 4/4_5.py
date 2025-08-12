# 5. WAP to print Fibonacci series upto n.

num=int(input("enter number = "))

a=-1
b=1

for i in range(0,num):
    c=a+b
    print(c)
    a=b
    b=c
 



