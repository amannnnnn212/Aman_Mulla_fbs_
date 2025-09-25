# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.



class Shirt():
    discount=10
    def __init__(self,sid=154758,sname="Lacoste",stype="Formal Shirt",sprice=10000,ssize="L"):

        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.sprice=sprice
        self.ssize=ssize
        self.discountt=(sprice/100*Shirt.discount)+sprice
    def showshirt(self):
        print("#######################################")
        print("Shirt Id : ",self.sid)
        print("Shirt Brand Name : ",self.sname)
        print("Shirt Type : ",self.stype)
        print("Shirt Price : ",self.discountt)
        print("Shirt Size : ",self.ssize)        

    def __del__(self):

        print("distroctor is called")



shirt1=Shirt(1025,"U.S.Polo","Polo T shirt",1500,"XL")

shirt1.showshirt()

del shirt1

shirt2=Shirt()

shirt2.showshirt()
