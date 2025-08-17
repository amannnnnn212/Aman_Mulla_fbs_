#         1 
#       1   1 
#     1   2   1
#   1   3   3   1
# pascle tringle

# for i in range(1,5):
#     for j in range(1,5-i):
#         print(' ',end=' ')
#     for j in range(1,i+1):
#         print(f'  {j}',end=' ')
#     print()

for i in range(0,4):
    for j in range(0,3-i+1):
        print(' ',end='')
        num = 1
    for j in range(0,i+1):
        print('',num,end='')
        num = num*(i-j)//(j+1)
    print()