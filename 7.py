# 7. Write a program to check if user has entered correct userid and password.

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