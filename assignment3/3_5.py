side1=float(input("enter angle 1= "))
side2=float(input("enter angle 2= "))
side3=float(input("enter angle 3= "))

# side4=side1+side2+side3

if(side1== side2 == side3):
    print("equilatoral tringle")
elif( side1 == side2):
    print("isosceles tringle")
elif( side1 != side2 !=side3):
    print("tringle is scalene")
# else:
#     print("invalid tringle")