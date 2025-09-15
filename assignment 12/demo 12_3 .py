# # to find the count 
# # count={}

# # for ch in str1:
# #     if ch in count:
# #         count[ch]+=1
# #     else:
# #         count[ch]=1

# # print(count)

# str1="listen"
# str2="silent"
# c=0
# c1=0
# for i in str1:
#     c+=1

# for i in str2:
#     c1+=1

# if(c!=c1):
#     print("not an anagram")
# else:
#     count={}
#     count1={}
#     for ch in str1:
#         if ch in count:
#             count[ch] += 1
#         else:
#             count[ch] = 1
    
#     for ch in str2:
#         if ch in count1:
#             count1[ch] += 1
#         else:
#             count1[ch] = 1

# if(count1==count):
#     print("anagram string ")
# else:
#     print("not an anagram string ")



























str="aman"
str2="aman"
c=0
c1=0

for i in range(len(str)):
    c+=1
for i in range(len(str2)):
    c1+=1


if(c!=c1):
    print("not an anagram")
else:

    count1=""
    count2=""    

    for c in str:
        if c in str:
            count1+=c 
        else:
            count1 = c     
            
    for c in str2:
        if c in str2:
            count2 += c
        else:
            count2 =c
    if(count1!=count2):
        print("no")
    else:
        print("yes")
        


