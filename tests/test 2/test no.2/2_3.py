# q 3
total=0
num=int(input("enter employee number= "))
for i in range(1,num+1):
    salary=int(input("enter salary= "))
    if(salary<=20000):
        da=salary*10/100
        ta=salary/100*12
        hra=salary/100*15
    else:
        da=salary*15/100
        ta=salary/100*18
        hra=salary/100*20

    total_salary=salary-da-ta-hra
    total=total+total_salary

    print(f'basic salary= {total_salary}')

print(f'total salary of all emp={total}')