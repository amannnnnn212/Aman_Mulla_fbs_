# 1. Write a program to find sum of following series using recursive functions:

#  1! + 2! + 3! + 4! +..... + n!

def fact(n):

    if(n==0):
        return 1
    else:
        return n*fact(n-1)

def fact_n(n):
    if (n==0):
        return 1
    else:
        return fact(n) + fact_n(n-1) 
num=int(input("enter number = "))
temp=0
res=fact_n(num)

print("factorial is : ",res)