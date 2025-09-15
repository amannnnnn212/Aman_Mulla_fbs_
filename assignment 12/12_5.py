# 5. Python Program to Count the Number of Vowels in a String

def vowel(str2,count):
    for ch in str2:
        if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
            count+=1
    return count

str="Aman mulla"
count=0
str2=str.lower()

result=vowel(str2,count)

print("numbers of vowels in a string : ",result)