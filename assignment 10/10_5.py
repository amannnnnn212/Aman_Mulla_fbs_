# 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

num=int(input("enter number = "))

li=[10,10,20,80,80]
total=0
for i in range(len(li)):
    if num == li[i] :
        total+=1

print("TOtal Number of present in the list = ",total)

