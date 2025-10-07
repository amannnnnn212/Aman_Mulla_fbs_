# 3. Count the number of spaces in a string (take input from user)

# sum() adds up all the numbers in that list

string=input("enter input :")

str=sum([1 for ele in string if ' '== ele])
# c=0
# for i in string:
   
#     if i==' ' :
#         c+=1

print("Total space in the string is",str)