# 15. Python Program to find larger string without using built-in functions.


def larger(str1,str2):
    count=0
    count1=0 
    for c in str1:
        count+=1
    for c in str2:
        count1+=1

    if(count > count1):
        print("larger strig is :",str1)
    else:
        print("larger strig is :",str2)


str1="Amanaa"
str2="mullaaa"

larger(str1,str2)