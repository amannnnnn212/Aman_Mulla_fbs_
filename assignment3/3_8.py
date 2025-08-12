# # 8.Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)


u=float(input("enter userid ="))
p=(input("enter password ="))

# temp1= u
# temp2=p
print("rewrite same user id and password :")
a= float(input("enter userid ="))
b= (input("enter password ="))

if(a==u and b==p):
    print("correct username or password")
else:
    print("incorrect username or password")
import random 

captcha =random.randint(1111, 9999)

print(f'the four digit code = {captcha}')

p2=int(input(" enter four digit code = "))

if(p2 == captcha):
    print("successful login")
else:
    print("failled")

