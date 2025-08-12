# 3. WAP to print sum of series upto n.

num=int(input("enter number = "))
total=0
for num in range(1,num+1):
    total=total+num

print(f'Sum = {total}')
