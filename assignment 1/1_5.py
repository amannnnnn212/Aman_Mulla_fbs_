# 5. Write a program to calculate area of an equilateral triangle.

p=int(input("enter amount = "))
r=int(input("rate of intrest %="))
t=int(input("time (months,year)="))

s_i=p*r*t/100

print(f'simple intrest = {s_i}')

c_i=s_i+s_i/100* 1 / 2 *r

print(f'compound intrest = {c_i}')