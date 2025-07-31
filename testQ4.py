height=int(input("enter lenght of wall ="))
width=int(input("enter breadth of wall ="))

area= height * width * 4



print(f'the cost of one room is {area}')

print(f'the cost of second room is {area}')

area= area + area

print(f'the cost of total rooms is={area}')