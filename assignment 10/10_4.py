# 4. Write a program to reverse the list.
# incomplete 
li=[10,20,30,40]
reverse_li=[]
for i in range(1,len(li)+1):
    reverse_li.append(li[-i])
    # print(li[-i],end=' ')

print(reverse_li)