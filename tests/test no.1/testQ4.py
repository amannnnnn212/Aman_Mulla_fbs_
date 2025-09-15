height=float(input("enter lenght of wall ="))
width=float(input("enter breadth of wall ="))

area= height * width * 2



print(f'thr area of one room is {area}')

print(f'the area of second room is {area}')

area= area + area

print(f'the area of total rooms is={area}')

f_interior=float(input("enter  first interior cost="))

f_exterior=float(input("enter first exterior cost="))

cost_firstroom= f_interior + f_exterior

cost_firstroom=area * cost_firstroom

print(f'the cost of first room ={cost_firstroom}')


s_interior=float(input("enter   second interior cost="))

s_exterior=float(input("enter  second exterior cost="))

cost_secondroom= f_interior + f_exterior

cost_secondroom=area * cost_secondroom

print(f'the cost of first room ={cost_firstroom}')
print(f'the cost of second room ={cost_secondroom}')

cost=cost_firstroom + cost_secondroom

print(f'the finnal cost is {cost}')