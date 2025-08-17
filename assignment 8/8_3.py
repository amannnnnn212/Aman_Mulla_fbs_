# write a program to find sum of following siries using function
    
#     1. 1+2+3+.....n
#     2. 1!+2!+3!+.....n!
#     3. 1^1+2^2+3^3+....n^n

def sum():

    num=int(input("enter number = "))
    temp=0
    for i in range(1,num+1):
        temp+=i
    print(f'sum ={temp}')
    fact=1
    for i in range(1,num+1):
        fact*=i
    print(f'factorial = {fact}')
    t=0
    for i in range(1,num+1):
        t=t+i*i
    print(f'exponentil = {t}')
sum()


