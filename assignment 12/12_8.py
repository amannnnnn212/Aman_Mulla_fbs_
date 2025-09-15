# 8. Python Program to Remove the Characters of Odd Index Values in a
# String
def odd(str,str2):
    for c in range(len(str)):
        if (c % 2 ==0):
            str2+=str[c]
    return str2

str="aman mulla"
str2=""
print("origional string : ",str)
res=odd(str,str2)

print("after removing odd index :",res)