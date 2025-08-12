# 7. WAP to print all integers upto n that aren’t divisible by 2 and 3.

num=int(input("enter number ="))

for i in range(1,num+1):
    if(i%2 !=0 and i%3!=0):
        print(f'{i} is not divisible by 2 and 3')
    # else:
    #     print(f'{i} is  divisible by 2 and 3 ')
    