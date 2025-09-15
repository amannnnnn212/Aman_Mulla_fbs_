# 6. Python Program to Multiply All the Items in a Dictionary

dict={1:50,2:40,3:30,4:20,5:10}

sum=1
for j in dict:
    sum*=dict[j]

print("origional dictionary :",dict)
print("\nthe multiplication of all items in dictionary :",sum)