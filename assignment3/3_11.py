#  Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

age1=float(input(" enter age of first person = "))
age2=float(input(" enter age of second person = "))
age3=float(input(" enter age of third person = "))
age4=float(input(" enter age of fourth person = "))
age5=float(input(" enter age of fifth person = "))
ticket_a1=float(input("enter ticker amout ="))

temp=ticket_a1
ticket_30= temp /100 *30 
ticket_60=temp /100 *50
ticket1= ticket_a1-ticket_30
ticket2=ticket_a1-ticket_60
total_amt=0


if(age1<=12):
    ticket1_1= ticket_a1-ticket_30 
    total_amt = total_amt+ticket1_1 
    print(f'ticket price for first person = {ticket1_1}')
elif(age1>59):
    ticket2_1=ticket_a1-ticket_60
    total_amt=total_amt+ticket2_1
    print(f'ticket price for first person = {ticket2_1}')
else:
    temp1=ticket_a1
    total_amt=total_amt+temp1
    print(f'ticket of first person is = {temp1}')

if(age2<=12):
    ticket1_2= ticket_a1-ticket_30
    total_amt=total_amt+ticket1_2
    print(f'ticket price for second person = {ticket1_2}')
elif(age2>59):
    ticket2_2=ticket_a1-ticket_60
    total_amt=total_amt+ticket2_2
    print(f'ticket price for second person = {ticket2_2}')
else:
    temp2=ticket_a1
    total_amt=total_amt+temp2
    print(f'ticket price for  second person = {temp2} ')

if(age3<=12):
    ticket1_3= ticket_a1-ticket_30
    total_amt=total_amt+ticket1_3
    print(f'ticket price for third person = {ticket1_3}')
elif(age3>59):
    ticket2_3=ticket_a1-ticket_60
    total_amt=total_amt+ticket2_3
    print(f'ticket price for third person = {ticket2_3}')
else:
    temp3=ticket_a1
    total_amt=total_amt+temp3
    print(f'ticket price for  third person = {temp3} ')

if(age4<=12):
    ticket1_4= ticket_a1-ticket_30
    total_amt=total_amt+ticket1_4
    print(f'ticket price for fourth person = {ticket1_4}')
elif(age4>59):
    ticket2_4=ticket_a1-ticket_60
    total_amt=total_amt+ticket2_4
    print(f'ticket price for fourth person = {ticket2_4}')
else:
    temp4=ticket_a1
    total_amt=total_amt+temp4
    print(f'ticket price for  fourth person = {temp4} ')

if(age5<=12):
    ticket1_5= ticket_a1-ticket_30
    total_amt=total_amt+ticket1_5
    print(f'ticket price for fifth person = {ticket1_5}')
elif(age5>59):
    ticket2_5=ticket_a1-ticket_60
    total_amt=total_amt+ticket2_5
    print(f'ticket price for fifth person = {ticket2_5}')
else:
    temp5=ticket_a1
    total_amt=total_amt+temp5
    print(f'ticket price for  fifth person = {temp5} ')

print(f'total amount of ticket = {total_amt}')



