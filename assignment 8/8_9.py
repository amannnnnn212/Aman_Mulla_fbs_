# write a program enter number is palindrome or not 
# 121 = 121

def reverse(num):

    temp=num
    t=0
    for i in range(1,num+1):
        d1=temp%10
        # t=t*10+d1
        t=t+d1*d1*d1
        # print(d1,end=' ')
        temp=temp//10
        if(temp==0):
            break
    return t

x=int(input("enter number = "))

res=reverse(x)

# print('\n',res)

if(res==x):
    print(f'{x} is palindrome number ')
else:
    print(f'{x} is not palindrome number ')


