# 7. Given two sets of numbers, write a Python program to find the missing
# numbers in the second set as compared to the first and vice versa.
# Use the Python set.

def difference_number(set1,set2):
    li=[]
    for i in set1:
        if i not in set2:
            li.append(i)
    print("missing set2 from (set1) : ",li)
    li2=[]
    for i in set2:
        if i not in set1:
            li2.append(i)
    print("missing set1 from (set2) : ",li2)
    
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 6}

difference_number(set1,set2)
