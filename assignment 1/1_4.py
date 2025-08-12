# 4. Write a program to enter P, T, R and calculate simple Interest.

p=int(input("enter amount = "))

r=int(input("rate of intrest %="))

t=int(input("time (months,year)="))

s_i=p*r*t/100

print(f'simple intrest = {s_i}')