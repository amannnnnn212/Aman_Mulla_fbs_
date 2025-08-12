side1=float(input("enter side 1= "))
side2=float(input("enter side 2= "))
side3=float(input("enter side 3= "))

if(side1+side2>side3 and side3+side2>side1 and side1+side3>side2):
    print("tringle is valid")
else:
    print("tringle is invalid")
