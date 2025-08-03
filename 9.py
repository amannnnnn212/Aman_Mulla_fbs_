# 9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

marathi=float(input("enter marathi marks : "))
hindi=float(input("enter hindi marks : "))
english=float(input(" enter english marks : "))
c_science=float(input("inter computer science marks : "))
java=float(input("enter java marks : "))


total_marks= hindi+english+c_science+java+marathi

percentage= total_marks /500 * 100
print(f'total percentage={percentage}')

if( marathi < 35):
    print(" fail in marathi and ")
    if(hindi < 35):
        print("fail in hindi and")
        if(english< 35):
            print("fail in english and")
            if(c_science < 35):
                print("fail in computer science and")
                if(java < 35):
                    print(" fail in java and")


if(percentage >= 75 and percentage <=100):
    print("Pass With Distinction")
elif(percentage >= 60 and percentage <75 ):
    print("Pass With First Class")
elif( percentage >=50 and percentage< 60):
    print("Pass With Second Class")
elif( percentage >=40 and percentage <50):
    print("Pass With Third Class")
elif(percentage >=35 and percentage<40):
    print(" pass ")
else:
    print(" fail") 