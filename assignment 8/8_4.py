# sum of all odd number between 1 to n 



def fact():

    num=int(input("enter number = "))
    fact=0
    for i in range(1,num+1):
        if(i%2==0):
            pass
        else:
            fact+=i
        
    return fact
result=fact()
print(f'the addition of all odd number  is  {result}')