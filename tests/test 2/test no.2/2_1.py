# write a pogram  to print first n prime number

num=int(input("enter number= "))
count=0
while(count<num):
    for i in range(2,num):
        if(num%i==0):
            print(f'{num} is not prime number')
    else:
        print(f'{num} is prime number ')
        num=num+1
# count+=1