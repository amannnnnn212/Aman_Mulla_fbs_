# 10.Python Program to Take in Two Strings and Display the Larger String
# without Using Built-in Functions

def large(str1,str2,count1,count2):
    for c in str1:
        count1+=1

    for c in str2:
        count2+=1

    if(count1 == count2):
        print(str1,",",str2,": both are same lenght")
    elif(count1 > count2):
        print(f'{str1} : is larger string ')
    elif(count1 < count2):
        print(f'{str2} : is larger string ')


str1="amann"
str2="mulla"
count1=0
count2=0

large(str1,str2,count1,count2)