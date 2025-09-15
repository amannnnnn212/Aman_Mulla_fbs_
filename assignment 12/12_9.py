# 9. Python Program to Calculate the Number of Words and the Number of
# Characters Present in a String

def calculate(str,count):
    for c in str:
        if(c==' '):
            count+=1
    return count

str="aman mulla from india and he is completed his degree"
count=1

res=calculate(str,count)

print("total words in string : ",res)