# 12. Python Program to count number of lowercase characters in a string.

def count_lowercase(str,count):
    for ch in str:
        if (ord(ch)>=97 and ord(ch)<=122):
            count+=1
    return count


str="Aman Mulla"
count=0
result=count_lowercase(str,count)

print("the count of total lowercase character is :",result)

