# 8. Python Program to Count the Frequency of Words Appearing in a String Using
# a Dictionary

str="aman mulla aman"

dict={}

count=str.split(' ')

for i in count:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1

print(dict)
