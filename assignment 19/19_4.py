# 4. Remove all of the vowels in a string (take input from user)


string=input("enter string :")

str=tuple(ele for ele in string if ord(ele) not in [65,69,73,79,85,97,101,105,111,117])

for i in str:
    print(i,end=' ')




