# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. Showproduct

class Product():

    def __init__(self,pid=1557,pname="Smart Phone",price=35000,quantity="3"):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity

    def showproduct(self):
        print("#################################")
        print("Product Id :",self.pid)
        print("Product Name :",self.pname)
        print("Product Price : ",self.price)
        print("Product Quantity : ",self.quantity)

    def __del__(self):
        print("destroctor is called")
product1=Product(1001,"Laptop",50000,"5")

product1.showproduct()

del product1

product2=Product()

product2.showproduct()