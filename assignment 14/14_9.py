# 9. Write a Python program to find all the unique combinations of 3
# numbers from a given list of numbers, adding up to a target number.

# def target_num1(li,target):
#     for i in range(len(li)):
#         for j in range(i,len(li)-1):
#             if (li[i]+li[j]+li[j+1]==target):
#                 print(li[i],"+",li[j],"+",li[j+1],"=",target)


def target_num(li,target):
    for i in range(len(li)):
        for j in range(i,len(li)):
            for k in range(j,len(li)):
                if li[i]+li[j]+li[k]==target and li[i]!=li[j]!=li[k]:
                    print(li[i],"+",li[j],"+",li[k],"=",target)
                    # return li[i],li[j],li[k]
                
li=[1,2,3,4,5,6]
print("oriogional list :",li)
target=int(input("enter number to target : "))

target_num(li,target)
# target_num1(li,target)
