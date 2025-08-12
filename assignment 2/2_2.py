# 2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

celsius=int(input("enter tempreture in celsius ="))

# tempreture= fahrenheit-32*5/9
tempreture=celsius * 9/5 +32

print(f'fahrenhit tempreture={tempreture}')