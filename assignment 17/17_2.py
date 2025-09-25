# 2. Create a derived class from Student as EnggStudent with :
    # a. Data members as :
        # i. Branch
        # ii. InternalMarks
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. override Method CalculateRank
        # v. Override __str__ Method



class Student:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print("Roll_Number:",self.roll_no)
        print("Name:",self.name)
       

# stud1=Student("Aman",1)

# stud1.display()

class Engineering_student(Student):

    def __init__(self,name=0,roll_no=0,branch=0,internal_mark=0,external_mark=0):
        
        super().__init__(name,roll_no)
        self.branch=branch
        self.internal_mark=internal_mark
        self.external_mark=external_mark

    def accept(self):

        self.name=input("Enter name: ")
        self.roll_no=int(input("Enter Roll Number :"))  
        self.branch=input("Enter Branch :")
        self.internal_mark=float(input("Enter Internal marks :"))
        self.external_mark=float(input("Enter External mark :"))

    def display(self):
        print("####################################################")
        super().display()
        print("Branch:",self.branch)
        print("Internel mark:",self.internal_mark)
        print("External mark:",self.external_mark)
        
    def calculate_rank(self):
            total=self.internal_mark+self.external_mark
            print("Total marks :",total)
            if( total >= 75):
                print("pass with distrinction")
            elif(total >= 60 and total < 75):
                print("Pass with the first class")
            elif(total >=50 and total<60):
                print("Pass with the second class")
            elif(total >=35 and total<50 ):
                print("pass")
            elif(total <35):
                print("Failed")

estud1=Engineering_student()

estud1.accept()

estud1.display()

estud1.calculate_rank()