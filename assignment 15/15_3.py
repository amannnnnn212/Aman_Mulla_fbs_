# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. Showshirt


class Shirt():

    def __init__(self,sid=154758,sname="Lacoste",stype="Formal Shirt",sprice=10000,ssize="L-XL"):

        self.sid=sid
        self.sname=sname
        self.stype=stype
        self.sprice=sprice
        self.ssize=ssize

    def showshirt(self):
        print("#######################################")
        print("Shirt Id : ",self.sid)
        print("Shirt Brand Name : ",self.sname)
        print("Shirt Type : ",self.stype)
        print("Shirt Price : ",self.sprice)
        print("Shirt Size : ",self.ssize)        

    def __del__(self):

        print("distroctor is called")



shirt1=Shirt(1025,"U.S.Polo","Polo T shirt",1500,"S-XL")

shirt1.showshirt()

del shirt1

shirt2=Shirt()

shirt2.showshirt()
