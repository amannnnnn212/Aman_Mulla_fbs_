# 1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

def replace(str,str2):
    for ch in str:
        if(ch =='a'):
            # print('m',end='')
            str2+= '$'
        else:
            str2+= ch
    return str2

str="bananaa"
str2=""

print("orogional string : ",str)
result=replace(str,str2)
print("list after replace'a' with '$' :"  ,result)