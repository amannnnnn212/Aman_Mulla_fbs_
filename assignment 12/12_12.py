# 13. Python Program to count number of digits and letters in a string.

def count_d_l(str,digit,letter):

    for c in str:
        if(ord(c)>=65 and ord(c)<=122):
            
            letter+=1
        elif(ord(c)>=48 and ord(c)<=57):
            digit+=1
    print("after count digit :",digit)
    print("after count  :",letter)

str="Aman123 mulla321"
digit=0
letter=0
print("origional string :",str)
count_d_l(str,digit,letter)