# # WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.


salary=int(input("enter salary= "))

da=salary*10/100
ta=salary/100*12
hra=salary/100*15


total_salary=salary-da-ta-hra

print(f'basic salary= {total_salary}')