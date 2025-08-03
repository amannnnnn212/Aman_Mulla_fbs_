# 7. Write a program to check if user has entered correct userid and password.

uid=input("enter user id =")
pas=int(input(" enter password="))

if((uid=='aman') and (pas==1234)):
    print("correct username or password")
else:
    print("incorrect username and password")