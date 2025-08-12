# 9. Write a program to swap two numbers without using third variable.


num1=int(input("enter first number="))
num2=int(input("enter second number="))

num2=num1+num2

num1=num2-num1
num2=num2-num1

print(f'number 1={num1} number 2={num2}')