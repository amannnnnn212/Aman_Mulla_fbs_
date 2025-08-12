# 8. Write a program to swap two numbers using third variable.

num1=int(input("enter first number="))
num2=int(input("enter second number="))

num3=num1

num1=num2
num2=num3

print(f'number 1={num1} number 2={num2}')