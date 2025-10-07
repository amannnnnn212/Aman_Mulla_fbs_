# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

string=input("enter string :")

temp=string.split(' ')

str={word : len(word) for word in temp  }

print(str) 