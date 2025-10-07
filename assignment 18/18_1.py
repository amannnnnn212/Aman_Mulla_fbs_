# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class complex :
    
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __del__(self):
        print("Distructor is called")

        
    def __add__(self,other):

        self.real=self.real+other.real
        self.imag=self.imag + other.imag

        return self 

    def __sub__(self,other):
            
        self.real=self.real - other.real
        self.imag=self.imag - other.imag
        
        return self


    def __str__(self):
            
        return f" {self.real} + {self.imag}j "


obj1=complex(100,50)

obj2=complex(100,50)

print(obj1+obj2)




