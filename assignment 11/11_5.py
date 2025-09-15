# 5. Python Program to Sort a List According to the Length of the Elements
# within the list.

# ["apple", "kiwi", "banana", "fig", "grapes"]

# o/p 
# ['fig', 'kiwi', 'apple', 'grapes', 'banana']

li=[[40,50,60],[10],[20,30,70,80,90]]

sum=0

for i in range(len(li)):
    for j in range(0,len([i])):
        sum+=[i][j]
        print(li[i])
