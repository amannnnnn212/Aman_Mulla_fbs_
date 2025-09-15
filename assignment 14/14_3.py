# 3. Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

str="dog,cat,rat,cat,lion,cat,lion,rat,elephant"

li=[]

li=str.split(',')

dict={}

for i in li:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

for i,j in dict.items():
    print(i,"=",j,end=" ")

