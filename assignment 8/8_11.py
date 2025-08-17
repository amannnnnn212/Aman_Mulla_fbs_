# write a program to check if a given number is armstrong number or not 


print("it is only show 3 and 4 digit armstrong number ")
def arm():
    num=int(input("enter number = "))
    if(num>=100 and num<=999):
        temp=num
        t=0
        for i  in range(1,num+1):
            d1=temp%10
            t+=d1*d1*d1
    
            temp=temp//10
            if(temp==0):
                break
        if(num==t):
            print(num,"number is armstrong")
        else:
            print(num,"number is not armstrong ")

    if(num>=1000 and num<=9999):
        temp=num
        t=0
        for i  in range(1,num+1):
            d1=temp%10
            t+=d1*d1*d1*d1
    
            temp=temp//10
            if(temp==0):
                break
        if(num==t):
            print(num,"number is armstrong")
        else:
            print(num,"number is not armstrong ")

arm()

