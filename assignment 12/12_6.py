# 6. Python Program to Take in a String and Replace Every Blank Space
# with Hyphen

def replace(str,str2):
    for ch in str:
        if(ch!=' '):
            str2+=ch
        else:
            str2+='-'
    return str2

str="Aman Mulla had completed his graduation"
str2=""

res=replace(str,str2)

print(res)