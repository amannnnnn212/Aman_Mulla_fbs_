# 4. Python Program to Generate a Dictionary that Contains Numbers (between 1
# and n) in the Form (x,x*x).

num=int(input("enter number to crete a dictionary :"))

dict={}
for i in range(1,num+1):

    dict[i] = i * i 

print(dict)
