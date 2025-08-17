# write a program to find sum of digit of a number


def sum():

    num=int(input("enter number = "))
    total=0 
    temp=num
    for i in range(1,num+1):
        d1=temp%10
        temp=temp//10
        total+=d1
    return total

result=sum()

print(f'the sum of a number is {result}')