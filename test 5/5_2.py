# 2. Write a program to find factorial of given number using recursion

def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
         

num=int(input("enter number = "))
res=fact(num)

print('factorial : ',res)