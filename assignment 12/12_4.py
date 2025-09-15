# 4. Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged

str="aman mullas"


first=str[0]
last=str[-1]

str2 = last + str[1:-1] + first

print(str2)


