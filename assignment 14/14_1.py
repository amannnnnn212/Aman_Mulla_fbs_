# 1. Write a Python program to find elements in a given set that are not in
# another set.

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

set3=set()

# print(set1.difference(set2))

for i in range(1,len(set1)+1):
    if(i not in set2 ):
        set3.add(i)

print("origional set",set1,set2)
print(" the elements that are present in the first set but not in the second set :",set3)

