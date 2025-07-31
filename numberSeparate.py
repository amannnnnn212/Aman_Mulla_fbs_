# three digit number sepertion 

num=int(input("enter three digit number ="))

temp=num

d1= temp % 10

temp=temp // 10

d2= temp % 10

temp=temp//10

d3=temp % 10
temp= temp // 10
print(f' first number= {d3} second number={d2} third number ={d1}')
