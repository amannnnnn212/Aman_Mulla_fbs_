
for i in range(1,6):
    for j in range(1,6):
        if((i+j)%2==0):
            print('1',end=' ')
    #     if(j%2==0):
    #         pass
    #     else:
    #         print('*',end=' ')
        else:
            print('0',end=' ')
    print()