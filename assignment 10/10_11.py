# 11. Write a program to print all numbers which are divisible by m and n in the
# list.
print("m=5")
print("n=2")
num1=int(input("enter number to create a list :"))

m=5
n=2

li1=[]
li2=[]
for i in range(1,num1+1):
    li1.append(i)

print(li1)

for i in range(len(li1)):
    if li1[i] % m ==0 and li1[i] % n ==0 :
        li2.append(li1[i])
    

print("\nvalue is divisible by m and n is :",li2)