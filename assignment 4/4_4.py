# 4. WAP to print factorial of a number .

num=int(input("enter number= "))

t=1
for i in range(1,num+1):
    t=t*i
print(f'factorial = {t}')

# while(i<=num ):
#     t=t*i
#     i+=1

# print(t)