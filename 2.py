# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
 
a=input("enter alfabet=")

if( a in "a,e,i,o,u"):
    print(f'{a}  it is vowel ')
elif(a in "A,E,I,O,U"):
    print(f'{a} it is vowel')
else:
    print("constant character")