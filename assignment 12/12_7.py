# 7. Python Program to Calculate the Length of a String Without Using a
# Library Function

def countt(str,count):
    for c in str:
        count+=1
    return count

str="Aman mulla"
count=0

res=countt(str,count)

print("the lenght of a string : ",res)