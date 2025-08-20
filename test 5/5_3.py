# 3. WAP to print following patterns :

#  * * * * * 
#        *   
#      *     
#    *       
#  * * * * * 

def pattern(num,i,j):

    
    for i in range(1,num+1):
        for j in range(1,num+1):
            if( i==1 or i==num or i+j==num+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


num=int(input("enter number = "))
i=0
j=0
pattern(num,i,j)