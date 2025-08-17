# 1 2 3 4 5 
# 2     5 
# 3   5
# 4 5
# 5

for i in range(1,6):
    for j in range(i,6):
        if(i==2 and j==3):
            print(' ',end=' ')
        elif(i==2 and j==4):
            print(' ',end=' ')
        elif(i==3 and j==4):
            print(' ',end=' ')
        else:
             print(j,end=' ')
    print()