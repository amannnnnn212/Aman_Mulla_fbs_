# 1 .WAP to print all even numbers until n.

num=int(input("enter number ="))

i=1
print("even number is : ")
while(i<=num):
    if(i%2==0):
        print(i)
    i=i+1

# second logic 
for num in range(0,num+1,2):
    print(num)
    if(num%2==0):
        print(num,end=' ')

# third logic
for num in range(1,num+1):
    if(num%2==0):
        print(num,end=' ')