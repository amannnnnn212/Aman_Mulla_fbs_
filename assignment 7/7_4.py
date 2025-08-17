#           1 
#         2 3 2 
#       3 4 5 4 3 2
#     4 5 6 7 6 5 4 3 2
#   5 6 7 8 9 8 7 6 5 4 3 2
temp=0
for i in range(1,6):
    for j in range(1,7-i):
        print(' ',end=' ')
    for i in range(i,i*2):
        print(i,end=' ')
    for j in range(2,i):
        temp=i-j+1
        temp=temp
        print(temp,end=' ')
    print()
