# 6. fibbonacci

def fibbo(num):
    a=0
    b=1
    
    for i in range(0,num+1):
        print(a,end=' ')
        c=a+b
        b=a
        a=c
x=int(input("enter number = "))

fibbo(x)


