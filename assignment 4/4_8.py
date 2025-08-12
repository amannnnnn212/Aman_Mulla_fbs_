# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

num1=int(input("enter numbers="))
t=0
t1=0
for i in range(1,num1+1):
    if(i%7==0 and i%5==0):
        # t=t+i
        # print(t)
        print(f'{i} is  divisible by 7 and multiple of 5')
    # else:
    #     print(f'{i} is  not  divisible by 7 and multiple of 5')
