# 3. Write a program to find the second largest element in the list.

li=[10,2,50,45,75,85,44,65]

max=li[0]
smax=li[0]
for i in range(1,len(li)):

    if(li[i] > max ):
        smax=max
        max=li[i]
    elif( li[i] > smax):
        smax=li[i]

print("Maximum Number = ",max)
print("Second Maximum Number = ",smax)