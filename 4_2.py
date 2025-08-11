# 2.  WAP to print all odd numbers until n.

num=int(input("enter number= "))
print("odd number : ")
for num in range(1,num+1):
    if(num%2==0):
        pass
    else:
        print(num,end=' ')
