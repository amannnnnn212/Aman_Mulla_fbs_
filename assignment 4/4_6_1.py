# 6. WAP to check if a given first 5  is prime number .

n=int(input("number ="))

count=0
num=2

while(count<num):
    for i in range(2,num):
        if(num%i==0):
            print(f'{num} is not prime number')
    else:
        print(f'{num} is prime number ')
        num=num+1
count+=1



