class vehicle():
    def __init__(self,num):
        self.num=num

    
class two_wheelers(vehicle):

    def cal_toll(self):
        # num=int(input("number of passanger :"))
        basic_toll=20
        total_toll=0
        if self.num > 2 :
            total_toll+=basic_toll+(self.num-2)*10
        else:
            total_toll+=basic_toll
        print("total cost of toll :",total_toll)

class three_wheelers(vehicle):
    def cal_toll(self):
        # num=int(input("number of passanger :"))
        basic_toll=30
        total_toll=0
        if self.num > 3 :
            total_toll+=basic_toll+(self.num-3)*20
        else:
            total_toll+=basic_toll

        print("total cost of toll :",total_toll)

class four_wheelers(vehicle):
    def cal_toll(self):

        # num=int(input("number of passanger :"))
        basic_toll=40
        total_toll=0
        if self.num > 4 :
            total_toll+=basic_toll+(self.num-4)*30
        else:
            total_toll+=basic_toll
        print("total cost of toll :",total_toll)

class heavy_vehicle(vehicle):
    
    def cal_toll(self):
        no_of_vehicle=int(input("enter number of wheels :"))
        if no_of_vehicle > 4 :
            # num=int(input("number of passanger :"))
            basic_toll=60
            total_toll=0
            if self.num > 6 :
                total_toll+=basic_toll+(self.num-6)*100
            else:
                total_toll+=basic_toll
            
        else:
            # num=int(input("number of passanger :"))
            basic_toll=40
            total_toll=0
            if self.num > 6 :
                total_toll+=basic_toll+(self.num-6)*100
            else:
                total_toll+=basic_toll

        print("total cost of toll :",total_toll)