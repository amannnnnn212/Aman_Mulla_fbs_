# write a program to check entered year is leap year or not 

def leap():

    num=int(input("enter year = "))

    return num

res=leap()

if(res%4==0):
    print(f'{res} year is leap year ')
elif(res % 100==0 and res % 400 ==0):
    print(f'{res} year is leap year')
else:
    print(f' {res} year is not a leap year')
