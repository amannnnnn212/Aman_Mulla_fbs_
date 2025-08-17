#        A
#      A B C 
#    A B C D E
#  A B C D E F G I


for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end=' ')
    for j in range(1,i*2):
        print(chr(64+j),end=' ')
    print()