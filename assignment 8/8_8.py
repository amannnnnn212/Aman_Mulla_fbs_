# write a program find reverse of a number 

def reverse(num):

    temp=num
    for i in range(1,num+1):
        d1=temp%10
        temp=temp//10
        print(d1,end=' ')
        if(temp==0):
            break

    return d1

x=int(input("enter number = "))
# reverse(x)

res=reverse(x)



