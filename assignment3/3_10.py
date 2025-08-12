 # 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)

age=float(input(" enter age = "))
gender=(input("enter gender (M/F) = "))


if((age >=21 and gender=='male') or ( age >=18 and gender =='female')):
    print("eligible for marriage")
elif((age <21 and gender=='male') or ( age <18 and gender =='female')):
    print("not eligible for marriage")
else:
    print("Invalid key ")