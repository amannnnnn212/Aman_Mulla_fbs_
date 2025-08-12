# 7. Find the sum of three-digit number.

val1=int(input("enter threee digit number ="))

temp=val1 

f_d=temp%10
temp=temp// 10

s_d=temp % 10
temp=temp // 10

t_d= temp %10
temp=temp // 10

print(f'third digit={f_d} second digit={s_d}  first digit={t_d} ')

sum=f_d+s_d+t_d

print(f'sum of three digit= {sum}')