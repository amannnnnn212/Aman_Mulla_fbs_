# Write a program to calculate profit or loss.

c_p=float(input("enter cost price="))
# d_p=float(input("enter discount price = "))

s_p=float(input("enter selling price= "))
# d_p = c_p * d_p /100

total_cp= c_p 

# temp = d_p /100 * d_p 

# s_p = total_cp + d_p
print(f'cost price ={c_p}')
print(f'selling price={s_p}')

if(s_p> c_p):
    print("profit")
else:
    print(" loss")