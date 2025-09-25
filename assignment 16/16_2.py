# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.



class Product():
    discount=10
    def __init__(self,pid=1557,pname="Smart Phone",price=35000,quantity="3"):
        self.pid=pid
        self.pname=pname
        self.price=price
        self.quantity=quantity
        self.discountt=(price/100*Product.discount)
    def showproduct(self):
        print("#################################")
        print("Fixed discount 10% ")
        print("Product Id :",self.pid)
        print("Product Name :",self.pname)
        print("Product Price : ",self.price)
        print("After discount price : ",self.price-self.discountt)
        print("Product Quantity : ",self.quantity)


    def __del__(self):
        print("destroctor is called")
product1=Product(1001,"Laptop",50000,"2")

product1.showproduct()

del product1

product2=Product()

product2.showproduct()