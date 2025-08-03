# Write a program to check if given 3 digit number is a palindrome or not.

num1=int(input("enter any three digit number = "))

temp=num1

d1= temp % 10
temp=temp//10

d2= temp % 10
temp=temp//10

d3= temp % 10
temp=temp //10

print(f'{d3}\t {d2}\t {d1}')

reverse=(d1*100)+(d2*10)+d3

print(f'reverse number = {reverse}')

if(num1 == reverse):
    print("number is palindrome")
else:
    print("number is not palindrome")