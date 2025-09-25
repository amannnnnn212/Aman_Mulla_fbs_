# 1. Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.



class Book:

    count=0
    def __init__(self,bid=102,bname="Physcology Of Money",bprice=450,bauthor="Morgan Housel"):
        Book.count+=1
        self.bid=bid
        self.bname=bname
        self.bprice=bprice
        self.bauthor=bauthor

    def showbook(self):
        print("########################################")
        print("Book Id :",self.bid)
        print("Book Name :",self.bname)
        print("Book Price :",self.bprice)
        print("Book Author :",self.bauthor)
                
    def total_count():
        print("total count of an object : ",Book.count)

    def __del__(self):
        print("Destroctor is called")
book1=Book(101,"Rich Dad Poor Dad",500,"Robert Kiyosaki")

book2=Book()

book1.showbook()

del book1 

book2.showbook()

Book.total_count()

del book2 