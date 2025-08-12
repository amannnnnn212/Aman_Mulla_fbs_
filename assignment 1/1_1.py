# 1. Write a program to calculate the percentage of student based on marks of any 5 subjects.

h=int(input("enter marks in hindi ="))
m=int(input("enter marks in marathi ="))
e=int(input("enter marks in english ="))
c_s=int(input("enter marks in compute science ="))
j=int(input("enter marks in java ="))

total_marks=h+m+e+c_s+j

percentage  = (total_marks/500)*100

print(f'total percentage is = {percentage}%')