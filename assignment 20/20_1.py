# 1. We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.
from prettytable import PrettyTable

table=PrettyTable()

table.field_names=["Fibbonacci siries :"]

def fibbo():
    a=1
    b=-1
    while True :
        c=a+b
        yield c
        b=a
        a=c
res=fibbo()

num=int(input("Enter number to create Fibonnacci siries :"))

for i in range(1,num+1):
    table.add_row([next(res)])
    
print(table)



