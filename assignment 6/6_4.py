# A
# AB 
# ABC 
# ABCD
# ABCDE


for i in range(1,7):
    for j in range(1,i):
        print(chr(64+j),end=' ')
    print()