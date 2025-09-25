# 1. Create a class Student with following
    # a. data members :
    # i. StudentId
    # ii. Name
    # iii. Age
    # iv. Percentage
        # b. Add the following methods :
        # i. Parameterized constructor
        # ii. Display
        # iii. Accept
        # iv. Method CalculateRank
        # v. Override __str__ Method


class Student:

    def datamethod(self,percentage,mar=0,hin=0,eng=0,py=0,jav=0,name=0,age=0):
        self.sname=name
        self.sage=age
        self.spercentage=percentage
        self.marathi=mar
        self.hindi=hin
        self.english=eng
        self.python=py
        self.java=jav 


    def accept(self):
        self.sname=input("Stdent name = ")
        self.sage=int(input("Student Age ="))
        self.marathi=float(input("Enter marathi marks :"))
        self.english=float(input("Enter english marks :"))
        self.hindi=float(input("Enter hindi marks :"))
        self.python=float(input("Enter Python marks :"))
        self.java=float(input("Enter java marks :"))


    def percentage(self,total_marks=0):
        print("########################################################")
        if (self.english <35):
            print("#### failed in english ####")
        elif(self.hindi<35):
            print("#### failed in hindi ####")
        elif(self.java < 35):
            print("#### failed in java ####")
        elif(self.python<35):
            print("#### Failed in python ####")
        elif(self.marathi<35):
            print("#### failed in marathi ####")
        total_marks=self.marathi+self.english+self.hindi+self.python+self.java

        self.percentage=total_marks/5
        print("percentage :",self.percentage,"%")

        
    def display(self):
        print("Student Name :",self.sname)
        print("Student Age :",self.sage)
        # print("Student Percentage :",self.spercentage)
        print(self.marathi,self.hindi,self.english,self.python,self.java)

    def calculateRank(self):

        if(self.percentage > 75 ):
            print("pass with Distinction")
        elif(self.percentage >= 60 and self.percentage < 75):
            print("Pass with the first class")
        elif(self.percentage >=50 and self.percentage<60):
            print("Pass with the second class")
        elif(self.percentage >=35 and self.percentage<50 ):
            print("pass")
        elif(self.percentage <35):
            print("Failed")


stud1=Student()

stud1.accept()

# stud1.display()

stud1.percentage()
stud1.calculateRank()