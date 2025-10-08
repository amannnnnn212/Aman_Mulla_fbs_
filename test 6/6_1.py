import function

from function import two_wheelers
from function import three_wheelers
from function import four_wheelers
from function import heavy_vehicle


ch=0

while ch!='5':
    print('''Stop the vehicle 
    1.two wheeler :
    2.three wheeler :
    3.four wheeler :
    4.heavy vehicle :
    5.exit :
    ''')

    ch=input("enter choice :")

    if (ch=='1'):
        # function.two_wheelers()
        num=int(input("enter number of pasanger :"))
        b=two_wheelers(num)
        b.cal_toll()
    elif(ch=='2'):
        # function.three_wheelers()
        num=int(input("enter number of pasanger :"))
        t=three_wheelers(num)
        t.cal_toll()
    elif(ch=='3'):
        num=int(input("enter number of pasanger :"))
        c=four_wheelers(num)
        c.cal_toll()
        # function.four_wheelers()
    elif(ch=='4'):
        # function.heavy_vehicle()
        num=int(input("enter number of pasanger :"))
        h=heavy_vehicle(num)
        h.cal_toll()
    elif(ch=='5'):
        print("thank you visit again...")
    else:
        print('''invalid input.
            try again...''')