# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

unit=int(input("enter units = "))
temp=unit

if( unit >0 and unit<=50):
    temp1=unit*0.50
    temp1=  temp1+temp1 /100 *20
    print(f'the total electricity bill is = {temp1}')
elif(unit>50 and unit <=150):
    temp2=unit*0.75
    temp2=temp2+temp2/100*20
    print(f'the total electricity bill is = {temp2}')
elif(unit >150 and unit<=250):
    temp3=unit * 1.20
    temp3=temp3+temp3/100*20
    print(f'the total electricity bll is = {temp3}')
elif(unit >250):
    temp4= unit * 1.50
    temp4=temp4+temp4/100*20
    print(f'the total electricity bill is = {temp4}')
else:
    print("enter invalid units")