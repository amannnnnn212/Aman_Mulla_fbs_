# 1. Write a function to which we pass a parameter and
# print the factors of a given number

def fact(num,i):

    for i in range(1,num+1):
        if(num%i==0):
            print(i,end=' ')
        
num=int(input("enter number = "))
i=0
fact(num,i)
