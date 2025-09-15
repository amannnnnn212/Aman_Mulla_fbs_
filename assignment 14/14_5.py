# 5. Write a Python program to find the longest common prefix of all
# strings. Use the Python set.

li=["aman","amanmulla","amanmullafrom"]

prefix=list()
res=""
for i in range(0,len(li)+1):
    for j in range(1,len(li)):
        if li[0][i]==li[j][i]:
            continue
        else:
            break
    
    else:
        res= res+li[0][i]

print(res)
