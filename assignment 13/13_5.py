# 5. Python Program to Sum All the Items in a Dictionary


dict={1:50,2:40,3:30,4:20,5:10}

sum=0
for i,j in dict.items():
    sum+=j

print("origional dictionary :",dict)
print("\nthe sum of all items items in dictionary :",sum)