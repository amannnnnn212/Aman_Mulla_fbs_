# 3.Python Program to Detect if Two Strings are Anagrams

# to find the count 
# count={}

# for ch in str1:
#     if ch in count:
#         count[ch]+=1
#     else:
#         count[ch]=1

# print(count)


str="listen"
str2="silent"
c=0
c1=0

for i in range(len(str)):
    c+=1
for i in range(len(str2)):
    c1+=1


if(c!=c1):
    print("not an a anagram")
else:

    count1={}
    count2={}  

    for c in str:
        if c in count1:
            count1[c]+=1 
        else:
            count1 [c]= 1     
            
    for c in str2:
        if c in count2:
            count2 [c]+= 1
        else:
            count2 [c]=1
    if(count1!=count2):
        print("not an anagram ")
    else:
        print("anagram string ")
