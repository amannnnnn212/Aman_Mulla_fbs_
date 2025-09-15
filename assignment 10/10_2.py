# 2. Write a program to find maximum and minimum element in a list.

li=[10,20,5,55,88,44,75]

max=li[0]
min=li[0]

for i in range(1,len(li)):

    if(li[i] > max):
        max=li[i]
    elif(li[i] < min):
        min=li[i]

print("Maximum Number = ",max)
print("Minimum Number = ",min)

    