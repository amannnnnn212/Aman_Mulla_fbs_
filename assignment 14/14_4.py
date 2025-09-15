# 4. Write a Python program that finds all pairs of elements in a list whose
# sum is equal to a given value.

li=[2,4,6,8,10]
print("list : ",li)
target=int(input("enter number to targer in the list :"))

for i in range(0,len(li)):
    for j in range(1+i,len(li)):
        if li[i]+li[j] == target: 
            print(li[i],"+",li[j],"=",target)


