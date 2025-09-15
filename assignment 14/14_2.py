# 2. Write a Python program to remove the intersection of a second set
# with a first set.

# remove first set element  present in the second set 

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

set3=set()
for i in set1:
    if i not in set2:
        set3.add(i)

print(set3)