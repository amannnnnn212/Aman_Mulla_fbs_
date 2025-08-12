# 10. Write a program to reverse three-digit number.

val1=int(input("enter three digit number="))

temp=val1

f_d=temp % 10

temp= temp // 10

s_d= temp % 10
temp = temp // 10

t_d= temp % 10
temp= temp //10

print(f'first digit ={t_d} second digit ={s_d} third digit={f_d}')

print("reverse number is ")

print(f'reverse numers ={f_d}{s_d}{t_d}')