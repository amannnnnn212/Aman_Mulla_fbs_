# 3. Create a class MedicalStudent inherited from Student with following :

        # i. Data members :Specialization
        # ii. MarksOfInternship
    # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. override Method CalculateRank
        # v. Override __str__ Method


class student :

    def __init__(self,name,college_n):
        self.name=name
        self.college_name=college_n

    def display(self):
        print("Name:",self.name)
        # print("Roll number:",self.roll_number)
        print("College name:",self.college_name)

# stud1=student("aman",1,"krushna")
# stud1.display()

class Medical_student(student):

    def __init__(self, roll_no=0, name=0, college_n=0,branch=0,i_mark=0,e_mark=0):
        super().__init__(name , college_n)
        self.internal_mark=i_mark
        self.external_mark=e_mark
        self.branch=branch
        self.roll_no=roll_no

    def accept(self):
        self.name=input("Enter name: ")
        self.roll_no=int(input("Enter Roll Number :"))
        self.college_name=input("Enter College Name:")
        self.branch=input("Enter Specialization :")
        self.internal_mark=float(input("Enter Internship marks :"))
        self.external_mark=float(input("Enter External mark :"))

    def display(self):
        print("#################################################")
        super().display()
        print("Roll Number:",self.roll_no)
        print("Specialization:",self.branch)
        print("Internship marks:",self.internal_mark)
        print("EXternal mark:",self.external_mark)
    
    def calculate_rank(self):
        total=self.internal_mark+self.external_mark
        print("Total marks:",total)
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

    

stud1=Medical_student()
stud1.accept()
stud1.display()
stud1.calculate_rank()