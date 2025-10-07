# 1. Find all of the numbers from 1–1000 that are divisible by 8

from prettytable import PrettyTable
table = PrettyTable()

print("Number which are divisible b 8 :")

table.field_names =[f'column{i+1}' for i in range(10)]

number=[ele for ele in range(1,1001) if ele % 8==0]

# for i in number:
#     table.add_row([i])

for i in range(0, len(number), 10):
    row = number[i:i+10]  # take next 10 numbers
    if len(row) < 10:      # if last row has less than 10, fill with empty strings
        row += [''] * (10 - len(row))
    table.add_row(row)

print(table)


# error ValueError: Row has incorrect number of values, (actual) 10!=1 (expected)