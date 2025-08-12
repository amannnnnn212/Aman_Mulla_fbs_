# 3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a1=float(input("enter angle 1= "))
a2=float(input("enter angle 2="))
a3=float(input("enter angle 3="))

t=a1+a2+a3 
if( t == 180):
    print(f'  trangle is valid ')
else:
    print("tringle is invalid")