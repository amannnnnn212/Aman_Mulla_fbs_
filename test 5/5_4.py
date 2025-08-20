#  WAP entered number is palidrome or not using recursion function


def r_palindrome(num,total=0):

    if(num==0):
        return 0
    else:
        return r_palindrome(num//10,total=total*10+ num%10)
    
def palindrome(num):
    return num==r_palindrome
num=int(input("enter number = "))
d=0
temp=num    
result1=r_palindrome(num,)
result=palindrome
if(result):
    print("entered number is palindrome ")
else:
    print("entered number is not palindrome ")