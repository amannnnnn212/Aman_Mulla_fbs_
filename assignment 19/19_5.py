# 5. Find all of the words in a string that are less than 5 letters (take
# input from user)

string=input("Enter string :")

temp=string.split(' ')

str={word for word in temp  if len(word) < 5}

print(str)


# c={}
# for i in range(len(temp)):
#     word=temp[i]
#     c[word]=len(word)


# for i,j in c.items():
#     if j > 5 :
#         print(i)