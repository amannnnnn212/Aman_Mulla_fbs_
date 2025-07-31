# odd even
# num=int(input("enter any number"))

# if(num%2==0):
#     print(f'{num} is odd number')

# else:
#     print(f'{num} is even number')

age=int(input("enter age ="))

gender=input("enter gender(M/F)")

if((gender=="MALE,male" and age>=21 ) or (gender=="female,FEMALE" and age >=18)):
    print("eligible for marrige")

else:
    print("not eligible for marriage")