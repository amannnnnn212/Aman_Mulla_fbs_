# 2. Python Program to Remove the nth Index Character from a Non-Empty
# String

def string(str,n,str2):

    for i in range(len(str)):
        # print(ch)
        if (i == n):
            # str2+=str[i]
            continue
        else:
            str2+=str[i]
    return str2            

str="Aman Mulla"
print("String before sort : ",str)
n=int(input("enter index of string to remove  = "))
str2=""
   
result=string(str,n,str2)

print("String after sort : ",result)